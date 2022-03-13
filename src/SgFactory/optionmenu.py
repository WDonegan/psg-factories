from typing import List, Tuple, Union

import PySimpleGUI as sg
from .base import GeneratorBase


class OptionMenu(GeneratorBase):
    VALUES = 'values'
    DEFAULT_VALUE = 'default_value'
    SIZE = 'size'
    DISABLED = 'disabled'
    AUTO_SIZE_TEXT = 'auto_size_text'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    BACKGROUND_COLOR = 'background_color'
    TEXT_COLOR = 'text_color'
    KEY = 'key'
    PAD = 'pad'
    TOOLTIP = 'tooltip'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.VALUES:            (False, None),
            self.DEFAULT_VALUE:     (False, None),
            self.SIZE:              (False, None),
            self.DISABLED:          (False, None),
            self.AUTO_SIZE_TEXT:    (False, None),
            self.EXPAND_X:          (False, None),
            self.EXPAND_Y:          (False, None),
            self.BACKGROUND_COLOR:  (False, None),
            self.TEXT_COLOR:        (False, None),
            self.KEY:               (False, None),
            self.PAD:               (False, None),
            self.TOOLTIP:           (False, None),
            self.VISIBLE:           (False, None),
            self.METADATA:          (False, None),
        }

    def make(self, key: str, values: Union[List[any], Tuple[any]], param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.VALUES] = (True, values)
        active_params: dict = self.__get_params__(param_key)
        return sg.OptionMenu(**active_params)
