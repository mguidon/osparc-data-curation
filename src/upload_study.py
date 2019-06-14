from blackfynn import Blackfynn
from blackfynn.models import Collection
import datcore as dc
from pathlib import Path

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
api_token = os.environ.get("BF_API_KEY", "none")
api_secret = os.environ.get("BF_API_SECRET", "none")

client = dc.DatcoreClient(api_token=api_token, api_secret=api_secret)

ds = client.create_dataset("Curation")
client.delete_files(ds)

study_name = "osparc-dataset-template"

study_folder = Path(dir_path).parent / Path(study_name)

def recursive_upload(destination, files):
    dirs = [f for f in files if os.path.isdir(f)]
    files = [f for f in files if os.path.isfile(f)]

    if len(files) > 0:
        client.upload_file(destination, files)
        #print("uploading files: " , files)

    for d in dirs:
        name = os.path.basename(os.path.normpath(d))
        print('Uploading to {}'.format(name))

        new_collection = Collection(name)
        destination.add(new_collection)

        files = [os.path.join(d,f) for f in os.listdir(d) if not f.startswith('.')]
        recursive_upload(new_collection, files)


files = [os.path.join(study_folder, f) for f in os.listdir(str(study_folder))]
recursive_upload(ds, files)