import pandas as pandas


class FileLoader:
    def load(self, path):
        if not isinstance(path, str):
            print("Error: path should be a string")
            return None
        try:
            file = pandas.read_csv(path)
        except FileNotFoundError:
            print("Error: non existing file")
            return None
        print(f"Loading dataset of dimensions {file.shape[0]} x {file.shape[1]}")
        return file