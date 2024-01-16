from pathlib import Path

import questionary
from rich import print

import typer

from boilerplatemachine.configuration_file_reader import ConfigurationFileReader
from boilerplatemachine.structure_builder import StructureBuilder
from boilerplatemachine.structure_parser import StructureParser

app = typer.Typer()


@app.command()
def main(structure_config_file: str, working_directory: Path):
    """
    :param structure_config_file:
    :param working_directory: path to create boilerplate directories and files.
    """

    structure_config: str = ConfigurationFileReader.read_structure_config_file(structure_config_file)

    structure: list = StructureParser(structure_config).parse()

    StructureBuilder(structure, working_directory).build()


@app.command()
def show():
    config_files = ConfigurationFileReader.get_config_files()

    file_type = questionary.select(
        "Select a config file type",
        choices=["structure", "template"]
    ).ask()

    match file_type:
        case "structure":
            file_name = questionary.select(
                "Select a structure config file",
                choices=config_files["structure_files"]
            ).ask()
        case "template":
            file_name = questionary.select(
                "Select a template file",
                choices=config_files["template_files"]
            ).ask()
        case _:
            raise ValueError(f"Invalid file type: {file_type}")

    file_content = ConfigurationFileReader.read_file_content(file_type, file_name)

    print(file_content)


if __name__ == "__main__":
    app()
