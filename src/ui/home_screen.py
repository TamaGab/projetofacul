import customtkinter as ctk
from PIL import Image
import os
from ui.homewidgets.sidebar import Sidebar
from ui.homewidgets.homewidgets import HomeWidgets

class HomeScreen:
    def __init__(self, master, user_type):
        self.master = master
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ctk.CTkImage(Image.open(os.path.join(self.current_path, "../../images/pattern.png")),
                                     size=(self.master.winfo_width(), self.master.winfo_height()))
        self._setup_widgets(user_type)

    def _setup_widgets(self, user_type):

        self.bg_image_label = ctk.CTkLabel(self.master, image=self.bg_image, text="")
        self.bg_image_label.place(relwidth=1, relheight=1)
        
        self.home_widgets = HomeWidgets(self.master, user_type)
        self.sidebar = Sidebar(self.master, self.home_widgets, user_type)

        self.home_widgets.welcome_widget()
        self.home_widgets.place_widget('alunos' if user_type == 'aluno' else 'professor_info')

