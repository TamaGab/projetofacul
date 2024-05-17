import customtkinter as ctk
from PIL import Image
import os
from ui.components.sidebar import Sidebar

class HomeScreen:
    def __init__(self, master, user_type):
        self.master = master
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ctk.CTkImage(Image.open(self.current_path + "/../../images/pattern.png"),
                                     size=(self.master.winfo_width(), self.master.winfo_height()))
        self._setup_widgets(user_type)

    def _setup_widgets(self, user_type):
        self.bg_image_label = ctk.CTkLabel(self.master, image=self.bg_image, text="")
        self.bg_image_label.place(relwidth=1, relheight=1)
        self.sidebar = Sidebar(self.master, user_type)