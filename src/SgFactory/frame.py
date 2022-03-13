from typing import List

import PySimpleGUI as sg
from .base import GeneratorBase


class Frame(GeneratorBase):
    TITLE = 'title'
    LAYOUT = 'layout'
    TITLE_COLOR = 'title_color'
    BACKGROUND_COLOR = 'background_color'
    TITLE_LOCATION = 'title_location'
    RELIEF = 'relief'
    SIZE = 'size'
    FONT = 'font'
    PAD = 'pad'
    BORDER_WIDTH = 'border_width'
    KEY = 'key'
    TOOLTIP = 'tooltip'
    RIGHT_CLICK_MENU = 'right_click_menu'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    GRAB = 'grab'
    VISIBLE = 'visible'
    ELEMENT_JUSTIFICATION = 'element_justification'
    VERTICAL_ALIGNMENT = 'vertical_alignment'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.TITLE:                     (False, None),
            self.LAYOUT:                    (False, None),
            self.TITLE_COLOR:               (False, None),
            self.BACKGROUND_COLOR:          (False, None),
            self.TITLE_LOCATION:            (False, None),
            self.RELIEF:                    (False, None),
            self.SIZE:                      (False, None),
            self.FONT:                      (False, None),
            self.PAD:                       (False, None),
            self.BORDER_WIDTH:              (False, None),
            self.KEY:                       (False, None),
            self.TOOLTIP:                   (False, None),
            self.RIGHT_CLICK_MENU:          (False, None),
            self.EXPAND_X:                  (False, None),
            self.EXPAND_Y:                  (False, None),
            self.GRAB:                      (False, None),
            self.VISIBLE:                   (False, None),
            self.ELEMENT_JUSTIFICATION:     (False, None),
            self.VERTICAL_ALIGNMENT:        (False, None),
            self.METADATA:                  (False, None),
        }

    def make(self, key: str, title: str, layout: List[List[sg.Element]], param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.TITLE] = (True, title)
        self.__parameters__[self.LAYOUT] = (True, layout)
        active_params: dict = self.__get_params__(param_key)
        return sg.Frame(**active_params)
