from pathlib import Path


class ConfigurationFileReader:
    home_config_path = Path.home() / ".config" / "bpm"
    structure_config_file_path = home_config_path / "structures"  # TODO: dynamically set config file path
    template_file_path = home_config_path / "templates"

    @staticmethod
    def read_structure_config_file(file_path: str):
        structure_config_file = ConfigurationFileReader.structure_config_file_path / f"{file_path}.yaml"

        if not structure_config_file.exists():
            raise FileNotFoundError(f"File {structure_config_file} does not exist.")

        return structure_config_file.read_text()

    @staticmethod
    def read_template_file(file_path: str):
        template_file = ConfigurationFileReader.template_file_path / f"{file_path}"

        if not template_file.exists():
            raise FileNotFoundError(f"File {template_file} does not exist.")

        return template_file.read_text()

    @staticmethod
    def get_config_files():
        structure_files = ConfigurationFileReader.structure_config_file_path.glob("*")
        template_files = ConfigurationFileReader.template_file_path.glob("*")

        return {
            "structure_files": [file.name for file in structure_files],
            "template_files": [file.name for file in template_files]
        }

    @staticmethod
    def read_file_content(file_type: str, file_name: str):
        match file_type:
            case "structure":
                return ConfigurationFileReader.read_structure_config_file(
                    ConfigurationFileReader.cut_extension(file_name))
            case "template":
                return ConfigurationFileReader.read_template_file(file_name)
            case _:
                raise ValueError(f"Invalid file type: {file_type}")

    # remove after last dot (including dot)
    @staticmethod
    def cut_extension(file_name: str):
        return file_name[:file_name.rfind(".")]
