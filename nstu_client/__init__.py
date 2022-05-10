"""
The nstu_client module.
"""
from .nstu_client import ModelRun
from .models_example import models_example
from .cli import main

__version__ = '1.1.0'

__all__ = (
    '__version__',
    'ModelRun', 'models_example',
    'main',
)



# model_hub == start_model
# modelhub_client == nstu_client
# ModelHub == ModelRun