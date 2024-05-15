import customtkinter as ctk
from PIL import Image
import os
from functions import *

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Cruzeiro do Sul")
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}+0+0")

        self.current_path = os.path.dirname(os.path.realpath(__file__))

        self.bg_image = ctk.CTkImage(Image.open(self.current_path + "/images/pattern.png"),
                                     size=(self.width, self.height))
        self.logo_image = ctk.CTkImage(dark_image=Image.open("images/logo.png"), size=(220, 55))

        self.show_login_screen()

    def show_login_screen(self):
        self.clear_screen()

        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.place(relwidth=1, relheight=1)

        self.frame_login = ctk.CTkFrame(self, corner_radius=15)
        self.frame_login.grid(row=0, column=0, padx=(self.width-320)//2, pady=(self.height-360)//2)

        self.logo_label = ctk.CTkLabel(self.frame_login, text="", image=self.logo_image)
        self.logo_label.grid(row=0, column=0, padx=50, pady=(30, 30), columnspan=6)

        self.entry_user = ctk.CTkEntry(self.frame_login, placeholder_text="Usuario", width=220, font=("Century Gothic", 16))
        self.entry_user.grid(row=1, column=0, padx=30, pady=(15, 15), columnspan=6)

        self.entry_password = ctk.CTkEntry(self.frame_login, placeholder_text="Senha", width=220, show="*", font=("Century Gothic", 16))
        self.entry_password.grid(row=2, column=0, padx=30, pady=(15, 5), columnspan=6)

        self.entry_user.bind("<Return>", lambda event: self.entry_password.focus_set())
        self.entry_password.bind("<Return>", lambda event: loginButton(self.entry_user, self.entry_password, self.show_home_screen))

        self.button_fpassword = ctk.CTkButton(self.frame_login, width=110, text="Esqueceu a senha?", fg_color="transparent",
                                              font=("Century Gothic", 12,), text_color="#FFFFFF", hover=False, command=self.forgot_password)
        self.button_fpassword.grid(row=3, column=2, padx=0, pady=(0, 15), columnspan=6)

        self.button_login = ctk.CTkButton(self.frame_login, width=220, text="Login", fg_color="#41c269", corner_radius=32,
                                          hover_color="#4F5250", font=("Century Gothic", 18), text_color="#FFFFFF",
                                          command=lambda: loginButton(self.entry_user, self.entry_password, self.show_home_screen))
        self.button_login.grid(row=4, column=0, padx=30, pady=(15, 5), columnspan=6)

        self.button_register = ctk.CTkButton(self.frame_login, width=110, text="Não possui conta? Cadastre-se", fg_color="transparent",
                                             font=("Century Gothic", 12,), text_color="#FFFFFF", hover=False, command=self.show_signup_screen)
        self.button_register.grid(row=5, column=0, padx=30, pady=(5, 30), columnspan=6)


    def show_signup_screen(self):
        self.clear_screen()

        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image_label.place(relwidth=1, relheight=1)

        self.frame_signup = ctk.CTkFrame(self, corner_radius=15)
        self.frame_signup.grid(row=0, column=0, padx=(self.width-320)//2, pady=(self.height-460)//2)

        self.logo_image_large = ctk.CTkImage(dark_image=Image.open("images/logo.png"), size=(220, 55))

        self.logo_label = ctk.CTkLabel(self.frame_signup, image=self.logo_image_large, text="")
        self.logo_label.grid(row=0, column=0, padx=50, columnspan=5, pady=(30, 30))

        self.entry_nome = ctk.CTkEntry(self.frame_signup, width=220, placeholder_text="Nome Completo", font=("Century Gothic", 16))
        self.entry_nome.grid(row=1, column=0, columnspan=5, padx=30, pady=(15, 5))

        self.entry_email = ctk.CTkEntry(self.frame_signup, width=220, placeholder_text="Email", font=("Century Gothic", 16))
        self.entry_email.grid(row=2, column=0, columnspan=5, padx=30, pady=(15, 5))

        self.entry_senha = ctk.CTkEntry(self.frame_signup, width=220, placeholder_text="Senha", show="*", font=("Century Gothic", 16))
        self.entry_senha.grid(row=3, column=0, columnspan=5, padx=30, pady=(15, 5))

        self.entry_confirmesenha = ctk.CTkEntry(self.frame_signup, width=220, placeholder_text="Confirme sua senha", show="*", font=("Century Gothic", 16))
        self.entry_confirmesenha.grid(row=4, column=0, columnspan=5, padx=30, pady=(15, 5))

        self.button_signup = ctk.CTkButton(self.frame_signup, text="Cadastrar", width=220, height=35, fg_color="#41c269",
                                           corner_radius=32, hover_color="#4F5250", text_color="#FFFFFF", font=("Century Gothic", 16), command=self.register_button)
        self.button_signup.grid(row=5, column=0, columnspan=5, pady=(15, 15))

        self.label_login = ctk.CTkLabel(self.frame_signup, text="Já possui uma conta? Conecte-se", font=("Century Gothic", 12),
                                        fg_color="transparent", text_color="#FFFFFF")
        self.label_login.grid(row=6, column=0, columnspan=5, pady=(5, 5))

        self.button_login = ctk.CTkButton(self.frame_signup, text="Conectar", width=220, height=35, fg_color="#4F5250",
                                          corner_radius=32, hover_color="#41c269", text_color="#FFFFFF", font=("Century Gothic", 16),
                                          command=self.show_login_screen)
        self.button_login.grid(row=7, column=0, columnspan=5, pady=(5, 45))


    def show_home_screen(self):
        

        self.clear_screen()

        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image_label.place(relwidth=1, relheight=1)

        self.frame_menu = ctk.CTkFrame(self, width=50, height=self.height, corner_radius=0)
        self.frame_menu.grid(row=0, column=0, sticky="ns")
        self.frame_menu.grid_propagate(False)

        self.logo_label = ctk.CTkLabel(self.frame_menu, text="", image=self.logo_image)
        self.logo_label.grid(row=0, column=0, padx=50, pady=(30, 30))

        user_image = ctk.CTkImage(dark_image=Image.open("images/user.png"))
        nota_image = ctk.CTkImage(dark_image=Image.open("images/notas.png"))
        materia_image = ctk.CTkImage(dark_image=Image.open("images/calendar.png"))

        self.user_button = ctk.CTkButton(self.frame_menu, width=180, height=40, text="Aluno", fg_color="transparent", corner_radius=6,
                                        hover_color="#4F5250", font=("Century Gothic", 18), text_color="#FFFFFF",
                                        image=user_image, anchor='w')
        self.user_button.grid(row=1, column=0, padx=10, pady=(15, 15))

        self.user_button2 = ctk.CTkButton(self.frame_menu, width=180, height=40, text="Notas", fg_color="transparent", corner_radius=6,
                                        hover_color="#4F5250", font=("Century Gothic", 18), text_color="#FFFFFF",
                                        image=nota_image, anchor='w')
        self.user_button2.grid(row=2, column=0, padx=10, pady=(15, 15))

        self.user_button3 = ctk.CTkButton(self.frame_menu, width=180, height=40, text="Matérias", fg_color="transparent", corner_radius=6,
                                        hover_color="#4F5250", font=("Century Gothic", 18), text_color="#FFFFFF",
                                        image=materia_image, anchor='w')
        self.user_button3.grid(row=3, column=0, padx=10, pady=(15, 15))

        # Ensuring the frame_menu expands to fill the vertical space
        self.rowconfigure(0, weight=1)

        # Hover effect for sidebar
        for widget in [self.frame_menu, self.user_button, self.user_button2, self.user_button3, self.logo_label]:
            widget.bind("<Enter>", lambda event, w=widget: expand_sidebar(event))
            widget.bind("<Leave>", lambda event, w=widget: shrink_sidebar(event))
            
        def expand_sidebar(event):
            self.frame_menu.configure(width=200)  # Adjust the width as needed for expansion
            self.frame_menu.grid_propagate(True)

        def shrink_sidebar(event):
            self.frame_menu.configure(width=50)  # Set back to original width
            self.frame_menu.grid_propagate(False)
            

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def forgot_password(self):
        # Implement forgot password functionality
        pass

    def register_button(self):
        # Implement register button functionality
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()
