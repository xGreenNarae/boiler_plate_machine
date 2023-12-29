import typer
from jinja2 import Environment, meta

from argument_repository import ArgumentRepository


class TemplateParser:

    @staticmethod
    def extract_variables(env, raw_string: str):
        """
        extract variables from raw string
        """

        parsed_content = env.parse(raw_string)

        undeclared_variables = meta.find_undeclared_variables(parsed_content)

        return set(undeclared_variables)

    @staticmethod
    def format(template: str):
        """
        replace variables in template with stored arguments
        if there is no argument in repository, ask user to input to format interactively(typer) and store it.
        """
        env = Environment()

        # validate argument repository is enough to format template's all variables
        variables = TemplateParser.extract_variables(env, template)
        args_map = ArgumentRepository.get_instance().data

        for var in variables:
            if var not in args_map:
                user_input = typer.prompt(f"Enter value for {var}")
                args_map[var] = user_input

        template = env.from_string(template)

        return template.render(args_map)

