import os
import pandas as pd


class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """

        csv_path1 = os.path.dirname(__file__)
        csv_path = os.path.join(csv_path1, '../data/csv')

        file_names = []
        for file in os.listdir(csv_path):
            if file.endswith(".csv"):
                file_names.append(file)


        key_names = []
        for file in file_names:
            clean_file = file.replace("_dataset.csv", "").replace(".csv", "").replace("olist_", "")
            key_names.append(clean_file)


        data = {}
        for key, file in zip(key_names, file_names):
            data[key] = pd.read_csv(os.path.join(csv_path, file))

        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")

# print(Olist().get_data()['sellers'].head())
