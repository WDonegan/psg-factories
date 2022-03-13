from typing import List, Tuple

import PySimpleGUI as sg
from .base import GeneratorBase


class MenubarCustom(GeneratorBase):
    MENU_DEFINITION = 'menu_definition'
    DISABLED_TEXT_COLOR = 'disabled_text_color'
    BAR_FONT = 'bar_font'
    FONT = 'font'
    TEAROFF = 'tearoff'
    PAD = 'pad'
    BACKGROUND_COLOR = 'background_color'
    TEXT_COLOR = 'text_color'
    BAR_BACKGROUND_COLOR = 'bar_background_color'
    BAR_TEXT_COLOR = 'bar_text_color'
    KEY = 'key'

    def reset_params(self):
        self.__parameters__ = {
            self.MENU_DEFINITION:       (False, None),
            self.DISABLED_TEXT_COLOR:   (False, None),
            self.BAR_FONT:              (False, None),
            self.FONT:                  (False, None),
            self.TEAROFF:               (False, None),
            self.PAD:                   (False, None),
            self.BACKGROUND_COLOR:      (False, None),
            self.TEXT_COLOR:            (False, None),
            self.BAR_BACKGROUND_COLOR:  (False, None),
            self.BAR_TEXT_COLOR:        (False, None),
            self.KEY:                   (False, None),
        }

    def make(self, key: str, menu_def: List[List[Tuple[str, List[str]]]], param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.MENU_DEFINITION] = (True, menu_def)
        active_params: dict = self.__get_params__(param_key)
        return sg.MenubarCustom(**active_params)
