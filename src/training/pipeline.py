from src.training.read import read_calibration_data
from src.training.transform import transform_calibration_data


def calibrate_beer_lambert_model(calibration_data_filepath):
    calibration_data = read_calibration_data(calibration_data_filepath)
    [transformed_samples, blanks_mean_by_wavelength] = transform_calibration_data(calibration_data)
    return




