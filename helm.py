from sbs_utils import faces

    
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
        self.task.face = faces.terran(0,0,0,3,None,4,None,1,9,0)
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
        self.task.show_hint = True
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
        self.task.show_hint = True
        self.helm_show_waterfall()
        yield self.helm_buttons()

    def helm_page_10(self):
        self.task.show_hint = False
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
    def helm_show_hint(self, area, text, right= False):
        if not self.task.show_hint:
            return
        
        self.gui_activate_console("helm")
        self.gui_section(area)
        if not right:
            self.gui_face(self.task.face)
        self.gui_text(text)
        if right:
            self.gui_face(self.task.face)


    def helm_show_2d_view(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 0, 2, 85, 100-30px;")
        self.gui_console_widget("2dview")
        self.helm_show_hint("area: 2, 65, 85, 90;", """
This is the 2d View. It shows the overview of the surrounding area.
""")

    def helm_show_throttle(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 0, 60, 7, 100-30px;")
        self.gui_console_widget("throttle")
        self.helm_show_hint("area: 10, 60, 50, 99;", """
The is the throttle. It can set the impulse drive speed. and go in reverse. For more speed switch to warp speed.
""", True)

    def helm_show_movement(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 7, 75, 30, 100-30px;")
        self.gui_console_widget("helm_movement")
        self.helm_show_hint("area: 7, 55, 55, 75;", """
The is the movment control. You can steer the ship. Left, Right, Up Down, and you can even roll.
""", True)

    def helm_show_main_control(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 80, 0, 100, 25;")
        self.gui_console_widget("main_screen_control")
        self.helm_show_hint("area: 50, 25, 100, 55;", """
This is a camera control. You can control what the main screen sees.
Front View, Back, Left, Right. Long range sensors, etc.
""", True)

    def helm_show_request_dock(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 85, 25, 100, 25+30px;")
        self.gui_console_widget("request_dock")
        self.helm_show_hint("area: 50, 30, 100, 60;", """
When near a space dock pressing this button will initiate the dokcing procedure
""", False)

    def helm_show_shield_control(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 85, 25+30px, 100, 25+60px;")
        self.gui_console_widget("shield_control")
        self.helm_show_hint("area: 50, 35, 100, 65;", """
This controls whether the shields are on. Having them off saves energy, but you probably what them on when bad guys are around.
""", False)

    def helm_show_ship_data(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 85, 30,100, 60")
        self.gui_console_widget("ship_data")
        self.helm_show_hint("area: 65, 15, 100, 30;", """
This is the ship data showing the ship condition and the number of weapons the ship has.
""", True)

    def helm_show_3d_view(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 85, 60,100, 85")
        self.gui_console_widget("3dview")
        self.helm_show_hint("area: 65, 30, 100, 60;", """
A look out side!
""", True)
    
    def helm_show_waterfall(self):
        self.gui_activate_console("helm")
        self.gui_section("area: 85, 85,100,100-30px")
        self.gui_console_widget("text_waterfall")
        self.helm_show_hint("area: 65, 60, 100, 85;", """
Messages may show up hear.
""", True)
