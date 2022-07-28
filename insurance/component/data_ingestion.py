import os, sys
from insurance.constant import DATASET_FILE_PATH
from insurance.entity.config_entity import DataIngestionConfig
from insurance.entity.artifact_entity import DataIngestionArtifact
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from insurance.exception import HousingException
from insurance.logger import logging



class DataIngestion:

    def __init__(self, data_ingestion_config:DataIngestionConfig) -> None:
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config = data_ingestion_config
            
        except Exception as e:
            raise HousingException(e,sys)

    
    def split_data_as_train_test(self)-> DataIngestionArtifact:

        try:

            insurance_data_frame = pd.read_csv(DATASET_FILE_PATH)

            insurance_data_frame["bmi_cat"] = pd.cut(insurance_data_frame["bmi"],
                                bins=[15.0, 25.0, 35.0, 45.0, np.inf],
                                labels=[1,2,3,4])

            file_name = os.path.basename(DATASET_FILE_PATH)

            strat_train_set = None
            strat_test_set = None

            logging.info(f"train_test_split of data started")
            split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

            for train_index, test_index in split.split(insurance_data_frame, insurance_data_frame["bmi_cat"]):
                strat_train_set =insurance_data_frame.loc[train_index].drop(["bmi_cat"], axis=1)
                strat_test_set = insurance_data_frame.loc[test_index].drop(["bmi_cat"], axis=1)

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir, file_name)

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir, file_name)

            if strat_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir, exist_ok=True)
                logging.info(f"exporting train dataset to file: [{train_file_path}]")
                strat_train_set.to_csv(train_file_path, index=False)

            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok=True)
                logging.info(f"exporting test dataset to file: [{test_file_path}]")
                strat_test_set.to_csv(test_file_path, index=False)

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,test_file_path=test_file_path,
                                    is_ingested=True, message="data ingestion completed successfully.")
            
            logging.info(f"data ingestion artifact: [{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise HousingException(e, sys) from e


    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            return self.split_data_as_train_test()
        except Exception as e:
            raise HousingException(e, sys) from e
    
    def __del__(self):
        logging.info(f"{'='*20}Data Ingestion log completed.{'='*20} \n\n")