from insurance.pipeline.pipeline import Pipeline
from insurance.logger import logging
from insurance.config.configuration import Configuration
import os, sys

def main():
    config_path = os.path.join("Config", "config.yaml")
    pipeline = Pipeline(Configuration(config_file_path=config_path))

    pipeline.start()
    logging.info("main function execution completed.")

if __name__=="__main__":
    main()