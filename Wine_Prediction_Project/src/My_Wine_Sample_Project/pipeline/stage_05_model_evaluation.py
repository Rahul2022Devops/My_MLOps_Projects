from My_Wine_Sample_Project.entity.config_entity import ModelEvaluationConfig
from My_Wine_Sample_Project.utils.common import logger
from My_Wine_Sample_Project.config.configuration import ConfigurationManager
from My_Wine_Sample_Project.components.model_evaluation import ModelEvaluation

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.save_results()
        except Exception as e:
            logger.exception(e)
            raise e