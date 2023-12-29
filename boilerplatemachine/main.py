from pathlib import Path

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


if __name__ == "__main__":
    app()
