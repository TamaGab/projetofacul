import customtkinter as ctk
from PIL import Image
import os
from backend.auth import login_user

class LoginScreen:
    def __init__(self, master):
        self.master = master
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ctk.CTkImage(Image.open(self.current_path + "/../../images/pattern.png"),
                                     size=(self.master.width, self.master.height))
        self.logo_image = ctk.CTkImage(dark_image=Image.open(self.current_path + "/../../images/logo.png"), size=(220, 55))
        self._setup_widgets()

    def _setup_widgets(self):
        self.bg_image_label = ctk.CTkLabel(self.master, image=self.bg_image, text="")
        self.bg_image_label.place(relwidth=1, relheight=1)
        
        self.frame_login = ctk.CTkFrame(self.master, corner_radius=15)
        self.frame_login.grid(row=0, column=0, padx=(self.master.width-320)//2, pady=(self.master.height-360)//2)
        
        self.logo_label = ctk.CTkLabel(self.frame_login, text="", image=self.logo_image)
        self.logo_label.grid(row=0, column=0, padx=50, pady=(30, 30), columnspan=6)
        
        self.entry_user = ctk.CTkEntry(self.frame_login, placeholder_text="Usuario", width=220, font=("Century Gothic", 16))
        self.entry_user.grid(row=1, column=0, padx=30, pady=(15, 15), columnspan=6)
        self.entry_user.bind("<Return>", lambda event: self.entry_password.focus_set())
        
        self.entry_password = ctk.CTkEntry(self.frame_login, placeholder_text="Senha", width=220, show="*", font=("Century Gothic", 16))
        self.entry_password.grid(row=2, column=0, padx=30, pady=(15, 5), columnspan=6)
        self.entry_password.bind("<Return>", lambda event: login_user(self.entry_user, self.entry_password, self.master.show_home_screen))
        
        self.button_fpassword = ctk.CTkButton(self.frame_login, width=110, text="Esqueceu a senha?", fg_color="transparent",
                                              font=("Century Gothic", 12,), text_color="#FFFFFF", hover=False, command=self.master.show_recoverpass_screen)
        self.button_fpassword.grid(row=3, column=2, padx=0, pady=(0, 15), columnspan=6)
        self.button_login = ctk.CTkButton(self.frame_login, width=220, text="Login", fg_color="#41c269", corner_radius=32,
                                          hover_color="#4F5250", font=("Century Gothic", 18), text_color="#FFFFFF",
                                          command=lambda: login_user(self.entry_user, self.entry_password, self.master.show_home_screen))
        self.button_login.grid(row=4, column=0, padx=30, pady=(15, 5), columnspan=6)
        self.button_register = ctk.CTkButton(self.frame_login, width=110, text="Não possui conta? Cadastre-se", fg_color="transparent",
                                             font=("Century Gothic", 12,), text_color="#FFFFFF", hover=False, command=self.master.show_signup_screen)
        self.button_register.grid(row=5, column=0, padx=30, pady=(5, 30), columnspan=6)

