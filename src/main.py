import customtkinter as ctk
from ui.login_screen import LoginScreen
from ui.signup_screen import SignupScreen
from ui.home_screen import HomeScreen
from ui.recoverpass_screen import RecoverPassScreen

ctk.set_appearance_mode("dark")

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
        RecoverPassScreen(self)
        
    def show_home_screen(self, user_type):
        self._clear_screen()
        HomeScreen(self, user_type)

    def _clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
