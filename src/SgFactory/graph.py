from typing import Tuple

import PySimpleGUI as sg
from .base import GeneratorBase


class Graph(GeneratorBase):
    CANVAS_SIZE = 'canvas_size'
    GRAPH_BOTTOM_LEFT = 'graph_bottom_left'
    GRAPH_TOP_RIGHT = 'graph_top_right'
    BACKGROUND_COLOR = 'background_color'
    PAD = 'pad'
    CHANGE_SUBMITS = 'change_submits'
    DRAG_SUBMITS = 'drag_submits'
    ENABLE_EVENTS = 'enable_events'
    MOTION_EVENTS = 'motion_events'
    KEY = 'key'
    TOOLTIP = 'tooltip'
    RIGHT_CLICK_MENU = 'right_click_menu'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    VISIBLE = 'visible'
    FLOAT_VALUES = 'float_values'
    BORDER_WIDTH = 'border_width'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.CANVAS_SIZE:       (False, None),
            self.GRAPH_BOTTOM_LEFT: (False, None),
            self.GRAPH_TOP_RIGHT:   (False, None),
            self.BACKGROUND_COLOR:  (False, None),
            self.PAD:               (False, None),
            self.CHANGE_SUBMITS:    (False, None),
            self.DRAG_SUBMITS:      (False, None),
            self.ENABLE_EVENTS:     (False, None),
            self.MOTION_EVENTS:     (False, None),
            self.KEY:               (False, None),
            self.TOOLTIP:           (False, None),
            self.RIGHT_CLICK_MENU:  (False, None),
            self.EXPAND_X:          (False, None),
            self.EXPAND_Y:          (False, None),
            self.VISIBLE:           (False, None),
            self.FLOAT_VALUES:      (False, None),
            self.BORDER_WIDTH:      (False, None),
            self.METADATA:          (False, None),
        }

    def make(self, key: str, size: Tuple[int, int], bottom_left: Tuple[int, int], top_right: Tuple[int, int],  param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.CANVAS_SIZE] = (True, size)
        self.__parameters__[self.GRAPH_BOTTOM_LEFT] = (True, bottom_left)
        self.__parameters__[self.GRAPH_TOP_RIGHT] = (True, top_right)
        active_params: dict = self.__get_params__(param_key)
        return sg.Graph(**active_params)
