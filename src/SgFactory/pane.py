from typing import List, Tuple, Union

import PySimpleGUI as sg
from .base import GeneratorBase


class Pane(GeneratorBase):
    PANE_LIST = 'pane_list'
    BACKGROUND_COLOR = 'background_color'
    SIZE = 'size'
    PAD = 'pad'
    ORIENTATION = 'orientation'
    SHOW_HANDLE = 'show_handle'
    RELIEF = 'relief'
    HANDLE_SIZE = 'handle_size'
    BORDER_WIDTH = 'border_width'
    KEY = 'key'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.PANE_LIST:         (False, None),
            self.BACKGROUND_COLOR:  (False, None),
            self.SIZE:              (False, None),
            self.PAD:               (False, None),
            self.ORIENTATION:       (False, None),
            self.SHOW_HANDLE:       (False, None),
            self.RELIEF:            (False, None),
            self.HANDLE_SIZE:       (False, None),
            self.BORDER_WIDTH:      (False, None),
            self.KEY:               (False, None),
            self.EXPAND_X:          (False, None),
            self.EXPAND_Y:          (False, None),
            self.VISIBLE:           (False, None),
            self.METADATA:          (False, None),
        }

    def make(self, key: str, panes: Union[List[sg.Column], Tuple[sg.Column]], param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.PANE_LIST] = (True, panes)
        active_params: dict = self.__get_params__(param_key)
        return sg.Pane(**active_params)
