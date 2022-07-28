from insurance.entity.config_entity import DataValidationConfig
from insurance.exception import InsuranceException
from insurance.logger import logging
from insurance.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
import os, sys
import json
from insurance.util.util import read_yaml_file
import pandas as pd
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab





class DataValidation:

    def __init__(self, data_validation_config:DataValidationConfig,
                data_ingestion_artifact:DataIngestionArtifact) -> None:
        try:
            logging.info(f"{'>>'*30}Data Valdaition log started.{'<<'*30} \n\n")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact

        except Exception as e:
            raise InsuranceException(e, sys) from e
    

    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df, test_df
        except Exception as e:
            raise InsuranceException(e, sys) from e
    
    def is_train_test_file_exists(self)-> bool:
        try:
            is_train_file_exist = False
            is_test_file_exist = False

            logging.info("checking if train_test_file path exists started")
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available = is_train_file_exist and is_test_file_exist

            logging.info(f"Is train_test_file_exists?-> {is_available}")

            if not is_available:
                message = f"Training file: {train_file_path} or Testing file: {test_file_path}" \
                            "is not present"
                raise Exception (message)

            return is_available

        except Exception as e:
            raise InsuranceException(e, sys) from e

    def validate_dataset_schema(self)-> bool:
        try:
            validation_status = False

            schema_file_path = self.data_validation_config.schema_file_path
            schema_file_info = read_yaml_file(file_path=schema_file_path)

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            for file_path in [train_file_path, test_file_path]:
                df = pd.read_csv(file_path)
                if df.shape[1] == len(schema_file_info['columns'].keys()):
                    for column in df.columns:
                        if column not in schema_file_info['columns'].keys():
                            message = f"This column {column} of {file_path} is not present in schema file"
                            logging.info(f"{message}")
                            raise Exception (message)
                        else:
                            validation_status = True
                    for item in schema_file_info['domain_value'].keys():
                        if len(df[item].value_counts().index) == len(schema_file_info['domain_value'][item]):
                            for value in df[item].value_counts().index:
                                if value not in schema_file_info['domain_value'][item]:
                                    message = f"The attribute {value} is not present in {item} column  of {file_path}."
                                    logging.info(f"{message}")
                                    raise Exception (message)
                                else:
                                    validation_status = True
    
                        else:
                            logging.info(f"attributes present in {item} column of {file_path} is not equal to" \
                            "{len(schema_file_info['domain_value'][item])}")
                            raise Exception(f"attributes present in {item} column of {file_path} is not equal to" \
                            "{len(schema_file_info['domain_value'][item])}")

                else:
                    logging.info(f"dataframe columns =  {df.shape[1]} of {file_path} is not equal to schema file column length")
                    raise Exception(f"dataframe columns =  {df.shape[1]} of {file_path} is not equal to schema file column length")

            return validation_status

        except Exception as e:
            raise InsuranceException(e, sys) from e


    def get_and_save_data_drift_report(self):
        try:
            train_df, test_df = self.get_train_and_test_df()
            profile = Profile(sections=[DataDriftProfileSection()])

            profile.calculate(train_df, test_df)

            report = json.loads(profile.json())

            report_file_path = self.data_validation_config.report_file_path

            report_dir = os.path.dirname(report_file_path)

            os.makedirs(report_dir, exist_ok=True)

            with open(self.data_validation_config.report_file_path, 'w') as report_file:
                json.dump(report, report_file, indent=6)
            return report
        except Exception as e:
            raise InsuranceException(e, sys) from e
    
    def save_data_drift_report_page(self):
        try:
            train_df, test_df = self.get_train_and_test_df()
            dashboard = Dashboard(tabs=[DataDriftTab()])

            dashboard.calculate(train_df, test_df)

            report_page_file_path = self.data_validation_config.report_page_file_path
            report_page_dir = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir,exist_ok=True)

            dashboard.save(report_page_file_path)
        except Exception as e:
            raise InsuranceException(e, sys) from e
    
    def is_data_drift_found(self)-> bool:
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()
            return True
        except Exception as e:
            raise InsuranceException(e, sys) from e


    def initiate_data_validation(self)-> DataValidationArtifact:
        try:
            is_available = self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift_found()
            data_validation_artifact = DataValidationArtifact(schema_file_path=self.data_validation_config.schema_file_path,
                                    report_file_path=self.data_validation_config.report_file_path,
                                    report_page_file_path=self.data_validation_config.report_page_file_path,
                                    is_validated=True,
                                    message="data validation completed successfully")
            return data_validation_artifact
        except Exception as e:
            raise InsuranceException(e, sys) from e

    def __del__(self):
        logging.info(f"{'>>'*30}Data Valdaition log completed.{'<<'*30} \n\n")