import numpy as np
from pathlib import Path
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from dataset_loader import LoadDataset
from utils import load_config


config = load_config()
CURRENT_DIR = Path(__file__).resolve().parent
# Accessing Dataset
try:
    DOGS_DIR = CURRENT_DIR / config['dataset']['train_dogs_dir']
    CATS_DIR = CURRENT_DIR / config['dataset']['train_cats_dir']
except KeyError:
    raise ValueError("Config File Missing Dataset Paths!")


