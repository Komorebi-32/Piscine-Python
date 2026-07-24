import pandas as pandas


class FileLoader:
    def load(self, path):
        """takes as an argument the file path of the dataset to load,
        displays a message specifying the dimensions of the dataset (e.g. 340 x 500) and
        returns the dataset loaded as a pandas.DataFrame."""
        if not isinstance(path, str):
            print("Error: path should be a string")
            return None
        try:
            df = pandas.read_csv(path)
        except FileNotFoundError:
            print("Error: non existing file")
            return None
        print(f"Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}") # rows x columns
        return df

    def display(self, df, n):
        """takes a pandas.DataFrame and an integer as arguments,
        displays the first n rows of the dataset if n is positive, or the last n rows if n is
        negative."""
        if not isinstance(n, int) or not isinstance(df, pandas.DataFrame):
            print("Error: n should be int and df should be pandas.DataFrame")
            return
        if abs(n) > df.shape[0]:
            print("n exceeds the number of rows of the dataset. Displaying all the rows")
            n = df.shape[0]
        if n == 0:
            print("What did you expect ? Nothing to show mate")
            return
        if n > 0:
            print(df.head(n))
        else:
            print(df.tail(-n))
