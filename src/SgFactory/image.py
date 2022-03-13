import PySimpleGUI as sg
from .base import GeneratorBase


class Image(GeneratorBase):
    SOURCE = 'source'
    FILENAME = 'filename'
    DATA = 'data'
    BACKGROUND_COLOR = 'background_color'
    SIZE = 'size'
    PAD = 'pad'
    KEY = 'key'
    TOOLTIP = 'tooltip'
    SUBSAMPLE = 'subsample'
    RIGHT_CLICK_MENU = 'right_click_menu'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    VISIBLE = 'visible'
    ENABLE_EVENTS = 'enable_events'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.SOURCE:            (False, None),
            self.FILENAME:          (False, None),
            self.DATA:              (False, None),
            self.BACKGROUND_COLOR:  (False, None),
            self.SIZE:              (False, None),
            self.PAD:               (False, None),
            self.KEY:               (False, None),
            self.TOOLTIP:           (False, None),
            self.SUBSAMPLE:         (False, None),
            self.RIGHT_CLICK_MENU:  (False, None),
            self.EXPAND_X:          (False, None),
            self.EXPAND_Y:          (False, None),
            self.VISIBLE:           (False, None),
            self.ENABLE_EVENTS:     (False, None),
            self.METADATA:          (False, None),
        }

    def make(self, key: str, param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        active_params: dict = self.__get_params__(param_key)
        return sg.Image(**active_params)
