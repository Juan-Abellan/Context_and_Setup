import os
import pandas as pd


class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities

        csv_path = os.path.dirname(__file__)
        csv_path = os.path.join(csv_path, '../data/csv')
        #print(csv_path)
        #pd.read_csv(os.path.join(csv_path, 'olist_sellers_dataset.csv')).head()

        file_names = []
        for file in os.listdir(csv_path):
            if file.endswith(".csv"):
                file_names.append(file)
        file_names

        key_names = []
        for file in file_names:
            clean_file = file.replace("_dataset.csv", "").replace(".csv", "").replace("olist_", "")
            key_names.append(clean_file)
        key_names

        data = {}
        for key, file in zip(key_names, file_names):
            #print(key, file)
            data[key] = pd.read_csv(os.path.join(csv_path, file))

        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
