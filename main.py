from src.KidneyDiseaseClassifier import logger
from src.KidneyDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.KidneyDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME} - {str(e)}")
    raise e


STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f">>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME} - {str(e)}")
    raise e