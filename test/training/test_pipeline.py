from src.training.pipeline import calibrate_beer_lambert_model


def test_calibrate_beer_lambert_model():
    [output1, output2] = calibrate_beer_lambert_model('../../src/training/data/calibration.csv')

    output1
    output2
