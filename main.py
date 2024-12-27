from src.KidneyDiseaseClassifier import logger
from src.KidneyDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME} - {str(e)}")
    raise e