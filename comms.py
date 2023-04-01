

    
# Mixins need to be first, and except generic arguments?
class CommsStory:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # This style of init makes it more mixin friendly
     
    def start_comms(self):
        self.comms_pages = [
            self.comms_page_01,
            self.comms_page_02,
            self.comms_page_03,
            self.comms_page_04,
            self.comms_page_05,
            self.comms_page_06,
            self.comms_page_07,
        ]
        self.task.comms_page = 0
        yield self.jump(self.comms_pages[0])


    def comms_page_next(self):
        self.task.comms_page += 1
        yield self.task.jump(self.comms_pages[self.task.comms_page])

    def comms_page_prev(self):
        self.task.comms_page -= 1
        yield self.jump(self.comms_pages[self.task.comms_page])

    def comms_buttons(self):
        buttons = {
            "Prev": self.comms_page_prev,
            "Next": self.comms_page_next,
        }
        if self.task.comms_page == 0:
            buttons.pop("Prev")
        if self.task.comms_page == len(self.comms_pages)-1:
            buttons.pop("Next")
        return self.await_gui(buttons)

    def comms_page_01(self):
        self.comms_show_comms_control()
        yield self.comms_buttons()

    def comms_page_02(self):
        self.comms_show_comms_face()
        yield self.comms_buttons()

    def comms_page_03(self):
        self.comms_show_comms_messsages()
        yield self.comms_buttons()

    def comms_page_04(self):
        self.comms_show_comms_list()
        yield self.comms_buttons()

    def comms_page_05(self):
        self.comms_show_ship_data()
        yield self.comms_buttons()

    def comms_page_06(self):
        self.comms_show_waterfall()
        yield self.comms_buttons()

    def comms_page_07(self):
        self.comms_show_comms_control()
        self.comms_show_comms_face()
        self.comms_show_comms_messsages()
        self.comms_show_comms_list()
        self.comms_show_ship_data()
        self.comms_show_waterfall()
        yield self.comms_buttons()

    ###################################
    # Helpers to layout and show each control
    def comms_show_comms_control(self):
        self.gui_activate_console("comms")
        self.gui_section("area: 30, 30, 60, 100-30px;")
        self.gui_console_widget("comms_control")

    def comms_show_comms_face(self):
        self.gui_activate_console("comms")
        
        self.gui_section("area: 30, 0, 60, 30;")
        f = self.gui_console_widget("comms_face")
        f.square = True


    def comms_show_comms_messsages(self):
        self.gui_activate_console("comms")
        self.gui_section("area: 60, 0, 100, 80;")
        self.gui_console_widget("comms_waterfall")

    def comms_show_comms_list(self):
        self.gui_activate_console("comms")
        self.gui_section("area: 0, 32px, 30, 55;")
        self.gui_console_widget("comms_sorted_list")
    
    def comms_show_ship_data(self):
        self.gui_activate_console("comms")
        self.gui_section("area: 0, 55,30, 100-30px;")
        self.gui_console_widget("ship_data")
    
    def comms_show_waterfall(self):
        self.gui_activate_console("comms")
        self.gui_section("area: 60, 80,100,100-30px;")
        self.gui_console_widget("text_waterfall")
