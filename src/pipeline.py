from src.model import calibrate_beer_lambert_model, predict_concentrations
from src.read import read_calibration_data, download_run_data, read_fermentation_run_data, read_model_from_json
from src.transform import transform_calibration_data, transform_fermentation_runs_data
from src.write import write_model_to_json, write_predicted_concentrations_to_json


def calibrate_beer_lambert(calibration_data_filepath):
    calibration_data = read_calibration_data(calibration_data_filepath)
    [transformed_samples, blanks_mean_by_wavelength] = transform_calibration_data(calibration_data)
    model = calibrate_beer_lambert_model(transformed_samples)
    write_model_to_json(model)


def estimate_concentration_fermentation_runs():
    model = read_model_from_json()
    fermentation_runs = download_run_data()
    for run in fermentation_runs:
        run_data = read_fermentation_run_data(run['url'])
        [prediction_data, blanks] = transform_fermentation_runs_data(run_data)
        preds = predict_concentrations(prediction_data, model)
        write_predicted_concentrations_to_json(preds, run)



