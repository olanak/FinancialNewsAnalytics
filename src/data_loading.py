import pandas as pd

def load_historical_datasets(file_paths):
    """
    Loads historical datasets from provided file paths and returns a dictionary of DataFrames.
    :param file_paths: List of paths to CSV files containing stock data.
    :return: Dictionary of DataFrames indexed by filename.
    """
    datasets = {}
    for file_path in file_paths:
        datasets[file_path] = pd.read_csv(file_path)
    return datasets

def load_raw_analyst_ratings(file_path):
    """
    Loads raw analyst ratings data from the given file path.
    :param file_path: Path to the CSV file containing raw analyst ratings.
    :return: DataFrame containing raw analyst ratings.
    """
    return pd.read_csv(file_path)
