# RIA ModelRun Client

## Installation
```bash
pip3 install git+https://github.com/ria-com/modelhub-client.git
```
or
```bash
git clone https://github.com/ria-com/modelhub-client.git
cd ./modelhub-client
python3 setup.py install
```

## Quick Start
```python3
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
# start_model.download_repo_for_model("numberplate_options")
# start_model.download_dataset_for_model("numberplate_options")

# ls local storage
models_list = start_model.ls_models_local()
print(models_list)
```

## Config Example
```python3
{   
    # unique model name
    "numberplate_options": {
        # application name 
        "application": "Numberplate Options Application",
        
        # model url for downloading 
        # model will be downloaded into 
        # [local_storage]/models/[application]/[model_name] dir
        "url": "https://nomeroff.net.ua/models/options/torch/numberplate_options_2021_05_23.pt",
        
        # path to model
        # if not exists model will by downloaded by `url`
        "path": "",
        
        # model dataset url for downloading
        # dataset will be downloaded into 
        # [local_storage]/datasets/[application]/[model_name] dir
        "dataset": "https://nomeroff.net.ua/datasets/autoriaNumberplateOptionsDataset-2021-05-17.zip",
        
        # path to dataset
        # if not exists dataset will by downloaded by `dataset`
        "dataset_path": "",
        
        # model repo url for cloning
        # and pushing into PATH
        # repo will be cloned into 
        # [local_storage]/repos/[application]/[model_name] dir
        "repo": "https://github.com/ria-com/nomeroff-net",
        
        # path to repo
        # if not exists repo will by downloaded by `repo`
        "repo_path": "",
        
        # model description (not required)
        "description": "Numberplate Options Classification",
        
        # model task (not required)
        "task": "Classification",
        
        # model type (not required)
        "type": "Supervised Learning",
        
        # model architecture (not required)
        "architecture": "CNN",
    }
}
```

## Simple ModelRun Nginx Server Example 
```nginx
server {
    # Port
    listen 5000;
    
    location /storage {
        # MAX size of uploaded file, 0 mean unlimited
        client_max_body_size 0;
        
        # Allow autocreate folder here if necessary
        create_full_put_path    on;
        
        # Temporary folder
        client_body_temp_path /tmp;
        
        # dav allowed method
        dav_methods     PUT DELETE MKCOL COPY MOVE;
        
        # In this folder, newly created folder or file is to have specified permission. If none is given, default is user:rw. If all or group permission is specified, user could be skipped
        dav_access      user:rw group:rw all:r;
        
        # Local folder
        alias /data/modelhub;
    }
```

## Command Line Interface
get models config example
```bash
nstu_client config_format
```

get current remote hub
```bash
nstu_client auth 
```

set remote hub
```bash
nstu_client auth --remote_url=127.0.0.1:5000 
```

load local models/datasets by `--config_path` into hub `--remote_url`
```bash
nstu_client remote_store --remote_url=127.0.0.1:5000 --config_path=./data/remote_loading_json_eample.json 
```

if auth load local models/datasets by `--config_path` into authed hub
```bash
nstu_client remote_store --config_path=./data/remote_loading_json_eample.json
```

## Tests
```bash
python3 ./tests/test.py
```


# model_hub == start_model
# modelhub_client == nstu_client
# ModelHub == ModelRun
# ModelHubClientTest == ModelRunClientTest