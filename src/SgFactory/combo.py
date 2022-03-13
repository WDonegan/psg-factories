from typing import List, Tuple, Union

import PySimpleGUI as sg
from .base import GeneratorBase


class Combo(GeneratorBase):
    VALUES = 'values'
    DEFAULT_VALUE = 'default_value'
    SIZE = 'size'
    AUTO_SIZE_TEXT = 'auto_size_text'
    BACKGROUND_COLOR = 'background_color'
    TEXT_COLOR = 'text_color'
    BUTTON_BACKGROUND_COLOR = 'button_background_color'
    BUTTON_ARROW_COLOR = 'button_arrow_color'
    BIND_RETURN_KEY = 'bind_return_key'
    CHANGE_SUBMITS = 'change_submits'
    ENABLE_EVENTS = 'enable_events'
    DISABLED = 'disabled'
    KEY = 'key'
    PAD = 'pad'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    TOOLTIP = 'tooltip'
    READONLY = 'readonly'
    FONT = 'font'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.VALUES:                    (False, None),
            self.DEFAULT_VALUE:             (False, None),
            self.SIZE:                      (False, None),
            self.AUTO_SIZE_TEXT:            (False, None),
            self.BACKGROUND_COLOR:          (False, None),
            self.TEXT_COLOR:                (False, None),
            self.BUTTON_BACKGROUND_COLOR:   (False, None),
            self.BUTTON_ARROW_COLOR:        (False, None),
            self.BIND_RETURN_KEY:           (False, None),
            self.CHANGE_SUBMITS:            (False, None),
            self.ENABLE_EVENTS:             (False, None),
            self.DISABLED:                  (False, None),
            self.KEY:                       (False, None),
            self.PAD:                       (False, None),
            self.EXPAND_X:                  (False, None),
            self.EXPAND_Y:                  (False, None),
            self.TOOLTIP:                   (False, None),
            self.READONLY:                  (False, None),
            self.FONT:                      (False, None),
            self.VISIBLE:                   (False, None),
            self.METADATA:                  (False, None),
        }

    def make(self, key: str, values: Union[List[any], Tuple[any]], param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.VALUES] = (True, values)
        active_params: dict = self.__get_params__(param_key)
        return sg.Combo(**active_params)
