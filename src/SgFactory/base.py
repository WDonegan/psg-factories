class GeneratorBase:
    __parameters__: dict
    __saved__: dict

    def __init__(self):
        self.reset_params()
        self.reset_saved()

    def reset_params(self):
        pass

    def reset_saved(self):
        self.__saved__ = {'default': self.__parameters__.copy()}

    def save(self, param_key: str):
        self.__saved__.update({param_key.lower(): self.__parameters__.copy()})

    def load(self, param_key: str):
        if self.__saved__.keys().__contains__(param_key):
            self.__parameters__ = self.__saved__[param_key]

    def set(self, param: str, value: any):
        if value is None:
            self.__parameters__[param] = False, None
        else:
            self.__parameters__[param] = True, value

    def __get_params__(self, param_key: str = None):
        source_params: dict = {}
        if param_key is None:
            source_params = self.__parameters__
        elif self.__saved__.keys().__contains__(param_key):
            source_params = self.__saved__[param_key]

        active_params: dict = {}
        for k, v in source_params.items():
            if v[0]:
                active_params.update({k: v[1]})
        return active_params
