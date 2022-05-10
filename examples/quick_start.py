# import python modules
import os
import sys

# add package root
sys.path.append(os.getcwd())

from nstu_client import (ModelRun,
                             models_example)

# initial
start_model = ModelRun(models=models_example,
                     local_storage=os.path.join(os.getcwd(), "./data"))

# download model
start_model.download_model_by_name("numberplate_options")
start_model.download_repo_for_model("numberplate_options")

# ls local storage
models_list = start_model.ls_models_local()
print(models_list)




# model_hub == start_model
# modelhub_client == nstu_client
# ModelHub == ModelRun