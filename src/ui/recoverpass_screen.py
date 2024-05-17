import customtkinter as ctk
from PIL import Image
import os
from backend.auth import recover_password


class RecoverPassScreen:
    def __init__(self, master):
        self.master = master
        self.current_path = os.path.dirname(os.path.realpath(__file__))

        self.bg_image = ctk.CTkImage(Image.open(self.current_path + "/../../images/pattern.png"), size=(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.logo_image = ctk.CTkImage(dark_image=Image.open(self.current_path + "/../../images/logo.png"), size=(220, 55))

        self._setup_widgets()

    def _setup_widgets(self):
        self.clear_screen()

        self.bg_image_label = ctk.CTkLabel(self.master, image=self.bg_image, text="")
        self.bg_image_label.place(relwidth=1, relheight=1)

        self.frame_recover = ctk.CTkFrame(self.master, corner_radius=15)
        self.frame_recover.grid(row=0, column=0, padx=(self.master.winfo_screenwidth()-320)//2, pady=(self.master.winfo_screenheight()-360)//2)

        self.logo_label = ctk.CTkLabel(self.frame_recover, text="", image=self.logo_image)
        self.logo_label.grid(row=0, column=0, padx=50, pady=(30, 30))

        self.entry_email = ctk.CTkEntry(self.frame_recover, placeholder_text="Email", width=220, font=("Century Gothic", 16))
        self.entry_email.grid(row=1, column=0, padx=30, pady=(15, 15))

        self.button_recover = ctk.CTkButton(self.frame_recover, width=220, text="Recuperar Senha", fg_color="#41c269", corner_radius=32,
                                          hover_color="#4F5250", font=("Century Gothic", 18), text_color="#FFFFFF",
                                          command=self.master.show_login_screen)
        self.button_recover.grid(row=2, column=0, padx=30, pady=(30, 40))

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

