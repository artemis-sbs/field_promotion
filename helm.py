

    
# Mixins need to be first, and except generic arguments?
class HelmStory:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # This style of init makes it more mixin friendly
     

    def start_helm(self):
        self.helm_pages = [
            self.helm_page_01,
            self.helm_page_02,
            self.helm_page_03,
            self.helm_page_04,
            self.helm_page_05,
            self.helm_page_06,
            self.helm_page_07,
            self.helm_page_08,
            self.helm_page_09,
            self.helm_page_10,
        ]
        self.task.helm_page = 0
        yield self.jump(self.helm_pages[0])


    def helm_page_next(self):
        self.task.helm_page += 1
        yield self.task.jump(self.helm_pages[self.task.helm_page])

    def helm_page_prev(self):
        self.task.helm_page -= 1
        yield self.jump(self.helm_pages[self.task.helm_page])

    def helm_buttons(self):
        buttons = {
            "Prev": self.helm_page_prev,
            "Next": self.helm_page_next,
        }
        if self.task.helm_page == 0:
            buttons.pop("Prev")
        if self.task.helm_page == len(self.helm_pages)-1:
            buttons.pop("Next")
        return self.await_gui(buttons)

    def helm_page_01(self):
        self.helm_show_2d_view()
        yield self.helm_buttons()

    def helm_page_02(self):
        self.helm_show_throttle()
        yield self.helm_buttons()

    def helm_page_03(self):
        self.helm_show_movement()
        yield self.helm_buttons()

    def helm_page_04(self):
        self.helm_show_main_control()
        yield self.helm_buttons()

    def helm_page_05(self):
        self.helm_show_request_dock()
        yield self.helm_buttons()

    def helm_page_06(self):
        self.helm_show_shield_control()
        yield self.helm_buttons()

    def helm_page_07(self):
        self.helm_show_ship_data()
        yield self.helm_buttons()

    def helm_page_08(self):
        self.helm_show_3d_view()
        yield self.helm_buttons()

    def helm_page_09(self):
        self.helm_show_waterfall()
        yield self.helm_buttons()

    def helm_page_10(self):
        self.helm_show_2d_view()
        self.helm_show_throttle()
        self.helm_show_movement()
        self.helm_show_main_control()
        self.helm_show_request_dock()
        self.helm_show_shield_control()
        self.helm_show_ship_data()
        self.helm_show_3d_view()
        self.helm_show_waterfall()
        yield self.helm_buttons()

    ###################################
    # Helpers to layout and show each control
    def helm_show_2d_view(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 0, 2, 85, 100-30px;")
        self.gui_console_widget("2dview")

    def helm_show_throttle(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 0, 60, 7, 100-30px;")
        self.gui_console_widget("throttle")

    def helm_show_movement(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 7, 75, 30, 100-30px;")
        self.gui_console_widget("helm_movement")

    def helm_show_main_control(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 80, 0, 100, 25;")
        self.gui_console_widget("main_screen_control")

    def helm_show_request_dock(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 85, 25, 100, 25+30px;")
        self.gui_console_widget("request_dock")

    def helm_show_shield_control(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 85, 25+30px, 100, 25+60px;")
        self.gui_console_widget("shield_control")

    def helm_show_ship_data(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 85, 30,100, 60")
        self.gui_console_widget("ship_data")

    def helm_show_3d_view(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 85, 60,100, 85")
        self.gui_console_widget("3dview")
    
    def helm_show_waterfall(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 85, 85,100,100-30px")
        self.gui_console_widget("text_waterfall")
