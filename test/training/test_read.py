from src.training.read import read_calibration_data


def test_read_calibration_data() -> None:
    calibration_data_filepath = '../../src/training/data/calibration.csv'

    output = read_calibration_data(calibration_data_filepath)

    assert len(output) == 27
