import PySimpleGUI as sg
from .base import GeneratorBase


class Window(GeneratorBase):
    TITLE = 'title'
    LAYOUT = 'layout'
    DEFAULT_ELEMENT_SIZE = 'default_element_size'
    DEFAULT_BUTTON_ELEMENT_SIZE = 'default_button_element_size'
    AUTO_SIZE_TEXT = 'auto_size_text'
    AUTO_SIZE_BUTTONS = 'auto_size_buttons'
    LOCATION = 'location'
    RELATIVE_LOCATION = 'relative_location'
    SIZE = 'size'
    ELEMENT_PADDING = 'element_padding'
    MARGINS = 'margins'
    BUTTON_COLOR = 'button_color'
    FONT = 'font'
    PROGRESS_BAR_COLOR = 'progress_bar_color'
    BACKGROUND_COLOR = 'background_color'
    BORDER_DEPTH = 'border_depth'
    AUTO_CLOSE = 'auto_close'
    AUTO_CLOSE_DURATION = 'auto_close_duration'
    ICON = 'icon'
    FORCE_TOPLEVEL = 'force_toplevel'
    ALPHA_CHANNEL = 'alpha_channel'
    RETURN_KEYBOARD_EVENTS = 'return_keyboard_events'
    USE_DEFAULT_FOCUS = 'use_default_focus'
    TEXT_JUSTIFICATION = 'text_justification'
    NO_TITLEBAR = 'no_titlebar'
    GRAB_ANYWHERE = 'grab_anywhere'
    GRAB_ANYWHERE_USING_CONTROL = 'grab_anywhere_using_control'
    KEEP_ON_TOP = 'keep_on_top'
    RESIZABLE = 'resizable'
    DISABLE_CLOSE = 'disable_close'
    DISABLE_MINIMIZE = 'disable_minimize'
    RIGHT_CLICK_MENU = 'right_click_menu'
    TRANSPARENT_COLOR = 'transparent_color'
    DEBUGGER_ENABLED = 'debugger_enabled'
    RIGHT_CLICK_MENU_BACKGROUND_COLOR = 'right_click_menu_background_color'
    RIGHT_CLICK_MENU_TEXT_COLOR = 'right_click_menu_text_color'
    RIGHT_CLICK_MENU_DISABLED_TEXT_COLOR = 'right_click_menu_disabled_text_color'
    RIGHT_CLICK_MENU_SELECTED_COLORS = 'right_click_menu_selected_colors'
    RIGHT_CLICK_MENU_FONT = 'right_click_menu_font'
    RIGHT_CLICK_MENU_TEAROFF = 'right_click_menu_tearoff'
    FINALIZE = 'finalize'
    ELEMENT_JUSTIFICATION = 'element_justification'
    TTK_THEME = 'ttk_theme'
    USE_TTK_BUTTONS = 'use_ttk_buttons'
    MODAL = 'modal'
    ENABLE_CLOSE_ATTEMPTED_EVENT = 'enable_close_attempted_event'
    TITLEBAR_BACKGROUND_COLOR = 'titlebar_background_color'
    TITLEBAR_TEXT_COLOR = 'titlebar_text_color'
    TITLEBAR_FONT = 'titlebar_font'
    TITLEBAR_ICON = 'titlebar_icon'
    USE_CUSTOM_TITLEBAR = 'use_custom_titlebar'
    SCALING = 'scaling'
    METADATA = 'metadata'

    def reset_params(self):
        self.__parameters__ = {
            self.TITLE:                                 (False, None),
            self.LAYOUT:                                (False, None),
            self.DEFAULT_ELEMENT_SIZE:                  (False, None),
            self.DEFAULT_BUTTON_ELEMENT_SIZE:           (False, None),
            self.AUTO_SIZE_TEXT:                        (False, None),
            self.AUTO_SIZE_BUTTONS:                     (False, None),
            self.LOCATION:                              (False, None),
            self.RELATIVE_LOCATION:                     (False, None),
            self.SIZE:                                  (False, None),
            self.ELEMENT_PADDING:                       (False, None),
            self.MARGINS:                               (False, None),
            self.BUTTON_COLOR:                          (False, None),
            self.FONT:                                  (False, None),
            self.PROGRESS_BAR_COLOR:                    (False, None),
            self.BACKGROUND_COLOR:                      (False, None),
            self.BORDER_DEPTH:                          (False, None),
            self.AUTO_CLOSE:                            (False, None),
            self.AUTO_CLOSE_DURATION:                   (False, None),
            self.ICON:                                  (False, None),
            self.FORCE_TOPLEVEL:                        (False, None),
            self.ALPHA_CHANNEL:                         (False, None),
            self.RETURN_KEYBOARD_EVENTS:                (False, None),
            self.USE_DEFAULT_FOCUS:                     (False, None),
            self.TEXT_JUSTIFICATION:                    (False, None),
            self.NO_TITLEBAR:                           (False, None),
            self.GRAB_ANYWHERE:                         (False, None),
            self.GRAB_ANYWHERE_USING_CONTROL:           (False, None),
            self.KEEP_ON_TOP:                           (False, None),
            self.RESIZABLE:                             (False, None),
            self.DISABLE_CLOSE:                         (False, None),
            self.DISABLE_MINIMIZE:                      (False, None),
            self.RIGHT_CLICK_MENU:                      (False, None),
            self.TRANSPARENT_COLOR:                     (False, None),
            self.DEBUGGER_ENABLED:                      (False, None),
            self.RIGHT_CLICK_MENU_BACKGROUND_COLOR:     (False, None),
            self.RIGHT_CLICK_MENU_TEXT_COLOR:           (False, None),
            self.RIGHT_CLICK_MENU_DISABLED_TEXT_COLOR:  (False, None),
            self.RIGHT_CLICK_MENU_SELECTED_COLORS:      (False, None),
            self.RIGHT_CLICK_MENU_FONT:                 (False, None),
            self.RIGHT_CLICK_MENU_TEAROFF:              (False, None),
            self.FINALIZE:                              (False, None),
            self.ELEMENT_JUSTIFICATION:                 (False, None),
            self.TTK_THEME:                             (False, None),
            self.USE_TTK_BUTTONS:                       (False, None),
            self.MODAL:                                 (False, None),
            self.ENABLE_CLOSE_ATTEMPTED_EVENT:          (False, None),
            self.TITLEBAR_BACKGROUND_COLOR:             (False, None),
            self.TITLEBAR_TEXT_COLOR:                   (False, None),
            self.TITLEBAR_FONT:                         (False, None),
            self.TITLEBAR_ICON:                         (False, None),
            self.USE_CUSTOM_TITLEBAR:                   (False, None),
            self.SCALING:                               (False, None),
            self.METADATA:                              (False, None),
        }

    def make(self, title: str, param_key: str = None):
        self.__parameters__[self.TITLE] = (True, title)
        active_params: dict = self.__get_params__(param_key)
        return sg.Window(**active_params)
