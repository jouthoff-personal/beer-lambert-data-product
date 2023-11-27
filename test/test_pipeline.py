from src.pipeline import calibrate_beer_lambert


def test_calibrate_beer_lambert_model():
    [output1, output2] = calibrate_beer_lambert('../src/data/calibration.csv')

    output1
    output2
