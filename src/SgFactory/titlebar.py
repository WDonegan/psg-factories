import PySimpleGUI as sg
from .base import GeneratorBase


class Titlebar(GeneratorBase):
    TITLE = 'title'
    ICON = 'icon'
    TEXT_COLOR = 'text_color'
    BACKGROUND_COLOR = 'background_color'
    FONT = 'font'
    KEY = 'key'

    def reset_params(self):
        self.__parameters__ = {
            self.TITLE:             (False, None),
            self.ICON:              (False, None),
            self.TEXT_COLOR:        (False, None),
            self.BACKGROUND_COLOR:  (False, None),
            self.FONT:              (False, None),
            self.KEY:               (False, None),
        }

    def make(self, key: str, param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        active_params: dict = self.__get_params__(param_key)
        return sg.Titlebar(**active_params)
