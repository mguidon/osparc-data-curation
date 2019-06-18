import csv
import json
import pathlib
import typing

import attr


def _write_csv(writer, key, value):
    if isinstance(value, list):
        writer.writerow([key] + value)
    else:
        writer.writerow([key, value])

@attr.s(auto_attribs=True)
class DatasetDescriptor(object):
    name: str = ""
    description: str = ""
    keywords: typing.List[str] = attr.Factory(list)
    contributors: typing.List[str] = attr.Factory(list)
    contributor_orcid_ids: typing.List[str] = attr.Factory(list)
    contributor_affiliations: typing.List[str] = attr.Factory(list)
    contributor_roles: typing.List[str] = attr.Factory(list)
    contributor_is_contact_persons: typing.List[bool] = attr.Factory(bool)
    acknowledgement: str = ""
    fundings: typing.List[str] = attr.Factory(list)
    originating_article_dois: typing.List[str] = attr.Factory(list)
    protocol_url_or_dois: typing.List[str] = attr.Factory(list)
    additional_links: typing.List[str] = attr.Factory(list)
    link_descriptions: typing.List[str] = attr.Factory(list)
    example_image_filename: str = ""
    example_image_locator: str = ""
    example_image_description: str = ""
    completeness: str =" "
    prior_batch_number: int = -1
    title_for_complete_dataset : str =""
    
    def from_study_file(self, study_file: pathlib.Path):
        with open(str(study_file)) as json_file:
            data = json.load(json_file)
            for attr in self.__dict__.keys():
                if attr in data.keys():
                    setattr(self, attr, data[attr])

    def dump_to_csv(self, filename: pathlib.Path):
        with open(str(filename), 'w') as f:
            writer = csv.writer(f, delimiter=',', quoting = csv.QUOTE_MINIMAL)
            _write_csv(writer, "Name", self.name)
            _write_csv(writer, "Description", self.description)
            _write_csv(writer, "Keywords", self.keywords)
            _write_csv(writer, "Contributors", self.contributors)
            _write_csv(writer, "Contributor ORCID ID", self.contributor_orcid_ids)
            _write_csv(writer, "Contributor Affiliation", self.contributor_affiliations)
            _write_csv(writer, "Contributor Role", self.contributor_roles)
            _write_csv(writer, "Is Contact Person", self.contributor_is_contact_persons)
            _write_csv(writer, "Acknowledgements", self.acknowledgement)
            _write_csv(writer, "Funding", self.fundings)
            _write_csv(writer, "Originating Article DOI", self.originating_article_dois)
            _write_csv(writer, "Protocol URL or DOI", self.protocol_url_or_dois)
            _write_csv(writer, "Additional Links", self.additional_links)
            _write_csv(writer, "Link Description", self.link_descriptions)
            _write_csv(writer, "Example image filename", self.example_image_filename)
            _write_csv(writer, "Example image locator", self.example_image_locator)
            _write_csv(writer, "Example image description", self.example_image_description)
            _write_csv(writer, "Completeness of dataset", self.completeness)
            _write_csv(writer, "Prior batch number", self.description)
            _write_csv(writer, "Title of the complete data set", self.title_for_complete_dataset)
