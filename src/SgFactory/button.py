import PySimpleGUI as sg
from .base import GeneratorBase


class Button(GeneratorBase):
    BUTTON_TEXT = 'button_text'
    BUTTON_TYPE = 'button_type'
    TARGET = 'target'
    TOOLTIP = 'tooltip'
    FILE_TYPES = 'file_types'
    INITIAL_FOLDER = 'initial_folder'
    DEFAULT_EXTENSION = 'default_extension'
    DISABLED = 'disabled'
    CHANGE_SUBMITS = 'change_submits'
    ENABLE_EVENTS = 'enable_events'
    IMAGE_FILENAME = 'image_filename'
    IMAGE_DATA = 'image_data'
    IMAGE_SIZE = 'image_size'
    IMAGE_SUBSAMPLE = 'image_subsample'
    BORDER_WIDTH = 'border_width'
    SIZE = 'size'
    AUTO_SIZE_BUTTON = 'auto_size_button'
    BUTTON_COLOR = 'button_color'
    DISABLED_BUTTON_COLOR = 'disabled_button_color'
    HIGHLIGHT_COLORS = 'highlight_colors'
    MOUSEOVER_COLORS = 'mouseover_colors'
    USE_TTK_BUTTONS = 'use_ttk_buttons'
    FONT = 'font'
    BIND_RETURN_KEY = 'bind_return_key'
    FOCUS = 'focus'
    PAD = 'pad'
    KEY = 'key'
    RIGHT_CLICK_MENU = 'right_click_menu'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.BUTTON_TEXT:           (False, None),
            self.BUTTON_TYPE:           (False, None),
            self.TARGET:                (False, None),
            self.TOOLTIP:               (False, None),
            self.FILE_TYPES:            (False, None),
            self.INITIAL_FOLDER:        (False, None),
            self.DEFAULT_EXTENSION:     (False, None),
            self.DISABLED:              (False, None),
            self.CHANGE_SUBMITS:        (False, None),
            self.ENABLE_EVENTS:         (False, None),
            self.IMAGE_FILENAME:        (False, None),
            self.IMAGE_DATA:            (False, None),
            self.IMAGE_SIZE:            (False, None),
            self.IMAGE_SUBSAMPLE:       (False, None),
            self.BORDER_WIDTH:          (False, None),
            self.SIZE:                  (False, None),
            self.AUTO_SIZE_BUTTON:      (False, None),
            self.BUTTON_COLOR:          (False, None),
            self.DISABLED_BUTTON_COLOR: (False, None),
            self.HIGHLIGHT_COLORS:      (False, None),
            self.MOUSEOVER_COLORS:      (False, None),
            self.USE_TTK_BUTTONS:       (False, None),
            self.FONT:                  (False, None),
            self.BIND_RETURN_KEY:       (False, None),
            self.FOCUS:                 (False, None),
            self.PAD:                   (False, None),
            self.KEY:                   (False, None),
            self.RIGHT_CLICK_MENU:      (False, None),
            self.EXPAND_X:              (False, None),
            self.EXPAND_Y:              (False, None),
            self.VISIBLE:               (False, None),
            self.METADATA:              (False, None),
        }

    def make(self, key: str, text: str = '', param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        self.__parameters__[self.BUTTON_TEXT] = (True, text)
        active_params: dict = self.__get_params__(param_key)
        return sg.Button(**active_params)
