from typing import List

import PySimpleGUI as sg
from .base import GeneratorBase


class Column(GeneratorBase):
    LAYOUT = 'layout'
    BACKGROUND_COLOR = 'background_color'
    SIZE = 'size'
    PAD = 'pad'
    SCROLLABLE = 'scrollable'
    VERTICAL_SCROLL_ONLY = 'vertical_scroll_only'
    RIGHT_CLICK_MENU = 'right_click_menu'
    KEY = 'key'
    VISIBLE = 'visible'
    JUSTIFICATION = 'justification'
    ELEMENT_JUSTIFICATION = 'element_justification'
    VERTICAL_ALIGNMENT = 'vertical_alignment'
    GRAB = 'grab'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.LAYOUT:                  (False, None),
            self.BACKGROUND_COLOR:        (False, None),
            self.SIZE:                    (False, None),
            self.PAD:                     (False, None),
            self.SCROLLABLE:              (False, None),
            self.VERTICAL_SCROLL_ONLY:    (False, None),
            self.RIGHT_CLICK_MENU:        (False, None),
            self.KEY:                     (False, None),
            self.VISIBLE:                 (False, None),
            self.JUSTIFICATION:           (False, None),
            self.ELEMENT_JUSTIFICATION:   (False, None),
            self.VERTICAL_ALIGNMENT:      (False, None),
            self.GRAB:                    (False, None),
            self.EXPAND_X:                (False, None),
            self.EXPAND_Y:                (False, None),
            self.METADATA:                (False, None),
        }

    def make(self, key: str, layout: List[List[sg.Element]], param_key: str = None) -> sg.Column:
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.LAYOUT] = (True, layout)
        active_params: dict = self.__get_params__(param_key)
        return sg.Column(**active_params)
