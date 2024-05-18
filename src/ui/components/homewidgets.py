import customtkinter as ctk
import os
from backend.home import get_name

class HomeWidgets:
    def __init__(self, master):
        self.master = master
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self._setup_widgets()

    def _setup_widgets(self):

        self.frame_homeinit = ctk.CTkFrame(self.master)
        self.frame_homeinit.place(relwidth=0.5, relheight= 0.5, relx=0.61, rely=0.5, anchor="center")
        
        self.label = ctk.CTkLabel(self.frame_homeinit, text=f"SEJA BEM VINDO {get_name()} ")