from typing import List, Tuple

import PySimpleGUI as sg
from .base import GeneratorBase


class Menu(GeneratorBase):
    MENU_DEFINITION = 'menu_definition'
    BACKGROUND_COLOR = 'background_color'
    TEXT_COLOR = 'text_color'
    DISABLED_TEXT_COLOR = 'disabled_text_color'
    SIZE = 'size'
    TEAROFF = 'tearoff'
    FONT = 'font'
    PAD = 'pad'
    KEY = 'key'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.MENU_DEFINITION:       (False, None),
            self.BACKGROUND_COLOR:      (False, None),
            self.TEXT_COLOR:            (False, None),
            self.DISABLED_TEXT_COLOR:   (False, None),
            self.SIZE:                  (False, None),
            self.TEAROFF:               (False, None),
            self.FONT:                  (False, None),
            self.PAD:                   (False, None),
            self.KEY:                   (False, None),
            self.VISIBLE:               (False, None),
            self.METADATA:              (False, None),
        }

    def make(self, key: str, menu_def: List[List[Tuple[str, List[str]]]], param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.MENU_DEFINITION] = (True, menu_def)
        active_params: dict = self.__get_params__(param_key)
        return sg.Menu(**active_params)
