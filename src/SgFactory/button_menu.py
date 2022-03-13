from typing import List

import PySimpleGUI as sg
from .base import GeneratorBase


class ButtonMenu(GeneratorBase):
    BUTTON_TEXT = 'button_text'
    MENU_DEF = 'menu_def'
    TOOLTIP = 'tooltip'
    DISABLED = 'disabled'
    IMAGE_SOURCE = 'image_source'
    IMAGE_FILENAME = 'image_filename'
    IMAGE_DATA = 'image_data'
    IMAGE_SIZE = 'image_size'
    IMAGE_SUBSAMPLE = 'image_subsample'
    BORDER_WIDTH = 'border_width'
    SIZE = 'size'
    AUTO_SIZE_BUTTON = 'auto_size_button'
    BUTTON_COLOR = 'button_color'
    TEXT_COLOR = 'text_color'
    BACKGROUND_COLOR = 'background_color'
    DISABLED_TEXT_COLOR = 'disabled_text_color'
    FONT = 'font'
    ITEM_FONT = 'item_font'
    PAD = 'pad'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    KEY = 'key'
    TEAROFF = 'tearoff'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.BUTTON_TEXT:           (False, None),
            self.MENU_DEF:              (False, None),
            self.TOOLTIP:               (False, None),
            self.DISABLED:              (False, None),
            self.IMAGE_SOURCE:          (False, None),
            self.IMAGE_FILENAME:        (False, None),
            self.IMAGE_DATA:            (False, None),
            self.IMAGE_SIZE:            (False, None),
            self.IMAGE_SUBSAMPLE:       (False, None),
            self.BORDER_WIDTH:          (False, None),
            self.SIZE:                  (False, None),
            self.AUTO_SIZE_BUTTON:      (False, None),
            self.BUTTON_COLOR:          (False, None),
            self.TEXT_COLOR:            (False, None),
            self.BACKGROUND_COLOR:      (False, None),
            self.DISABLED_TEXT_COLOR:   (False, None),
            self.FONT:                  (False, None),
            self.ITEM_FONT:             (False, None),
            self.PAD:                   (False, None),
            self.EXPAND_X:              (False, None),
            self.EXPAND_Y:              (False, None),
            self.KEY:                   (False, None),
            self.TEAROFF:               (False, None),
            self.VISIBLE:               (False, None),
            self.METADATA:              (False, None),
        }

    def make(self, key: str, txt: str, menu: List[List[str]], param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.BUTTON_TEXT] = (True, txt)
        self.__parameters__[self.MENU_DEF] = (True, menu)
        active_params: dict = self.__get_params__(param_key)
        return sg.ButtonMenu(**active_params)
