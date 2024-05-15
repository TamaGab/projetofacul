from customtkinter import *
from CTkMessagebox import *
messagebox_opened = False


 
def forgot_password():
    pass

def loginButton(user, password, event1):
    usuario = user.get()
    senha = password.get()
    if usuario == "gabriel" and senha == "123":
        event1()
    else:
        print("Usuário ou senha incorretos")
     