from loguru import logger

from config import settings
from delivery.worker.consumer_runner import run_consumer
from utils.logger import setup_logger


def main():
    setup_logger()
    logger.info("Starting processor-service")
    logger.info("Log level: {}", settings.log_level)
    run_consumer()

if __name__ == "__main__":
    main()
