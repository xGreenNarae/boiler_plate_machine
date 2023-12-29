import yaml

from template_parser import TemplateParser


class StructureParser:
    def __init__(self, structure_config: str):
        self.structure_config = structure_config

    def parse(self) -> list:
        formatted_structure_config = TemplateParser.format(self.structure_config)

        return yaml.safe_load(formatted_structure_config)
