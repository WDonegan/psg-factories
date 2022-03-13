import PySimpleGUI as sg
from .base import GeneratorBase


class Separator(GeneratorBase):
    COLOR = 'color'
    PAD = 'pad'
    KEY = 'key'

    def reset_params(self):
        self.__parameters__ = {
            self.COLOR:     (False, None),
            self.PAD:       (False, None),
            self.KEY:       (False, None),
        }

    def make(self, key: str, vert: bool = False, param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        active_params: dict = self.__get_params__(param_key)
        if vert:
            return sg.VSep(**active_params)
        return sg.HSep(**active_params)
