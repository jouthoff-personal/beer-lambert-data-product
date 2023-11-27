import sys
import os

from src.pipeline import calibrate_beer_lambert


def predict_fermentation_run_concentrations():
    current_dir = os.getcwd()
    calibration_file_path = current_dir + '/src/data/calibration.csv'
    print('Running calibration...')
    calibrate_beer_lambert(calibration_file_path)


if __name__ == "__main__":
    predict_fermentation_run_concentrations()