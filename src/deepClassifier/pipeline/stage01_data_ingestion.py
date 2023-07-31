from deepClassifier.config import ConfigurationManager
from deepClassifier.components import DataIngestion
from deepClassifier import logger

Stage_name = "dataIngestion stage"


def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>{Stage_name} started <<<<<<")
        main()
        logger.info(f">>>>>{Stage_name} completed successfully <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
