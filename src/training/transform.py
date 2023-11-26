from typing import Tuple

import pandas as pd


def transform_calibration_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    df_with_concentrations = get_concentrations(df)
    blanks = get_blanks(df_with_concentrations)
    samples = get_samples(df_with_concentrations)
    training_data = drop_columns(samples)
    blanks_means = get_absorbance_means(drop_columns(blanks))

    return training_data, blanks_means


def drop_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop(columns=["Well", "Sample"])


def get_blanks(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["Sample"] == "Blank"]


def get_samples(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["Sample"] == "S1"]


def get_concentrations(df: pd.DataFrame) -> pd.DataFrame:
    df["Concentration"] = (1 / df["Dilution"]) * 50
    return df


def get_absorbance_means(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('Concentration', as_index=False).mean()

