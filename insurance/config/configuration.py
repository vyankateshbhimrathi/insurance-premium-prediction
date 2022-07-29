
from insurance.exception import InsuranceException
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
            raise InsuranceException(e, sys) from e

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
            raise InsuranceException(e, sys) from e


    def get_data_validation_config(self) -> DataValidationConfig:

        try:
            data_validation_info = self.config_info[DATA_VALIDATION_CONFIG_KEY]
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_validation_artifact_dir = os.path.join(artifact_dir, DATA_VALIDATION_ARTIFACT_DIR, self.time_stamp)
            schema_file_path = os.path.join(ROOT_DIR, data_validation_info[DATA_VALIDATION_SCHEMA_DIR_KEY],
                        data_validation_info[DATA_VALIDATION_SCHEMA_FILE_NAME_KEY])
            report_file_path = os.path.join(data_validation_artifact_dir, data_validation_info[DATA_VALIDATION_REPORT_FILE_NAME_KEY])
            report_page_file_path = os.path.join(data_validation_artifact_dir, data_validation_info[DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY])


            data_validation_config = DataValidationConfig(schema_file_path=schema_file_path,report_file_path=report_file_path,
                                report_page_file_path=report_page_file_path)

            logging.info(f"data ingestion config : {data_validation_config}")
            return data_validation_config
            
        except Exception as e:
            raise InsuranceException(e, sys) from e


    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_transformation_info = self.config_info[DATA_TRANSFORMATION_CONFIG_KEY]

            data_transformation_artifact_dir = os.path.join(artifact_dir, DATA_TRANSFORMATION_ARTIFACT_DIR,
                            self.time_stamp)

            preprocessed_object_file_path = os.path.join(data_transformation_artifact_dir,
                                            data_transformation_info[DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY],
                                            data_transformation_info[DATA_TRANSFORMATION_PREPROCESSED_FILE_NAME_KEY])

            transformed_train_dir = os.path.join(data_transformation_artifact_dir,
                                    data_transformation_info[DATA_TRANSFORMATION_DIR_NAME_KEY],
                                    data_transformation_info[DATA_TRANSFORMATION_TRAIN_DIR_NAME_KEY])

            transformed_test_dir = os.path.join(data_transformation_artifact_dir,
                                    data_transformation_info[DATA_TRANSFORMATION_DIR_NAME_KEY],
                                    data_transformation_info[DATA_TRANSFORMATION_TEST_DIR_NAME_KEY])


            data_transformation_config = DataTransformationConfig(transformed_train_dir=transformed_train_dir,
                                                                transformed_test_dir=transformed_test_dir,
                                                                preprocessed_object_file_path=preprocessed_object_file_path)
            logging.info(f"data transformation config completed: {data_transformation_config}")
            
            return data_transformation_config
        except Exception as e:
            raise InsuranceException(e, sys) from e



    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR, training_pipeline_config[TRAINING_PIPELINE_NAME],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR])
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"training pipeline config : {training_pipeline_config}")
            return training_pipeline_config
            
        except Exception as e:
            raise InsuranceException(e, sys) from e