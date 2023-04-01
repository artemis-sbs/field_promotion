

    
# Mixins need to be first, and except generic arguments?
class EngineerStory:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # This style of init makes it more mixin friendly
     
    def start_engineer(self):
        self.engineer_pages = [
            self.engineer_page_01,
            self.engineer_page_02,
            self.engineer_page_03,
            self.engineer_page_04,
            self.engineer_page_05,
            self.engineer_page_06,
            self.engineer_page_07,
        ]
        self.task.engineer_page = 0
        yield self.jump(self.engineer_pages[0])


    def engineer_page_next(self):
        self.task.engineer_page += 1
        yield self.task.jump(self.engineer_pages[self.task.engineer_page])

    def engineer_page_prev(self):
        self.task.engineer_page -= 1
        yield self.jump(self.engineer_pages[self.task.engineer_page])

    def engineer_buttons(self):
        buttons = {
            "Prev": self.engineer_page_prev,
            "Next": self.engineer_page_next,
        }
        if self.task.engineer_page == 0:
            buttons.pop("Prev")
        if self.task.engineer_page == len(self.engineer_pages)-1:
            buttons.pop("Next")
        return self.await_gui(buttons)

    def engineer_page_01(self):
        self.engineer_show_internal()
        yield self.engineer_buttons()

    def engineer_page_02(self):
        self.engineer_show_engineer_data()
        yield self.engineer_buttons()

    def engineer_page_03(self):
        self.engineer_show_engineer_heat()
        yield self.engineer_buttons()

    def engineer_page_04(self):
        self.engineer_show_engineer_power()
        yield self.engineer_buttons()

    def engineer_page_05(self):
        self.engineer_show_ship_data()
        yield self.engineer_buttons()
    def engineer_page_06(self):
        self.engineer_show_waterfall()
        yield self.engineer_buttons()

    def engineer_page_07(self):
        self.engineer_show_internal()
        self.engineer_show_engineer_data()
        self.engineer_show_engineer_heat()
        self.engineer_show_engineer_power()
        self.engineer_show_ship_data()
        #self.engineer_show_3d_view()
        self.engineer_show_waterfall()
        yield self.engineer_buttons()

#"engineer_2d_view^ship_data^text_waterfall^engineer_data^engineer_sorted_list"
    ###################################
    # Helpers to layout and show each control
    def engineer_show_internal(self):
        self.gui_activate_console("engineer")
        self.gui_section("area: 50, 30px, 100, 50;")
        g = self.gui_console_widget("ship_internal_view")
        #g.square = True

    def engineer_show_engineer_data(self):
        self.gui_activate_console("engineer")
        self.gui_section("area: 50, 50, 100, 100-30px;")
        self.gui_console_widget("grid_object_list")

    def engineer_show_engineer_heat(self):
        self.gui_activate_console("engineer")
        self.gui_section("area: 0, 30px, 50, 35;")
        self.gui_console_widget("eng_heat_controls")

    def engineer_show_engineer_power(self):
        self.gui_activate_console("engineer")
        self.gui_section("area: 0, 35, 50, 70;")
        self.gui_console_widget("eng_power_controls")

    
    def engineer_show_ship_data(self):
        self.gui_activate_console("engineer")
        self.gui_section("area: 0, 70, 25, 100-30px;")
        self.gui_console_widget("ship_data")
    
    def engineer_show_waterfall(self):
        self.gui_activate_console("engineer")
        self.gui_section("area: 25, 70, 50,100-30px;")
        self.gui_console_widget("text_waterfall")
