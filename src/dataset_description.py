import csv
import json
import pathlib
import typing

import attr


@attr.s(auto_attribs=True)
class DatasetDescriptor(object):
    filename: str = ""
    timestamp: str = ""
    description: str = ""
    filetype: str = ""

@attr.s(auto_attribs=True)
class DatasetDescriptors(object):
    descriptors: typing.List[DatasetDescriptor] = attr.Factory(list)
    fieldnames: typing.List[str] = ["filename", "timestamp", "description", "file_type"]

    def add_descriptor(self, desc: DatasetDescriptor):
        self.descriptors.append(desc)

    def dump_to_csv(self, filename: pathlib.Path):
        with open(str(filename), 'w') as f:
            writer = csv.writer(f, fieldnames=self.fieldnames, delimiter=',', quoting = csv.QUOTE_MINIMAL)
            for d in self.descriptors:
                line = [d.filename, d.timestamp, d.description, d.filename]
                writer(writer, line)
