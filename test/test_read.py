from src.read import read_calibration_data, download_run_data, read_sop_data, download_file_from_url, \
    read_fermentation_run_data


def test_read_calibration_data() -> None:
    # Given a csv filepath
    calibration_data_filepath = '../src/data/calibration.csv'
    # When read_calibration_data is called
    output = read_calibration_data(calibration_data_filepath)
    # Then the df has the correct number of rows
    assert len(output) == 27


def test_read_fermentation_run_data():
    url = 'https://drive.google.com/uc?export=download&id=1BhIbqzmNth7rG-3HXRTibzhCZY6wMb3L'
    download_file_from_url(url)

    output = read_fermentation_run_data(url)

    assert len(output) == 3


def test_download_run_data():
    output = download_run_data()

    assert len(output) == 27


def test_read_dye_house_data() -> None:
    output = read_sop_data()
    assert len(output) == 27


def test_download_file_from_url() -> None:
    url = 'https://drive.google.com/uc?export=download&id=1BhIbqzmNth7rG-3HXRTibzhCZY6wMb3L'
    download_file_from_url(url)