# import python modules
import os
import sys
import unittest

# add package root
sys.path.append(os.getcwd())

from nstu_client import (ModelRun,
                             models_example)


class ModelRunClientTest(unittest.TestCase):
    def test_download_model_by_name(self) -> None:
        start_model = ModelRun(models=models_example,
                             local_storage=os.path.join(os.getcwd(), "./data"))
        start_model.download_model_by_name("numberplate_options")
        models_list = start_model.ls_models_local()
        self.assertEqual(models_list, ["numberplate_options_2021_05_23.pt"])

    def test_download_repo_for_model(self) -> None:
        start_model = ModelRun(models=models_example,
                             local_storage=os.path.join(os.getcwd(), "./data"))
        start_model.download_repo_for_model("numberplate_options")
        repos_list = start_model.ls_repos_local()
        self.assertEqual(repos_list, ["lpr-nstu"])

    def test_download_dataset_for_model(self) -> None:
        start_model = ModelRun(models=models_example,
                             local_storage=os.path.join(os.getcwd(), "./data"))
        start_model.download_dataset_for_model("numberplate_options")
        datasets_list = start_model.ls_datasets_local()
        self.assertEqual(datasets_list, ["autoriaNumberplateOptionsDataset-2021-05-17"])


if __name__ == '__main__':
    unittest.main()


# model_hub == start_model
# modelhub_client == nstu_client
# ModelHub == ModelRun
# ModelHubClientTest == ModelRunClientTest
