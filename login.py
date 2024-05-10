import customtkinter, tkinter
from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
from CTkMessagebox import CTkMessagebox
from home import appHome
messagebox_opened = False

def verify(usuario, senha):
    # Retorne True se as credenciais estiverem corretas, caso contrário, False
    pass

def esqueci_senha():
    # Aqui você pode adicionar o código para lidar com a situação em que o usuário esqueceu a senha
    pass


# defini uma funçao messagebox_opened como global para seja possivel bloquear as solicitaçoes da funçao loginButton quando a mesma for aberta
# quando messagebox_opened = False, quer dizer que a msg_box nao esta aberta possibilitanto o chamado da funçao loginButton
# quando messagebox_opened = True, no caso quando o login do usuario falha, nao é possivel solicitar a funçao loginButton ate o fechamento da msg_box 

def loginButton(event):
    global messagebox_opened

    def on_messagebox_closed(event): # reseta o bool messagebox_opened para false, permitindo a funçao loginButton ser chamada novamente.
        global messagebox_opened
        messagebox_opened = False

    if not messagebox_opened:
        usuario = entry_user.get()
        senha = entry_password.get()
        if usuario == "gabriel" and senha == "123": # <<< ---  SUBSTITUIR POR FUNÇAO QUE DETECTA SE O USUARIO ESTA CADASTRADO NO BANCO. (def verify()) #
            app_login.destroy()
            appHome()
        else:
            messagebox_opened = True
            msg_box = CTkMessagebox(master=login_frame, title="Erro", message="Falha no login", icon="cancel", cancel_button="cross", width=300, height=100, button_width=100, justify="center", corner_radius=18, icon_size=(30, 30), fade_in_duration=1)
            print(usuario)
            print(senha)
            msg_box.bind("<Destroy>", on_messagebox_closed) # quando o widget msg_box for destruido, aplica o evento(funçao) on_messagebox_closed.


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
app_login = customtkinter.CTk()
app_login.title("Login")
app_login.geometry("600x440")

img1 = customtkinter.CTkImage(Image.open("images/pattern.png"), size=(app_login.winfo_screenwidth(), app_login.winfo_screenheight()))
img2 = customtkinter.CTkImage(dark_image=Image.open("images/logo.png"),  size=(220, 55))


background = customtkinter.CTkLabel(master=app_login, image=img1)
background.pack()

login_frame = customtkinter.CTkFrame(master=app_login, width=320, height=360, corner_radius=15)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

entry_user = customtkinter.CTkEntry(master=login_frame, placeholder_text="Usuario", width=220, font=("Century Gothic", 16))
entry_user.place(x=50, y=135)

entry_password = customtkinter.CTkEntry(master=login_frame, placeholder_text="Senha", width=220, show="*", font=("Century Gothic", 16))
entry_password.place(x=50, y=190)

button_fpassword = customtkinter.CTkButton(master=login_frame, width=110, text="Esqueci a senha", fg_color="transparent", font=("Century Gothic", 12,), text_color="#FFFFFF", hover=False)
button_fpassword.place(x=165, y=225)

button_login = customtkinter.CTkButton(master=login_frame, width=220, text="Login", fg_color="#41c269", corner_radius=32, hover_color="#4F5250",font=("Century Gothic", 18), text_color="#FFFFFF")
button_login.place(x=50, y=270)

button_login.bind("<Button-1>", loginButton)
entry_password.bind("<Return>", loginButton)
entry_user.bind("<Return>", lambda event: entry_password.focus_set())



logo = customtkinter.CTkLabel(master=login_frame, text="", image=img2)
logo.place(relx=0.5, rely=0.19, anchor="center")

app_login.mainloop()