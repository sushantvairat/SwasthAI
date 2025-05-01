import json
from ..utils.logger import get_logger

def load_config(config_path):
    logger = get_logger("Config")
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
        logger.info(f"Configuration loaded from {config_path}")
        return config
    except Exception as e:
        logger.error(f"Error loading config: {str(e)}")
        return {} 
