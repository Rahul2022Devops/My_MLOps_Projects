from My_Wine_Sample_Project.config.configuration import ConfigurationManager
from My_Wine_Sample_Project.components.data_validation import DataValidation
from My_Wine_Sample_Project import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        data_validation = DataValidation(config=data_validation_config)

        data_validation.validate_all_columns()