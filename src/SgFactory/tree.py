import PySimpleGUI as sg
from .base import GeneratorBase


class Tree(GeneratorBase):
    DATA = 'data'
    HEADINGS = 'headings'
    VISIBLE_COLUMN_MAP = 'visible_column_map'
    COL_WIDTHS = 'col_widths'
    COL0_WIDTH = 'col0_width'
    COL0_HEADING = 'col0_heading'
    DEF_COL_WIDTH = 'def_col_width'
    AUTO_SIZE_COLUMNS = 'auto_size_columns'
    MAX_COL_WIDTH = 'max_col_width'
    SELECT_MODE = 'select_mode'
    SHOW_EXPANDED = 'show_expanded'
    CHANGE_SUBMITS = 'change_submits'
    ENABLE_EVENTS = 'enable_events'
    FONT = 'font'
    JUSTIFICATION = 'justification'
    TEXT_COLOR = 'text_color'
    BACKGROUND_COLOR = 'background_color'
    SELECTED_ROW_COLORS = 'selected_row_colors'
    HEADER_TEXT_COLOR = 'header_text_color'
    HEADER_BACKGROUND_COLOR = 'header_background_color'
    HEADER_FONT = 'header_font'
    NUM_ROWS = 'num_rows'
    ROW_HEIGHT = 'row_height'
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
            self.DATA:                      (False, None),
            self.HEADINGS:                  (False, None),
            self.VISIBLE_COLUMN_MAP:        (False, None),
            self.COL_WIDTHS:                (False, None),
            self.COL0_WIDTH:                (False, None),
            self.COL0_HEADING:              (False, None),
            self.DEF_COL_WIDTH:             (False, None),
            self.AUTO_SIZE_COLUMNS:         (False, None),
            self.MAX_COL_WIDTH:             (False, None),
            self.SELECT_MODE:               (False, None),
            self.SHOW_EXPANDED:             (False, None),
            self.CHANGE_SUBMITS:            (False, None),
            self.ENABLE_EVENTS:             (False, None),
            self.FONT:                      (False, None),
            self.JUSTIFICATION:             (False, None),
            self.TEXT_COLOR:                (False, None),
            self.BACKGROUND_COLOR:          (False, None),
            self.SELECTED_ROW_COLORS:       (False, None),
            self.HEADER_TEXT_COLOR:         (False, None),
            self.HEADER_BACKGROUND_COLOR:   (False, None),
            self.HEADER_FONT:               (False, None),
            self.NUM_ROWS:                  (False, None),
            self.ROW_HEIGHT:                (False, None),
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
        return sg.Tree(**active_params)
