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