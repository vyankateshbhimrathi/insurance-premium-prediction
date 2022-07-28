
from insurance.exception import HousingException
from insurance.constant import *
from insurance.entity.config_entity import *
from insurance.logger import logging
from insurance.util.util import read_yaml_file
import os, sys
from datetime import datetime





class Configuration:

    def __init__(self, config_file_path = CONFIG_FILE_PATH, current_time_stamp = CURRENT_TIME_STAMP) -> None:
        try:
            self.config_info = read_yaml_file(file_path=config_file_path)
            self.time_stamp = current_time_stamp
            self.training_pipeline_config = self.get_training_pipeline_config()
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        try:
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG]

            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir = os.path.join(artifact_dir, DATA_INGESTION_ARTIFACT_DIR, self.time_stamp)
            ingested_data_dir = os.path.join(data_ingestion_artifact_dir, data_ingestion_info[DATA_INGESTION_INGESTED_DIR_KEY])
            ingested_test_dir = os.path.join(ingested_data_dir, data_ingestion_info[DATA_INGESTION_INGESTED_TEST_DIR_KEY])
            ingested_train_dir = os.path.join(ingested_data_dir, data_ingestion_info[DATA_INDESTION_INGESTED_TRAIN_DIR_KEY])
            
            data_ingestion_config = DataIngestionConfig(ingested_test_dir=ingested_test_dir,
                                                        ingested_train_dir=ingested_train_dir)
            logging.info(f"data ingestion config : {data_ingestion_config}")
            return data_ingestion_config

        except Exception as e:
            raise HousingException(e, sys) from e


    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR, training_pipeline_config[TRAINING_PIPELINE_NAME],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR])
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"training pipeline config : {training_pipeline_config}")
            return training_pipeline_config
            
        except Exception as e:
            raise HousingException(e, sys) from e