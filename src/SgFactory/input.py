import PySimpleGUI as sg
from .base import GeneratorBase


class Input(GeneratorBase):
    DEFAULT_TEXT = 'default_text'
    SIZE = 'size'
    DISABLED = 'disabled'
    PASSWORD_CHAR = 'password_char'
    JUSTIFICATION = 'justification'
    BACKGROUND_COLOR = 'background_color'
    TEXT_COLOR = 'text_color'
    FONT = 'font'
    TOOLTIP = 'tooltip'
    BORDER_WIDTH = 'border_width'
    CHANGE_SUBMITS = 'change_submits'
    ENABLE_EVENTS = 'enable_events'
    DO_NOT_CLEAR = 'do_not_clear'
    KEY = 'key'
    FOCUS = 'focus'
    PAD = 'pad'
    USE_READONLY_FOR_DISABLE = 'use_readonly_for_disable'
    READONLY = 'readonly'
    DISABLED_READONLY_BACKGROUND_COLOR = 'disabled_readonly_background_color'
    DISABLED_READONLY_TEXT_COLOR = 'disabled_readonly_text_color'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    RIGHT_CLICK_MENU = 'right_click_menu'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.DEFAULT_TEXT:                          (False, None),
            self.SIZE:                                  (False, None),
            self.DISABLED:                              (False, None),
            self.PASSWORD_CHAR:                         (False, None),
            self.JUSTIFICATION:                         (False, None),
            self.BACKGROUND_COLOR:                      (False, None),
            self.TEXT_COLOR:                            (False, None),
            self.FONT:                                  (False, None),
            self.TOOLTIP:                               (False, None),
            self.BORDER_WIDTH:                          (False, None),
            self.CHANGE_SUBMITS:                        (False, None),
            self.ENABLE_EVENTS:                         (False, None),
            self.DO_NOT_CLEAR:                          (False, None),
            self.KEY:                                   (False, None),
            self.FOCUS:                                 (False, None),
            self.PAD:                                   (False, None),
            self.USE_READONLY_FOR_DISABLE:              (False, None),
            self.READONLY:                              (False, None),
            self.DISABLED_READONLY_BACKGROUND_COLOR:    (False, None),
            self.DISABLED_READONLY_TEXT_COLOR:          (False, None),
            self.EXPAND_X:                              (False, None),
            self.EXPAND_Y:                              (False, None),
            self.RIGHT_CLICK_MENU:                      (False, None),
            self.VISIBLE:                               (False, None),
            self.METADATA:                              (False, None),
        }

    def make(self, key: str, param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        active_params: dict = self.__get_params__(param_key)
        return sg.Input(**active_params)
