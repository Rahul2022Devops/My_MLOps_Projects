from My_Wine_Sample_Project.config.configuration import ConfigurationManager
from My_Wine_Sample_Project.components.model_trainer import ModelTrainer
from My_Wine_Sample_Project import logger
from pathlib import Path


STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                model_trainer_config = config.get_model_trainer_config()
                model_trainer = ModelTrainer(config=model_trainer_config)
                model_trainer.train()   

            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)