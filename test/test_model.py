import pandas as pd
import pytest

from src.model import calibration_model, calibrate_beer_lambert_model, predict_concentrations


def test_calibrate_beer_lambert_model_model():
   df = pd.DataFrame([[50.0, 3.0, 3.0], [25.0, 3.7, 3.1], [12.5, 4.2, 3.2], [6.25, 4.7, 3.3], [3.125, 5.2, 3.4]], columns=['Concentration', '220', '230'])

   output = calibrate_beer_lambert_model(df)

   assert output['230'][0] == pytest.approx(-112.5)
   assert round(output['230'][0], 2) == 379.38


def test_calibration_model():
    concentration = pd.Series([20, 40, 60, 80, 100, 120, 140, 160, 180, 200]).values
    absorbance = pd.Series([0.0060, 0.0111, 0.0233, 0.0546, 0.0489, 0.0675, 0.0654, 0.0625, 0.0785, 0.0705]).values

    output = calibration_model(concentration, absorbance)

    assert round(output[0][0], 2) == pytest.approx(2128.97)
    assert round(output[1][0], 2) == pytest.approx(6.04)


def test_predict_concentrations():
    run_data = pd.DataFrame([3.0, 3.4, 2.8], columns=['220'])
    model = pd.DataFrame([1, 0], columns=['220'], index=['coefficient', 'intercept'])
    output = predict_concentrations(run_data, model)

    assert len(output) == 3
    assert output['220'][0] == 3.0
