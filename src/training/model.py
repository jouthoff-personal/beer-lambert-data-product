import pandas as pd
from sklearn.linear_model import LinearRegression


def train_model(df: pd.DataFrame):
    coefficients = pd.DataFrame(columns=df.columns)
    intercepts = pd.DataFrame(columns=df.columns)
    for column in df.columns:
        if column not in ('Concentration', 'Dilution'):
            coefficients[column], intercepts[column] = calibration_model(df['Concentration'].values, df[column].values)
    return coefficients, intercepts


def calibration_model(concentration, absorbance):
    concentration = concentration.reshape(len(concentration), 1)
    absorbance = absorbance.reshape(len(absorbance), 1)
    model = LinearRegression(fit_intercept=True)
    model.fit(absorbance, concentration)
    return model.coef_[0], model.intercept_


def predict(df: pd.DataFrame):
    pass

