import PySimpleGUI as sg
from .base import GeneratorBase


class Text(GeneratorBase):
    TEXT = 'text'
    SIZE = 'size'
    AUTO_SIZE_TEXT = 'auto_size_text'
    CLICK_SUBMITS = 'click_submits'
    ENABLE_EVENTS = 'enable_events'
    RELIEF = 'relief'
    FONT = 'font'
    TEXT_COLOR = 'text_color'
    BACKGROUND_COLOR = 'background_color'
    BORDER_WIDTH = 'border_width'
    JUSTIFICATION = 'justification'
    PAD = 'pad'
    KEY = 'key'
    RIGHT_CLICK_MENU = 'right_click_menu'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    GRAB = 'grab'
    TOOLTIP = 'tooltip'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    RELIEF_FLAT = sg.RELIEF_FLAT
    RELIEF_SOLID = sg.RELIEF_SOLID
    RELIEF_RIDGE = sg.RELIEF_RIDGE
    RELIEF_GROOVE = sg.RELIEF_GROOVE
    RELIEF_RAISED = sg.RELIEF_RAISED
    RELIEF_SUNKEN = sg.RELIEF_SUNKEN

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
            self.BORDER_WIDTH:      (False, None),
            self.JUSTIFICATION:     (False, None),
            self.PAD:               (False, None),
            self.KEY:               (False, None),
            self.RIGHT_CLICK_MENU:  (False, None),
            self.EXPAND_X:          (False, None),
            self.EXPAND_Y:          (False, None),
            self.GRAB:              (False, None),
            self.TOOLTIP:           (False, None),
            self.VISIBLE:           (False, None),
            self.METADATA:          (False, None),
        }

    def make(self, key: str, text: str = '', param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.TEXT] = (True, text)
        active_params: dict = self.__get_params__(param_key)
        return sg.Text(**active_params)
