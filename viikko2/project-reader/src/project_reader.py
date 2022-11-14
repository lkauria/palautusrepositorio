from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url
        print(self._url)

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)
        parsed_toml = toml.loads(content)
        

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project("Test name", "Test description", [], [])
