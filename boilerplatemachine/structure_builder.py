from pathlib import Path

from configuration_file_reader import ConfigurationFileReader
from template_parser import TemplateParser


class StructureBuilder:
    def __init__(self, structure: list, working_directory: Path):
        self.structure = structure
        self.working_directory = working_directory

    def build(self):
        self.create_structure_recursively(self.structure, self.working_directory)

    def create_structure_recursively(self, items: list, current_path: Path):
        """
        :param items: item list in structure.yaml with same depth level
        :param current_path: current depth level path
        """
        # data should be list or None
        if not isinstance(items, list):
            if items is None:
                return
            raise Exception(f"data should be list, but {items} is not list.")

        for item in items:
            # item should be dict
            if not isinstance(item, dict):
                raise Exception(f"item should be dict, but {item} is not dict.")

            for parent, child in item.items():
                if parent.endswith("/"):  # directory
                    # create directory
                    new_path = current_path / parent
                    new_path.mkdir(exist_ok=True)

                    # step into child tree
                    self.create_structure_recursively(child, new_path)
                else:  # file
                    self.create_file_with_template(current_path / parent, child)

    @staticmethod
    def create_file_with_template(file_path: Path, template_file: str):
        template = ConfigurationFileReader.read_template_file(template_file)

        rendered_content = TemplateParser.format(template)

        file_path.write_text(rendered_content)
