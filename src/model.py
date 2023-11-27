import pandas as pd
from sklearn.linear_model import LinearRegression


def calibrate_beer_lambert_model(df: pd.DataFrame):
    coefficients = pd.DataFrame(columns=df.columns).drop(['Concentration', 'Dilution'], axis=1)
    intercepts = pd.DataFrame(columns=df.columns).drop(['Concentration', 'Dilution'], axis=1)
    for column in df.columns:
        if column not in ('Concentration', 'Dilution'):
            coefficients[column], intercepts[column] = calibration_model(df['Concentration'].values, df[column].values)
    return wrap_model(coefficients, intercepts)


def wrap_model(coefficients, intercepts):
    model = pd.concat([coefficients, intercepts])
    model.index = ['coefficient', 'intercept']
    print(model)
    return model


def calibration_model(concentration, absorbance):
    concentration = concentration.reshape(len(concentration), 1)
    absorbance = absorbance.reshape(len(absorbance), 1)
    model = LinearRegression(fit_intercept=True)
    model.fit(absorbance, concentration)
    return model.coef_[0], model.intercept_


def predict_concentrations(run_data, model):
    prediction = pd.DataFrame(columns=run_data.columns)
    for column in run_data.columns:
        prediction[column] = (model.at["coefficient", column] * run_data[column].values) + model.at["intercept", column]
    return prediction


