import csv
import json
import pathlib
import typing

import attr


@attr.s(auto_attribs=True)
class FileDescriptor(object):
    filename: str = ""
    timestamp: str = ""
    description: str = ""
    file_type: str = ""

@attr.s(auto_attribs=True)
class FileDescriptors(object):
    descriptors: typing.List[FileDescriptor] = attr.Factory(list)
    fieldnames: typing.List[str] = ["filename", "timestamp", "description", "file_type"]
    filename: str = "manifest.csv"

    def add_descriptor(self, desc: FileDescriptor):
        self.descriptors.append(desc)

    def dump_to_csv(self, root_filepath: pathlib.Path):
        filename = pathlib.Path(root_filepath) / pathlib.Path(self.filename)
        with open(str(filename), 'w') as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames, delimiter=',', quoting = csv.QUOTE_MINIMAL)
            for d in self.descriptors:
                writer.writerow(attr.asdict(d))
