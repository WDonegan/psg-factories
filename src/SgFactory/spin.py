from typing import List, Tuple, Union

import PySimpleGUI as sg
from .base import GeneratorBase


class Spin(GeneratorBase):
    VALUES = 'values'
    INITIAL_VALUE = 'initial_value'
    DISABLED = 'disabled'
    CHANGE_SUBMITS = 'change_submits'
    ENABLE_EVENTS = 'enable_events'
    READONLY = 'readonly'
    SIZE = 'size'
    AUTO_SIZE_TEXT = 'auto_size_text'
    FONT = 'font'
    BACKGROUND_COLOR = 'background_color'
    TEXT_COLOR = 'text_color'
    KEY = 'key'
    PAD = 'pad'
    TOOLTIP = 'tooltip'
    RIGHT_CLICK_MENU = 'right_click_menu'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.VALUES:            (False, None),
            self.INITIAL_VALUE:     (False, None),
            self.DISABLED:          (False, None),
            self.CHANGE_SUBMITS:    (False, None),
            self.ENABLE_EVENTS:     (False, None),
            self.READONLY:          (False, None),
            self.SIZE:              (False, None),
            self.AUTO_SIZE_TEXT:    (False, None),
            self.FONT:              (False, None),
            self.BACKGROUND_COLOR:  (False, None),
            self.TEXT_COLOR:        (False, None),
            self.KEY:               (False, None),
            self.PAD:               (False, None),
            self.TOOLTIP:           (False, None),
            self.RIGHT_CLICK_MENU:  (False, None),
            self.EXPAND_X:          (False, None),
            self.EXPAND_Y:          (False, None),
            self.VISIBLE:           (False, None),
            self.METADATA:          (False, None),
        }

    def make(self, key: str, values: Union[List[any], Tuple[any]], param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.VALUES] = (True, values)
        active_params: dict = self.__get_params__(param_key)
        return sg.Spin(**active_params)
