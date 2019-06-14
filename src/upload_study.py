from blackfynn import Blackfynn
from blackfynn.models import Collection
from dataset_description import DatasetDescriptor
import datcore as dc
from pathlib import Path
import csv
from datetime import date
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
api_token = os.environ.get("BF_API_KEY", "none")
api_secret = os.environ.get("BF_API_SECRET", "none")

client = dc.DatcoreClient(api_token=api_token, api_secret=api_secret)

ds = client.create_dataset("Curation")
client.delete_files(ds)

study_name = "osparc-dataset-template"

study_folder = Path(dir_path).parent / Path(study_name)
study_file = Path(study_folder) / Path("study/project.json")


def submission(root_folder):
    filename = Path(root_folder) / Path("submission.csv")
    with open(str(filename), 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(["SPARC Award number", "OT3OD025348"])
        writer.writerow(["Milestone achieved", "Milestone 0.0.1"])
        writer.writerow(["Milestone completion date", date.today()] )
        
def dataset_description(root_folder, study_file):
    filename = Path(root_folder) / Path("dataset_description.csv")
    dd = DatasetDescriptor()
    dd.from_study_file(study_file)
    dd.dump_to_csv(filename)


submission(study_folder)
dataset_description(study_folder, study_file)

aa
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