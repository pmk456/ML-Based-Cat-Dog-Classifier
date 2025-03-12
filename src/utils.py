import os
from yaml import safe_load, YAMLError
def load_config():
    """ Loading YAML Config File """
    config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "config.yaml")
    if not os.path.exists(config_path):
        
        raise FileNotFoundError("Config File Not Found!")
    
    with open(config_path, "r") as file:    
        try:
            return safe_load(file)
        except YAMLError:
            raise YAMLError("Error Loading Config File!")