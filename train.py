"""
Training script to generate model and preprocessor artifacts
"""
import sys
import os

# Add the project root to the path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)

# Change to project root directory to ensure relative paths work correctly
os.chdir(project_root)

from src.FlightPricePrediction.pipeline.Training_pipeline import *
