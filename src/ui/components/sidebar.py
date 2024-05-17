import customtkinter as ctk
from PIL import Image
import os
from backend.home import buttons_aluno, buttons_professor

class Sidebar:
    def __init__(self, master, user_type):
        self.master = master
        self.user_type = user_type
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self._setup_widgets()
        self._shrink_sidebar()  # Inicia a sidebar encolhida

    def _setup_widgets(self):
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        
        self.frame_shrinkmenu = ctk.CTkFrame(self.master, width=50, corner_radius=0)
        self.frame_shrinkmenu.grid(row=0, column=0, sticky="ns")
        
        self.frame_menu = ctk.CTkFrame(self.master, width=300, corner_radius=0)

        logo_image = ctk.CTkImage(dark_image=Image.open(self.current_path + "/../../../images/logo.png"), size=(220, 55))
        logo_label = ctk.CTkLabel(self.frame_menu, text="", image=logo_image)
        logo_label.grid(row=0, column=0, padx=50, pady=(30, 30))

        buttons = buttons_aluno if self.user_type == "aluno" else buttons_professor
        self.button_widgets = []  # List to keep track of button widgets

        for key, button in buttons.items():
            button_image = ctk.CTkImage(dark_image=Image.open(self.current_path + button["url_imagem"]))
            button_icon = ctk.CTkLabel(self.frame_shrinkmenu, image=button_image, text="")
            button_icon.grid(row=int(key), column=0, padx=10, pady=(30, 15))

            if button["nome"] != "logo":
                button_place = ctk.CTkButton(self.frame_menu, width=280, height=40, text=button["nome"], fg_color="transparent", corner_radius=6,
                                             hover_color="#4F5250", font=("Century Gothic", 18), text_color="#FFFFFF",
                                             image=button_image, anchor='w')
                button_place.grid(row=int(key), column=0, padx=10, pady=(15, 15))
                self.button_widgets.append(button_place)  # Add button to the list
                
                button_place.bind("<Enter>", self._expand_sidebar)
                button_place.bind("<Leave>", self._schedule_shrink_sidebar)

        for widget in [self.frame_menu, self.frame_shrinkmenu, logo_label]:
            
            widget.bind("<Leave>", self._schedule_shrink_sidebar)
            widget.bind("<Enter>", self._expand_sidebar)

    
    
    def _expand_sidebar(self, event):
        if hasattr(self.master, 'shrink_sidebar_after_id'):
            self.master.after_cancel(self.master.shrink_sidebar_after_id)
        self.frame_menu.grid(row=0, column=0, sticky="nsw")
        self.frame_shrinkmenu.grid_forget()

    def _schedule_shrink_sidebar(self, event=None):
        self.master.shrink_sidebar_after_id = self.master.after(500, self._shrink_sidebar)

    def _shrink_sidebar(self):
        self.frame_menu.grid_forget()
        self.frame_shrinkmenu.grid(row=0, column=0, sticky="nsw")