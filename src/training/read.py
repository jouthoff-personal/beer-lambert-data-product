import pandas as pd


def read_calibration_data(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)
