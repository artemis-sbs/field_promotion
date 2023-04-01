

    
# Mixins need to be first, and except generic arguments?
class WeaponsStory:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # This style of init makes it more mixin friendly
     
    def start_weapons(self):
        self.weapons_pages = [
            self.weapons_page_01,
            self.weapons_page_02,
            self.weapons_page_03,
            self.weapons_page_04,
            self.weapons_page_05,
            self.weapons_page_06,
            self.weapons_page_07,
        ]
        self.task.weapons_page = 0
        yield self.jump(self.weapons_pages[0])


    def weapons_page_next(self):
        self.task.weapons_page += 1
        yield self.task.jump(self.weapons_pages[self.task.weapons_page])

    def weapons_page_prev(self):
        self.task.weapons_page -= 1
        yield self.jump(self.weapons_pages[self.task.weapons_page])

    def weapons_buttons(self):
        buttons = {
            "Prev": self.weapons_page_prev,
            "Next": self.weapons_page_next,
        }
        if self.task.weapons_page == 0:
            buttons.pop("Prev")
        if self.task.weapons_page == len(self.weapons_pages)-1:
            buttons.pop("Next")
        return self.await_gui(buttons)

    def weapons_page_01(self):
        self.weapons_show_2d_view()
        yield self.weapons_buttons()

    def weapons_page_02(self):
        self.weapons_show_weapon_control()
        yield self.weapons_buttons()

    def weapons_page_03(self):
        self.weapons_show_main_control()
        yield self.weapons_buttons()

    def weapons_page_04(self):
        self.weapons_show_shield_control()
        yield self.weapons_buttons()

    def weapons_page_05(self):
        self.weapons_show_ship_data()
        yield self.weapons_buttons()
    def weapons_page_06(self):
        self.weapons_show_waterfall()
        yield self.weapons_buttons()

    def weapons_page_07(self):
        self.weapons_show_2d_view()
        self.weapons_show_weapon_control()
        self.weapons_show_main_control()
        self.weapons_show_shield_control()
        self.weapons_show_ship_data()
        #self.weapons_show_3d_view()
        self.weapons_show_waterfall()
        yield self.weapons_buttons()

    ###################################
    # Helpers to layout and show each control
    def weapons_show_2d_view(self):
        self.gui_activate_console("weapons")
        self.gui_section("area: 0, 2, 85, 100-30px;")
        self.gui_console_widget("2dview")

    def weapons_show_weapon_control(self):
        self.gui_activate_console("weapons")
        self.gui_section("area: 0, 75, 30, 100-30px;")
        self.gui_console_widget("weapon_control")

    def weapons_show_main_control(self):
        self.gui_activate_console("weapons")
        self.gui_section("area: 80, 0, 100, 25;")
        self.gui_console_widget("main_screen_control")

    def weapons_show_shield_control(self):
        self.gui_activate_console("weapons")
        self.gui_section("area: 85, 25+30px, 100, 25+60px;")
        self.gui_console_widget("shield_control")

    def weapons_show_ship_data(self):
        self.gui_activate_console("weapons")
        self.gui_section("area: 85, 30,100, 60")
        self.gui_console_widget("ship_data")

    def weapons_show_3d_view(self):
        self.gui_activate_console("weapons")
        self.gui_section("area: 85, 60,100, 85")
        self.gui_console_widget("3dview")
    
    def weapons_show_waterfall(self):
        self.gui_activate_console("weapons")
        self.gui_section("area: 85, 85,100,100-30px")
        self.gui_console_widget("text_waterfall")
