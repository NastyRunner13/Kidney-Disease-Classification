from src.KidneyDiseaseClassifier.components.prepare_base_model import PrepareBaseModel
from src.KidneyDiseaseClassifier.config.configuration import ConfigurationManager
from src.KidneyDiseaseClassifier import logger

STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME} - {str(e)}")
        raise e