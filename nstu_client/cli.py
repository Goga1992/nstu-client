import json
import argparse
from . import (ModelRun,
               models_example)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('action',
                        choices=['config_format', 'auth', "remote_store"])
    parser.add_argument('--remote_url',
                        type=str,
                        required=False,
                        help='Save nstu remote remote_url')
    parser.add_argument('--config_path',
                        type=str,
                        required=False,
                        help='config_path for remote_store action')
    args = vars(parser.parse_args())
    return args


def main():
    args = parse_args()
    if args["action"] == "config_format":
        print(json.dumps(models_example, indent=4, sort_keys=False))
    elif args["action"] == "auth":
        start_model = ModelRun()
        start_model.get_auth()
        print("Current remote storage", start_model.remote_storage)
        if not args.get("remote_url", None):
            return
        start_model.save_auth(args["remote_url"])
        print("Changed remote storage:", args["remote_url"])
    elif args["action"] == "remote_store":
        if not args.get("config_path", None):
            return
        start_model = ModelRun()
        if args.get("remote_url", None):
            start_model.remote_storage = args["remote_url"]
        else:
            start_model.get_auth()
        config_path = args["config_path"]
        start_model.store_remote_by_json(config_path)


# model_hub == start_model
# modelhub_client == nstu_client
# ModelHub == ModelRun