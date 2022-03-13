import PySimpleGUI as sg
from .base import GeneratorBase


class Canvas(GeneratorBase):
    CANVAS = 'canvas'
    BACKGROUND_COLOR = 'background_color'
    SIZE = 'size'
    PAD = 'pad'
    KEY = 'key'
    TOOLTIP = 'tooltip'
    RIGHT_CLICK_MENU = 'right_click_menu'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    VISIBLE = 'visible'
    BORDER_WIDTH = 'border_width'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.CANVAS:                (False, None),
            self.BACKGROUND_COLOR:      (False, None),
            self.SIZE:                  (False, None),
            self.PAD:                   (False, None),
            self.KEY:                   (False, None),
            self.TOOLTIP:               (False, None),
            self.RIGHT_CLICK_MENU:      (False, None),
            self.EXPAND_X:              (False, None),
            self.EXPAND_Y:              (False, None),
            self.VISIBLE:               (False, None),
            self.BORDER_WIDTH:          (False, None),
            self.METADATA:              (False, None),
        }

    def make(self, key: str, param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        active_params: dict = self.__get_params__(param_key)
        return sg.Canvas(**active_params)
