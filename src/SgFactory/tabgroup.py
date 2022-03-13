from typing import List

import PySimpleGUI as sg
from .base import GeneratorBase


class TabGroup(GeneratorBase):
    LAYOUT = 'layout'
    TAB_LOCATION = 'tab_location'
    TITLE_COLOR = 'title_color'
    TAB_BACKGROUND_COLOR = 'tab_background_color'
    SELECTED_TITLE_COLOR = 'selected_title_color'
    SELECTED_BACKGROUND_COLOR = 'selected_background_color'
    BACKGROUND_COLOR = 'background_color'
    FOCUS_COLOR = 'focus_color'
    FONT = 'font'
    CHANGE_SUBMITS = 'change_submits'
    ENABLE_EVENTS = 'enable_events'
    PAD = 'pad'
    BORDER_WIDTH = 'border_width'
    TAB_BORDER_WIDTH = 'tab_border_width'
    THEME = 'theme'
    KEY = 'key'
    SIZE = 'size'
    TOOLTIP = 'tooltip'
    RIGHT_CLICK_MENU = 'right_click_menu'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.LAYOUT:                        (False, None),
            self.TAB_LOCATION:                  (False, None),
            self.TITLE_COLOR:                   (False, None),
            self.TAB_BACKGROUND_COLOR:          (False, None),
            self.SELECTED_TITLE_COLOR:          (False, None),
            self.SELECTED_BACKGROUND_COLOR:     (False, None),
            self.BACKGROUND_COLOR:              (False, None),
            self.FOCUS_COLOR:                   (False, None),
            self.FONT:                          (False, None),
            self.CHANGE_SUBMITS:                (False, None),
            self.ENABLE_EVENTS:                 (False, None),
            self.PAD:                           (False, None),
            self.BORDER_WIDTH:                  (False, None),
            self.TAB_BORDER_WIDTH:              (False, None),
            self.THEME:                         (False, None),
            self.KEY:                           (False, None),
            self.SIZE:                          (False, None),
            self.TOOLTIP:                       (False, None),
            self.RIGHT_CLICK_MENU:              (False, None),
            self.EXPAND_X:                      (False, None),
            self.EXPAND_Y:                      (False, None),
            self.VISIBLE:                       (False, None),
            self.METADATA:                      (False, None),
        }

    def make(self, key: str, layout: List[List[sg.Tab]], param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.LAYOUT] = (True, layout)
        active_params: dict = self.__get_params__(param_key)
        return sg.TabGroup(**active_params)
