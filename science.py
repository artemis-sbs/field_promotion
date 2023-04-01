

    
# Mixins need to be first, and except generic arguments?
class ScienceStory:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # This style of init makes it more mixin friendly
     
    def start_science(self):
        self.science_pages = [
            self.science_page_01,
            self.science_page_02,
            self.science_page_03,
            self.science_page_04,
            self.science_page_05,
            self.science_page_06,
        ]
        self.task.science_page = 0
        yield self.jump(self.science_pages[0])


    def science_page_next(self):
        self.task.science_page += 1
        yield self.task.jump(self.science_pages[self.task.science_page])

    def science_page_prev(self):
        self.task.science_page -= 1
        yield self.jump(self.science_pages[self.task.science_page])

    def science_buttons(self):
        buttons = {
            "Prev": self.science_page_prev,
            "Next": self.science_page_next,
        }
        if self.task.science_page == 0:
            buttons.pop("Prev")
        if self.task.science_page == len(self.science_pages)-1:
            buttons.pop("Next")
        return self.await_gui(buttons)

    def science_page_01(self):
        self.science_show_2d_view()
        yield self.science_buttons()

    def science_page_02(self):
        self.science_show_science_data()
        yield self.science_buttons()

    def science_page_03(self):
        self.science_show_science_list()
        yield self.science_buttons()

    def science_page_04(self):
        self.science_show_ship_data()
        yield self.science_buttons()
    def science_page_05(self):
        self.science_show_waterfall()
        yield self.science_buttons()

    def science_page_06(self):
        self.science_show_2d_view()
        self.science_show_science_data()
        self.science_show_science_list()
        self.science_show_ship_data()
        #self.science_show_3d_view()
        self.science_show_waterfall()
        yield self.science_buttons()

#"science_2d_view^ship_data^text_waterfall^science_data^science_sorted_list"
    ###################################
    # Helpers to layout and show each control
    def science_show_2d_view(self):
        self.gui_activate_console("science")
        self.gui_section("area: 0, 2, 80, 100-30px;")
        self.gui_console_widget("science_2d_view")

    def science_show_science_data(self):
        self.gui_activate_console("science")
        self.gui_section("area: 80, 0, 100, 20;")
        self.gui_console_widget("science_data")

    def science_show_science_list(self):
        self.gui_activate_console("science")
        self.gui_section("area: 80, 20, 100, 60;")
        self.gui_console_widget("science_sorted_list")
    
    def science_show_ship_data(self):
        self.gui_activate_console("science")
        self.gui_section("area: 80, 60,100, 85;")
        self.gui_console_widget("ship_data")
    
    def science_show_waterfall(self):
        self.gui_activate_console("science")
        self.gui_section("area: 80, 85,100,100-30px;")
        self.gui_console_widget("text_waterfall")
