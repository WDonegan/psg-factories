import PySimpleGUI as sg
from .base import GeneratorBase


class StatusBar(GeneratorBase):
    TEXT = 'text'
    SIZE = 'size'
    AUTO_SIZE_TEXT = 'auto_size_text'
    CLICK_SUBMITS = 'click_submits'
    ENABLE_EVENTS = 'enable_events'
    RELIEF = 'relief'
    FONT = 'font'
    TEXT_COLOR = 'text_color'
    BACKGROUND_COLOR = 'background_color'
    JUSTIFICATION = 'justification'
    PAD = 'pad'
    KEY = 'key'
    RIGHT_CLICK_MENU = 'right_click_menu'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    TOOLTIP = 'tooltip'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.TEXT:              (False, None),
            self.SIZE:              (False, None),
            self.AUTO_SIZE_TEXT:    (False, None),
            self.CLICK_SUBMITS:     (False, None),
            self.ENABLE_EVENTS:     (False, None),
            self.RELIEF:            (False, None),
            self.FONT:              (False, None),
            self.TEXT_COLOR:        (False, None),
            self.BACKGROUND_COLOR:  (False, None),
            self.JUSTIFICATION:     (False, None),
            self.PAD:               (False, None),
            self.KEY:               (False, None),
            self.RIGHT_CLICK_MENU:  (False, None),
            self.EXPAND_X:          (False, None),
            self.EXPAND_Y:          (False, None),
            self.TOOLTIP:           (False, None),
            self.VISIBLE:           (False, None),
            self.METADATA:          (False, None),
        }

    def make(self, key: str, txt: str, param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.TEXT] = (True, txt)
        active_params: dict = self.__get_params__(param_key)
        return sg.StatusBar(**active_params)
