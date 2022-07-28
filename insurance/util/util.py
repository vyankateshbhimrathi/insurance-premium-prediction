from insurance.exception import HousingException
import os, sys
import yaml


def read_yaml_file(file_path:str)->dict:
    """
    reads a yaml file and returns content of the file in dictionary format.
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            config_file_info = yaml.safe_load(yaml_file)
            return config_file_info
    except Exception as e:
        raise HousingException (e,sys) from e