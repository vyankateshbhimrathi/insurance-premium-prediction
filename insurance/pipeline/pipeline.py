

from insurance.config.configuration import Configuration
from insurance.exception import HousingException
from insurance.logger import logging
import os, sys
from insurance.entity.artifact_entity import *
from insurance.component.data_ingestion import DataIngestion


class Pipeline:

    def __init__(self, config: Configuration=Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise HousingException(e, sys) from e


    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HousingException(e, sys) from e

    
    def run_pipeline(self):
        try:
            self.start_data_ingestion()
        except Exception as e:
            raise HousingException(e, sys) from e