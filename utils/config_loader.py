import yaml
import os

def load_config(config_path: str = "config/config.yaml") -> dict:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "..", config_path)
    with open(config_path, "r") as file:
        config=yaml.safe_load(file)
    return config