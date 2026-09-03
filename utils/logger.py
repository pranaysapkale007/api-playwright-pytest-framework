import logging
import os

def get_logger(name="api_framework"):
    """
    Create and configure a logger.
    Logs will be written both to console and to a log file.
    """
    logger = logging.getLogger(name)

    if not logger.handlers:  # Prevent duplicate handlers
        # Create reports/logs directory if not exists
        os.makedirs("reports/logs", exist_ok=True)

        # Console handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(console_formatter)

        # File handler
        file_handler = logging.FileHandler("reports/logs/framework.log")
        file_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(file_formatter)

        # Add both handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        logger.setLevel(logging.INFO)

    return logger
