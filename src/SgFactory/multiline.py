import PySimpleGUI as sg
from .base import GeneratorBase


class Multiline(GeneratorBase):
    DEFAULT_TEXT = 'default_text'
    ENTER_SUBMITS = 'enter_submits'
    DISABLED = 'disabled'
    AUTOSCROLL = 'autoscroll'
    BORDER_WIDTH = 'border_width'
    SIZE = 'size'
    AUTO_SIZE_TEXT = 'auto_size_text'
    BACKGROUND_COLOR = 'background_color'
    TEXT_COLOR = 'text_color'
    HORIZONTAL_SCROLL = 'horizontal_scroll'
    CHANGE_SUBMITS = 'change_submits'
    ENABLE_EVENTS = 'enable_events'
    DO_NOT_CLEAR = 'do_not_clear'
    KEY = 'key'
    WRITE_ONLY = 'write_only'
    AUTO_REFRESH = 'auto_refresh'
    REROUTE_STDOUT = 'reroute_stdout'
    REROUTE_STDERR = 'reroute_stderr'
    REROUTE_CPRINT = 'reroute_cprint'
    ECHO_STDOUT_STDERR = 'echo_stdout_stderr'
    FOCUS = 'focus'
    FONT = 'font'
    PAD = 'pad'
    TOOLTIP = 'tooltip'
    JUSTIFICATION = 'justification'
    NO_SCROLLBAR = 'no_scrollbar'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    RSTRIP = 'rstrip'
    RIGHT_CLICK_MENU = 'right_click_menu'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.DEFAULT_TEXT:          (False, None),
            self.ENTER_SUBMITS:         (False, None),
            self.DISABLED:              (False, None),
            self.AUTOSCROLL:            (False, None),
            self.BORDER_WIDTH:          (False, None),
            self.SIZE:                  (False, None),
            self.AUTO_SIZE_TEXT:        (False, None),
            self.BACKGROUND_COLOR:      (False, None),
            self.TEXT_COLOR:            (False, None),
            self.HORIZONTAL_SCROLL:     (False, None),
            self.CHANGE_SUBMITS:        (False, None),
            self.ENABLE_EVENTS:         (False, None),
            self.DO_NOT_CLEAR:          (False, None),
            self.KEY:                   (False, None),
            self.WRITE_ONLY:            (False, None),
            self.AUTO_REFRESH:          (False, None),
            self.REROUTE_STDOUT:        (False, None),
            self.REROUTE_STDERR:        (False, None),
            self.REROUTE_CPRINT:        (False, None),
            self.ECHO_STDOUT_STDERR:    (False, None),
            self.FOCUS:                 (False, None),
            self.FONT:                  (False, None),
            self.PAD:                   (False, None),
            self.TOOLTIP:               (False, None),
            self.JUSTIFICATION:         (False, None),
            self.NO_SCROLLBAR:          (False, None),
            self.EXPAND_X:              (False, None),
            self.EXPAND_Y:              (False, None),
            self.RSTRIP:                (False, None),
            self.RIGHT_CLICK_MENU:      (False, None),
            self.VISIBLE:               (False, None),
            self.METADATA:              (False, None),
        }

    def make(self, key: str, param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        active_params: dict = self.__get_params__(param_key)
        return sg.Multiline(**active_params)
