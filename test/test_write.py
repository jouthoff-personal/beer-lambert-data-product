import pandas as pd

from src.write import write_model_to_json


def test_write_model_to_json():
    df1 = pd.DataFrame([1, 2], columns=['220'])
    df2 = pd.DataFrame([2, 2], columns=['220'])
    write_model_to_json(df1, df2)