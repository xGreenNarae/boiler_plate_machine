class ArgumentRepository:
    _instance = None

    @staticmethod
    def get_instance():
        if ArgumentRepository._instance is None:
            ArgumentRepository()
        return ArgumentRepository._instance

    def __init__(self):
        if ArgumentRepository._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ArgumentRepository._instance = self
            self.data = {}
