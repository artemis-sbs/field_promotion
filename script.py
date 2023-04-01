# start of my python script program file


import sbslibs
import sbs
import random
import sbs_utils.faces as faces
import sbs_utils.scatter as scatter
import sbs_utils.names as names
from sbs_utils.handlerhooks import *
from sbs_utils.gui import Gui
from sbs_utils.pages.start import ClientSelectPage, StartPage
from sbs_utils.objects import PlayerShip, Npc, Terrain
import sbs_utils.query as query
from sbs_utils.pymast.pymaststory import PyMastStory, PollResults
from sbs_utils.pymast.pymaststorypage import PyMastStoryPage
from helm import HelmStory
from weapons import WeaponsStory
from science import ScienceStory
from comms import CommsStory
from engineer import EngineerStory

    
# Mixins need to be first, and except generic arguments?
class SiegeStory( PyMastStory, 
                 HelmStory, 
                 WeaponsStory, 
                 ScienceStory,
                 CommsStory, 
                 EngineerStory):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # This style of init makes it more mixin friendly
        self.start_text = "Bar example: Connect as a client to go to the bar"

    def start_server(self):
        sbs.create_new_sim()
        sim = self.sim
        player_ship = PlayerShip().spawn(sim,1200,0,200, "Artemis", "tsn", "tsn_battle_cruiser")
        faces.set_face(player_ship.id, faces.random_terran())
        sbs.assign_client_to_ship(0, player_ship.id)
        self.player_id = player_ship.id
    
        self.gui_section("area: 0, 10, 99, 90;")
        self.gui_text(self.start_text)
        self.gui_section("area: 60, 75, 99, 89;row-height: 30px")
        
        yield self.await_gui({
            "Start Mission": self.start
        })

      

    def start_client(self):
        # Have change_console route here
        #
        # Events are not workign properly
        #
        #self.watch_event("client_change", self.client_change)
        self.gui_section("area: 75, 65, 99, 90;")
        console = self.gui_radio("Helm, Weapons, Comms, Engineering, Science", "Helm", True)
        sbs.assign_client_to_ship(self.get_page().client_id, self.player_id)

        def console_selected():
            pass

        yield self.await_gui({
            "Accept": console_selected
        })
        console_sel = console.value.lower()
        #print(f"{player_name} {console_sel}")
        # Keep running the console
        while True:
            match console_sel:
                case "helm":
                    yield self.jump(self.start_helm)
                case "weapons":
                    yield self.jump(self.start_weapons)
                case "science":
                    yield self.jump(self.start_science)
                case "comms":
                    yield self.jump(self.start_comms)
                case "engineering":
                    yield self.jump(self.start_engineer)
                case _:
                    self.gui_console(console_sel)
                
                #widgets = "3dview^2dview^helm_movement^throttle^request_dock^shield_control^ship_data^text_waterfall^main_screen_control"

            yield self.await_gui({
                "Accept": console_selected
            })
        



class StoryPage(PyMastStoryPage):
    story = SiegeStory()
    #story_file = "story.mast"

Gui.server_start_page_class(StoryPage)
Gui.client_start_page_class(StoryPage)

