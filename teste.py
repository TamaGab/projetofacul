import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")



class App(customtkinter.CTk):
      
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Cruzeiro do Sul")
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}+-9+-9")

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/images/pattern.png"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)
        self.logo = customtkinter.CTkImage(dark_image=Image.open("images/logo.png"),  size=(220, 55))

        # create login frame
        self.frame_login = customtkinter.CTkFrame(self, width=320, height=360, corner_radius=15)
        self.frame_login.grid(row=0, column=0, columnspan=6)
        
        self.logo = customtkinter.CTkLabel(self.frame_login, text="", image=self.logo)
        self.logo.grid(row=0, column=0, padx=50, pady=(30,30), columnspan=6)

        self.entry_user = customtkinter.CTkEntry(self.frame_login, placeholder_text="Usuario", width=220, font=("Century Gothic", 16))
        self.entry_user.grid(row=1, column=0, padx=30, pady=(15, 15), columnspan=6)

        self.entry_password = customtkinter.CTkEntry(self.frame_login, placeholder_text="Senha", width=220, show="*", font=("Century Gothic", 16))
        self.entry_password.grid(row=2, column=0, padx=30, pady=(15, 5), columnspan=6)

        self.button_fpassword = customtkinter.CTkButton(self.frame_login, width=110, text="Esqueceu a senha?", fg_color="transparent", font=("Century Gothic", 12,), text_color="#FFFFFF", hover=False)
        self.button_fpassword.grid(row=3, column=2, padx=0, pady=(0, 15), columnspan=6)

        self.button_login = customtkinter.CTkButton(self.frame_login, width=220, text="Login", fg_color="#41c269", corner_radius=32, hover_color="#4F5250",font=("Century Gothic", 18), text_color="#FFFFFF")
        self.button_login.grid(row=4, column=0, padx=30, pady=(15, 5), columnspan=6)
        
        self.button_register = customtkinter.CTkButton(self.frame_login, width=110, text="Não possui conta? Cadastre-se", fg_color="transparent", font=("Century Gothic", 12,), text_color="#FFFFFF", hover=False)
        self.button_register.grid(row=5, column=0, padx=30, pady=(5, 30), columnspan=6)




        # create main frame
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_label = customtkinter.CTkLabel(self.main_frame, text="CustomTkinter\nMain Page",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        self.back_button = customtkinter.CTkButton(self.main_frame, text="Back", command=self.back_event, width=200)
        self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))

    def login_event(self):
        print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())

        self.login_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame

    def back_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame


if __name__ == "__main__":
    app = App()
    app.mainloop()