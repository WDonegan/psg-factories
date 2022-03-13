import PySimpleGUI as sg
from .base import GeneratorBase


class Table(GeneratorBase):
    VALUES = 'values'
    HEADINGS = 'headings'
    VISIBLE_COLUMN_MAP = 'visible_column_map'
    COL_WIDTHS = 'col_widths'
    DEF_COL_WIDTH = 'def_col_width'
    AUTO_SIZE_COLUMNS = 'auto_size_columns'
    MAX_COL_WIDTH = 'max_col_width'
    SELECT_MODE = 'select_mode'
    DISPLAY_ROW_NUMBERS = 'display_row_numbers'
    NUM_ROWS = 'num_rows'
    ROW_HEIGHT = 'row_height'
    FONT = 'font'
    JUSTIFICATION = 'justification'
    TEXT_COLOR = 'text_color'
    BACKGROUND_COLOR = 'background_color'
    ALTERNATING_ROW_COLOR = 'alternating_row_color'
    SELECTED_ROW_COLORS = 'selected_row_colors'
    HEADER_TEXT_COLOR = 'header_text_color'
    HEADER_BACKGROUND_COLOR = 'header_background_color'
    HEADER_FONT = 'header_font'
    ROW_COLORS = 'row_colors'
    VERTICAL_SCROLL_ONLY = 'vertical_scroll_only'
    HIDE_VERTICAL_SCROLL = 'hide_vertical_scroll'
    SIZE = 'size'
    CHANGE_SUBMITS = 'change_submits'
    ENABLE_EVENTS = 'enable_events'
    ENABLE_CLICK_EVENTS = 'enable_click_events'
    RIGHT_CLICK_SELECTS = 'right_click_selects'
    BIND_RETURN_KEY = 'bind_return_key'
    PAD = 'pad'
    KEY = 'key'
    TOOLTIP = 'tooltip'
    RIGHT_CLICK_MENU = 'right_click_menu'
    EXPAND_X = 'expand_x'
    EXPAND_Y = 'expand_y'
    VISIBLE = 'visible'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.VALUES:                    (False, None),
            self.HEADINGS:                  (False, None),
            self.VISIBLE_COLUMN_MAP:        (False, None),
            self.COL_WIDTHS:                (False, None),
            self.DEF_COL_WIDTH:             (False, None),
            self.AUTO_SIZE_COLUMNS:         (False, None),
            self.MAX_COL_WIDTH:             (False, None),
            self.SELECT_MODE:               (False, None),
            self.DISPLAY_ROW_NUMBERS:       (False, None),
            self.NUM_ROWS:                  (False, None),
            self.ROW_HEIGHT:                (False, None),
            self.FONT:                      (False, None),
            self.JUSTIFICATION:             (False, None),
            self.TEXT_COLOR:                (False, None),
            self.BACKGROUND_COLOR:          (False, None),
            self.ALTERNATING_ROW_COLOR:     (False, None),
            self.SELECTED_ROW_COLORS:       (False, None),
            self.HEADER_TEXT_COLOR:         (False, None),
            self.HEADER_BACKGROUND_COLOR:   (False, None),
            self.HEADER_FONT:               (False, None),
            self.ROW_COLORS:                (False, None),
            self.VERTICAL_SCROLL_ONLY:      (False, None),
            self.HIDE_VERTICAL_SCROLL:      (False, None),
            self.SIZE:                      (False, None),
            self.CHANGE_SUBMITS:            (False, None),
            self.ENABLE_EVENTS:             (False, None),
            self.ENABLE_CLICK_EVENTS:       (False, None),
            self.RIGHT_CLICK_SELECTS:       (False, None),
            self.BIND_RETURN_KEY:           (False, None),
            self.PAD:                       (False, None),
            self.KEY:                       (False, None),
            self.TOOLTIP:                   (False, None),
            self.RIGHT_CLICK_MENU:          (False, None),
            self.EXPAND_X:                  (False, None),
            self.EXPAND_Y:                  (False, None),
            self.VISIBLE:                   (False, None),
            self.METADATA:                  (False, None),
        }

    def make(self, key: str, param_key: str = None):
        self.__parameters__[self.KEY] = (True, key)
        active_params: dict = self.__get_params__(param_key)
        return sg.Table(**active_params)
