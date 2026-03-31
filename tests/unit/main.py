import logging
import os
import sys

from analytics_worker.config import Config
from analytics_worker.worker import Worker

def main():
    config = Config(os.environ)
    worker = Worker(config)

    logging.basicConfig(level=config.log_level, format=config.log_format)
    logger = logging.getLogger(__name__)

    try:
        worker.run()
    except Exception as e:
        logger.error(f"Error running worker: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()