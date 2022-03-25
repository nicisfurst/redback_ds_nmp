# data_handling.py
# includes functions for reading / writing data


# Imports
from pandas import read_csv, DataFrame


# Constants
RAW_DATA_DIR = 'data/raw/'
PARAMS_FILE = 'input_params.csv'
DATA_FILE = 'output.csv'


# Loads a specific setup's input params
def load_setup_params(subsection: int, division: int = 0) -> DataFrame:
    data = read_csv(f"{RAW_DATA_DIR}/data{division}_{subsection:02}/{PARAMS_FILE}")
    return data
    # TODO: add error handling


# Loads a specific setup's output data
def load_setup_output(subsection: int, division: int = 0) -> DataFrame:
    data = read_csv(f"{RAW_DATA_DIR}data{division}_{subsection:02}/{DATA_FILE}")
    return data
    # TODO: add error handling


# Loads all data for a specific setup
def load_setup_all(subsection: int, division: int = 0) -> list[2]:
    params = load_setup_params(subsection, division)
    data = load_setup_output(subsection, division)
    return [params, data]
