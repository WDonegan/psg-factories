from typing import List, Tuple, Union

import PySimpleGUI as sg
from .base import GeneratorBase


class Listbox(GeneratorBase):
    VALUES = 'values'
    DEFAULT_VALUES = 'default_values'
    SELECT_MODE = 'select_mode'
    CHANGE_SUBMITS = 'change_submits'
    ENABLE_EVENTS = 'enable_events'
    BIND_RETURN_KEY = 'bind_return_key'
    SIZE = 'size'
    DISABLED = 'disabled'
    AUTO_SIZE_TEXT = 'auto_size_text'
    FONT = 'font'
    NO_SCROLLBAR = 'no_scrollbar'
    HORIZONTAL_SCROLL = 'horizontal_scroll'
    BACKGROUND_COLOR = 'background_color'
    TEXT_COLOR = 'text_color'
    HIGHLIGHT_BACKGROUND_COLOR = 'highlight_background_color'
    HIGHLIGHT_TEXT_COLOR = 'highlight_text_color'
    KEY = 'key'
    PAD = 'pad'
    TOOLTIP = 'tooltip'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    RIGHT_CLICK_MENU = 'right_click_menu'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.VALUES:                        (False, None),
            self.DEFAULT_VALUES:                (False, None),
            self.SELECT_MODE:                   (False, None),
            self.CHANGE_SUBMITS:                (False, None),
            self.ENABLE_EVENTS:                 (False, None),
            self.BIND_RETURN_KEY:               (False, None),
            self.SIZE:                          (False, None),
            self.DISABLED:                      (False, None),
            self.AUTO_SIZE_TEXT:                (False, None),
            self.FONT:                          (False, None),
            self.NO_SCROLLBAR:                  (False, None),
            self.HORIZONTAL_SCROLL:             (False, None),
            self.BACKGROUND_COLOR:              (False, None),
            self.TEXT_COLOR:                    (False, None),
            self.HIGHLIGHT_BACKGROUND_COLOR:    (False, None),
            self.HIGHLIGHT_TEXT_COLOR:          (False, None),
            self.KEY:                           (False, None),
            self.PAD:                           (False, None),
            self.TOOLTIP:                       (False, None),
            self.EXPAND_X:                      (False, None),
            self.EXPAND_Y:                      (False, None),
            self.RIGHT_CLICK_MENU:              (False, None),
            self.VISIBLE:                       (False, None),
            self.METADATA:                      (False, None),
        }

    def make(self, key: str, values: Union[List[any], Tuple[any]], param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.VALUES] = (True, values)
        active_params: dict = self.__get_params__(param_key)
        return sg.Listbox(**active_params)
