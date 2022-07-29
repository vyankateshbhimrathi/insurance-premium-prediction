from datetime import datetime
import os

ROOT_DIR = os.getcwd()


def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

config_path = "Config"
config_file = "config.yaml"

dataset_path = "dataset"
dataset_file = "insurance.csv"

CONFIG_FILE_PATH = os.path.join(ROOT_DIR, config_path, config_file)

DATASET_FILE_PATH = os.path.join(ROOT_DIR, dataset_path, dataset_file)

CURRENT_TIME_STAMP = get_current_time_stamp()

# training pipeline variable

TRAINING_PIPELINE_CONFIG_KEY = 'training_pipeline_config'
TRAINING_PIPELINE_NAME = 'pipeline_name'
TRAINING_PIPELINE_ARTIFACT_DIR = 'artifact_dir'

# data ingestion variables

DATA_INGESTION_CONFIG = 'data_ingestion_config'
DATA_INGESTION_ARTIFACT_DIR = 'data_ingestion'
DATA_INGESTION_INGESTED_DIR_KEY = 'ingested_dir'
DATA_INDESTION_INGESTED_TRAIN_DIR_KEY = 'ingested_train_dir'
DATA_INGESTION_INGESTED_TEST_DIR_KEY = 'ingested_test_dir'

# data validation variables

DATA_VALIDATION_CONFIG_KEY = 'data_validation_config'
DATA_VALIDATION_ARTIFACT_DIR = 'data_validation'
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY = 'schema_file_name'
DATA_VALIDATION_SCHEMA_DIR_KEY = 'schema_dir'
DATA_VALIDATION_REPORT_FILE_NAME_KEY = 'report_file_name'
DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY = 'report_page_file_name'

# Data Transformation related variables
DATA_TRANSFORMATION_ARTIFACT_DIR = "data_transformation"
DATA_TRANSFORMATION_CONFIG_KEY = "data_transformation_config"
DATA_TRANSFORMATION_DIR_NAME_KEY = "transformed_dir"
DATA_TRANSFORMATION_TRAIN_DIR_NAME_KEY = "transformed_train_dir"
DATA_TRANSFORMATION_TEST_DIR_NAME_KEY = "transformed_test_dir"
DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY = "preprocessing_dir"
DATA_TRANSFORMATION_PREPROCESSED_FILE_NAME_KEY = "preprocessed_object_file_name"

NUMERICAL_COLUMN_KEY="numerical_columns"
CATEGORICAL_COLUMN_KEY = "categorical_columns"
TARGET_COLUMN_KEY="target_column"
DATASET_SCHEMA_COLUMNS_KEY=  "columns"
