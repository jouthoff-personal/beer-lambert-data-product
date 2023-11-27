import tempfile

import gdown
import pandas as pd
import requests
from pandas import read_csv

TEMP_DIR = tempfile.TemporaryDirectory()


def read_calibration_data(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)


def read_fermentation_run_data(url):
    tempfile_name = TEMP_DIR.name + url[-10:] + '.csv'
    return read_csv(tempfile_name)


def download_run_data():
    runs = read_sop_data()
    for run in runs:
        download_file_from_url(run['url'])
    return runs


def read_sop_data():
    notion_token = 'secret_SBzckpdOOtWsu7R6BSt3rEMPP2XIrakgLogPOg9ItnW'
    database_id = '558261863d3b40d2a2d403748079e37f'
    url = f'https://api.notion.com/v1/databases/{database_id}/query'

    r = requests.post(url, headers={
        "Authorization": f"Bearer {notion_token}",
        "Notion-Version": "2021-08-16"
    })

    result_dict = r.json()
    result = result_dict['results']

    fermentation_runs = []

    for run in result:
        fermentation_runs_dict = map_notion_result_to_fermentation_run(run)
        fermentation_runs.append(fermentation_runs_dict)

    return fermentation_runs


def map_notion_result_to_fermentation_run(result):
    # you can print result here and check the format of the answer.
    properties = result['properties']

    return {
        'client': properties['Client']['select']['name'],
        'date': properties['Date']['date']['start'],
        'url': properties['Download URL']['url']
    }


def download_file_from_url(url: str):
    tempfile_name = TEMP_DIR.name + url[-15:] + '.csv'
    gdown.download(url, tempfile_name)


def clean_up_tempfiles():
    TEMP_DIR.cleanup()


def read_model_from_json():
    return pd.read_json('calibrated_model.json')
