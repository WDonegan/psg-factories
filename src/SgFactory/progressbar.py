import PySimpleGUI as sg
from .base import GeneratorBase


class ProgressBar(GeneratorBase):
    MAX_VALUE = 'max_value'
    ORIENTATION = 'orientation'
    SIZE = 'size'
    SIZE_PX = 'size_px'
    AUTO_SIZE_TEXT = 'auto_size_text'
    BAR_COLOR = 'bar_color'
    STYLE = 'style'
    BORDER_WIDTH = 'border_width'
    RELIEF = 'relief'
    KEY = 'key'
    PAD = 'pad'
    RIGHT_CLICK_MENU = 'right_click_menu'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.MAX_VALUE:         (False, None),
            self.ORIENTATION:       (False, None),
            self.SIZE:              (False, None),
            self.SIZE_PX:           (False, None),
            self.AUTO_SIZE_TEXT:    (False, None),
            self.BAR_COLOR:         (False, None),
            self.STYLE:             (False, None),
            self.BORDER_WIDTH:      (False, None),
            self.RELIEF:            (False, None),
            self.KEY:               (False, None),
            self.PAD:               (False, None),
            self.RIGHT_CLICK_MENU:  (False, None),
            self.EXPAND_X:          (False, None),
            self.EXPAND_Y:          (False, None),
            self.VISIBLE:           (False, None),
            self.METADATA:          (False, None),
        }

    def make(self, key: str, max_val: int, param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.MAX_VALUE] = (True, max_val)
        active_params: dict = self.__get_params__(param_key)
        return sg.ProgressBar(**active_params)
