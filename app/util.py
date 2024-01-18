import logging
import yaml


def parse_config(config_file_name: str):
    with open(config_file_name, "r", encoding="utf-8") as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            logging.error(e)
            raise e

        return config
