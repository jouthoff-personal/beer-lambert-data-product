import pandas as pd

from src.training.transform import get_blanks, get_samples, get_absorbance_means, transform_calibration_data, \
    get_concentrations


def test_get_blanks():
    # Given a df with Blank and Other types
    df = pd.DataFrame(["Blank", "Blank", "Other"], columns=['Sample'])
    # When get_blanks is called
    output = get_blanks(df)
    # Then the output df only contains Blanks
    assert len(output) == 2


def test_get_samples():
    # Given a df with Samples and Other types
    df = pd.DataFrame(["S1", "S1", "Other"], columns=['Sample'])
    # When get_samples is called
    output = get_samples(df)
    # Then the output df only contains Samples
    assert len(output) == 2


def test_get_concentrations():
    # Given a df with Dilution values
    df = pd.DataFrame([[1, 'S1'], [2, 'S1'], [4, 'S1']], columns=['Dilution', 'Sample'])
    # When get_concentrations is called
    output = get_concentrations(df)
    # Then the output df contains column Concentration with calculated concentrations
    assert df["Concentration"][0] == 50
    assert df["Concentration"][1] == 25
    assert df["Concentration"][2] == 12.5
    assert df["Dilution"][0] == 1


def test_get_absorbance_means():
    # Given a df with multiple dilutions
    df = pd.DataFrame([[1, 4], [1, 5], [1, 6], [128, 1], [128, 2], [128, 3]], columns=['Concentration', '220'])
    # When get_means is called
    output = get_absorbance_means(df)
    # Then the mean of each dilution for each wavelength is calculated
    assert output['220'][1] == 5.0
    assert output['220'][128] == 2.0


def test_transform_calibration_data():
    df = pd.read_csv('../../src/training/data/calibration.csv')

    [output1, output2] = transform_calibration_data(df)

    assert len(output1) == 24
