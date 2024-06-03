import customtkinter as ctk
from PIL import Image
import os
from backend.auth import register_user

class SignupScreen:
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

        self.frame_signup = ctk.CTkFrame(self.master, corner_radius=15)
        self.frame_signup.grid(row=0, column=0, padx=(self.master.width-320)//2, pady=(self.master.height-460)//2)

        self.logo_label = ctk.CTkLabel(self.frame_signup, image=self.logo_image, text="")
        self.logo_label.grid(row=0, column=0, padx=50, columnspan=5, pady=(25, 30))

        self.entry_cpf = ctk.CTkEntry(self.frame_signup, width=220, placeholder_text="CPF", font=("Century Gothic", 16))
        self.entry_cpf.grid(row=1, column=0, columnspan=5, padx=30, pady=(15, 15))
        self.entry_cpf.bind("<KeyRelease>", self.format_cpf)
        self.entry_cpf.bind("<Return>", lambda event: self.entry_email.focus_set())
        self.entry_cpf.bind("<Enter>", self.enable_cpf_editing)
        self.entry_cpf.bind("<Button-1>", self.enable_cpf_editing)

        self.entry_email = ctk.CTkEntry(self.frame_signup, width=220, placeholder_text="Email", font=("Century Gothic", 16))
        self.entry_email.grid(row=2, column=0, columnspan=5, padx=30, pady=(15, 15))
        self.entry_email.bind("<Return>", lambda event: self.entry_senha.focus_set())

        self.entry_senha = ctk.CTkEntry(self.frame_signup, width=220, placeholder_text="Senha", show="*", font=("Century Gothic", 16))
        self.entry_senha.grid(row=3, column=0, columnspan=5, padx=30, pady=(15, 15))
        self.entry_senha.bind("<Return>", lambda event: self.entry_confirmesenha.focus_set())

        self.entry_confirmesenha = ctk.CTkEntry(self.frame_signup, width=220, placeholder_text="Confirme sua senha", show="*", font=("Century Gothic", 16))
        self.entry_confirmesenha.grid(row=4, column=0, columnspan=5, padx=30, pady=(15, 15))
        self.entry_confirmesenha.bind("<Return>", lambda event: register_user(self.entry_cpf, self.entry_email, self.entry_senha, self.entry_confirmesenha, self.master.show_login_screen))

        self.button_signup = ctk.CTkButton(self.frame_signup, text="Cadastrar", width=220, height=35, fg_color="#41c269",
                                           corner_radius=32, hover_color="#4F5250", text_color="#FFFFFF", font=("Century Gothic", 16),
                                           command=lambda: register_user(self.entry_cpf, self.entry_email, self.entry_senha, self.entry_confirmesenha, self.master.show_login_screen))
        self.button_signup.grid(row=5, column=0, columnspan=5, pady=(30, 5))
        self.button_login = ctk.CTkButton(self.frame_signup, text="Já possui uma conta? Conecte-se", font=("Century Gothic", 12),
                                          fg_color="transparent", text_color="#FFFFFF", command=self.master.show_login_screen, hover=False)
        self.button_login.grid(row=6, column=0, columnspan=5, pady=(5, 30))

    def format_cpf(self, event=None):
        cpf = self.entry_cpf.get()
        digits = [d for d in cpf if d.isdigit()]

        if len(digits) > 11:
            digits = digits[:11]

        formatted_cpf = ""
        for i, digit in enumerate(digits):
            if i in [3, 6]:
                formatted_cpf += "."
            elif i == 9:
                formatted_cpf += "-"
            formatted_cpf += digit

        self.entry_cpf.delete(0, "end")
        self.entry_cpf.insert(0, formatted_cpf)

        if len(digits) >= 11:
            self.entry_cpf.configure(state="disabled")
            self.entry_cpf.unbind("<KeyRelease>")
        else:
            self.entry_cpf.configure(state="normal")

    def enable_cpf_editing(self, event=None):
        self.entry_cpf.configure(state="normal")
        self.entry_cpf.bind("<KeyRelease>", self.format_cpf)
