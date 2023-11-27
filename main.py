from src.pipeline import calibrate_beer_lambert, estimate_concentration_fermentation_runs


def run_beer_lambert_data_product():
    print('Running calibration...')
    calibrate_beer_lambert()
    print('Estimating concentration for fermentation runs...')
    estimate_concentration_fermentation_runs()


if __name__ == "__main__":
    run_beer_lambert_data_product()
