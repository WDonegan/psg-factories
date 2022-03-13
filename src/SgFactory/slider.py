import PySimpleGUI as sg
from .base import GeneratorBase


class Slider(GeneratorBase):
    RANGE = 'range'
    DEFAULT_VALUE = 'default_value'
    RESOLUTION = 'resolution'
    TICK_INTERVAL = 'tick_interval'
    ORIENTATION = 'orientation'
    DISABLE_NUMBER_DISPLAY = 'disable_number_display'
    BORDER_WIDTH = 'border_width'
    RELIEF = 'relief'
    CHANGE_SUBMITS = 'change_submits'
    ENABLE_EVENTS = 'enable_events'
    DISABLED = 'disabled'
    SIZE = 'size'
    FONT = 'font'
    BACKGROUND_COLOR = 'background_color'
    TEXT_COLOR = 'text_color'
    TROUGH_COLOR = 'trough_color'
    KEY = 'key'
    PAD = 'pad'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    TOOLTIP = 'tooltip'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.RANGE:                     (False, None),
            self.DEFAULT_VALUE:             (False, None),
            self.RESOLUTION:                (False, None),
            self.TICK_INTERVAL:             (False, None),
            self.ORIENTATION:               (False, None),
            self.DISABLE_NUMBER_DISPLAY:    (False, None),
            self.BORDER_WIDTH:              (False, None),
            self.RELIEF:                    (False, None),
            self.CHANGE_SUBMITS:            (False, None),
            self.ENABLE_EVENTS:             (False, None),
            self.DISABLED:                  (False, None),
            self.SIZE:                      (False, None),
            self.FONT:                      (False, None),
            self.BACKGROUND_COLOR:          (False, None),
            self.TEXT_COLOR:                (False, None),
            self.TROUGH_COLOR:              (False, None),
            self.KEY:                       (False, None),
            self.PAD:                       (False, None),
            self.EXPAND_X:                  (False, None),
            self.EXPAND_Y:                  (False, None),
            self.TOOLTIP:                   (False, None),
            self.VISIBLE:                   (False, None),
            self.METADATA:                  (False, None),
        }

    def make(self, key: str, param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        active_params: dict = self.__get_params__(param_key)
        return sg.Slider(**active_params)
