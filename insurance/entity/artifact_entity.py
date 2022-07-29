from collections import namedtuple


DataIngestionArtifact = namedtuple('DataIngestionArtifact', ['train_file_path', 'test_file_path', 'is_ingested', 'message'])

DataValidationArtifact = namedtuple('DataValidationArtifact', ['schema_file_path', 'report_file_path', 'report_page_file_path',
                            'is_validated', 'message'])
                            
DataTransformationArtifact = namedtuple('DataTransformationArtifact', ['transformed_train_file_path', 'transformed_test_file_path',
                            'is_transformed', 'message', 'preprocessed_object_file_path'])