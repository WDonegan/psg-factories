import PySimpleGUI as sg
from .base import GeneratorBase


class Radio(GeneratorBase):
    TEXT = 'text'
    GROUP_ID = 'group_id'
    DEFAULT = 'default'
    DISABLED = 'disabled'
    SIZE = 'size'
    AUTO_SIZE_TEXT = 'auto_size_text'
    BACKGROUND_COLOR = 'background_color'
    TEXT_COLOR = 'text_color'
    CIRCLE_COLOR = 'circle_color'
    FONT = 'font'
    KEY = 'key'
    PAD = 'pad'
    TOOLTIP = 'tooltip'
    CHANGE_SUBMITS = 'change_submits'
    ENABLE_EVENTS = 'enable_events'
    RIGHT_CLICK_MENU = 'right_click_menu'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.TEXT:              (False, None),
            self.GROUP_ID:          (False, None),
            self.DEFAULT:           (False, None),
            self.DISABLED:          (False, None),
            self.SIZE:              (False, None),
            self.AUTO_SIZE_TEXT:    (False, None),
            self.BACKGROUND_COLOR:  (False, None),
            self.TEXT_COLOR:        (False, None),
            self.CIRCLE_COLOR:      (False, None),
            self.FONT:              (False, None),
            self.KEY:               (False, None),
            self.PAD:               (False, None),
            self.TOOLTIP:           (False, None),
            self.CHANGE_SUBMITS:    (False, None),
            self.ENABLE_EVENTS:     (False, None),
            self.RIGHT_CLICK_MENU:  (False, None),
            self.EXPAND_X:          (False, None),
            self.EXPAND_Y:          (False, None),
            self.VISIBLE:           (False, None),
            self.METADATA:          (False, None),
        }

    def make(self, key: str, txt: str, group: any, param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.TEXT] = (True, txt)
        self.__parameters__[self.GROUP_ID] = (True, group)
        active_params: dict = self.__get_params__(param_key)
        return sg.Radio(**active_params)
