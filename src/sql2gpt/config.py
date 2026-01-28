import os
import json

CONFIG_DIR = ".sql2gpt"


def load(config_dir=CONFIG_DIR) -> dict:
    # Define config directory and file paths
    config_dir = os.path.join(os.path.expanduser("~"), config_dir)
    dbs_file = os.path.join(config_dir, "dbs.json")

    # Create config directory if it doesn't exist
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    # Create dbs.json file with an empty JSON object if it doesn't exist
    if not os.path.exists(dbs_file):
        with open(dbs_file, "w") as file:
            json.dump({}, file)

    # Load and return the config as a dictionary
    with open(dbs_file, "r") as file:
        config = json.load(file)

    return config


def add(name: str, database_url: str, config_dir=CONFIG_DIR) -> None:
    config = load(config_dir)
    config[name] = database_url
    # save the config
    config_dir = os.path.join(os.path.expanduser("~"), config_dir)
    dbs_file = os.path.join(config_dir, "dbs.json")
    with open(dbs_file, "w") as file:
        json.dump(config, file)
