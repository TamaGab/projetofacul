import customtkinter as ctk
from ui.login_screen import LoginScreen
from ui.signup_screen import SignupScreen
from ui.home_screen import HomeScreen
from ui.recoverpass_screen import RecoverPassScreen
from PIL import Image
import os

ctk.set_appearance_mode("dark")

import os

import os

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Cruzeiro do Sul")
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}+0+0")
        
        self.show_login_screen()
        
    def show_login_screen(self):
        self._clear_screen()
        LoginScreen(self)

    def show_signup_screen(self):
        self._clear_screen()
        SignupScreen(self)
        
    def show_recoverpass_screen(self):
        self._clear_screen()
        r = RecoverPassScreen(self)
        self.add_back_button(r.frame_recover, self.show_login_screen)
        
    def show_home_screen(self, user_type):
        self._clear_screen()
        HomeScreen(self, user_type)

    def _clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def add_back_button(self, widget, command):
        image_path = os.path.join(os.path.dirname(__file__), "..", "images", "back_button.png")
        back_button = ctk.CTkButton(widget, width=30, text="", hover=False, fg_color="transparent", image=ctk.CTkImage(Image.open(image_path), size=(35,35)), command=command)
        back_button.place(rely=0.05, relx=0.07, anchor="center")

if __name__ == "__main__":
    app = App()
    app.mainloop()


