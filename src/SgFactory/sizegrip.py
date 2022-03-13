import PySimpleGUI as sg
from .base import GeneratorBase


class Sizegrip(GeneratorBase):
    BACKGROUND_COLOR = 'background_color'
    PAD = 'pad'
    KEY = 'key'

    def reset_params(self):
        self.__parameters__ = {
            self.BACKGROUND_COLOR:  (False, None),
            self.PAD:               (False, None),
            self.KEY:               (False, None),
        }

    def make(self, key: str, param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        active_params: dict = self.__get_params__(param_key)
        return sg.Sizegrip(**active_params)
