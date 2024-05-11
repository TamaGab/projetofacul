import customtkinter, tkinter
from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
from CTkMessagebox import CTkMessagebox
from home import appHome
import mysql.connector
messagebox_opened = False

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="gordoidiota123",
        database="faculdade"
    )

def verify(usuario, senha):
    # Conecta ao banco de dados
    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Consulta SQL para verificar as credenciais
    query = "SELECT * FROM aluno WHERE id = %s AND senha = %s"
    cursor.execute(query, (usuario, senha))

    # Obtém o resultado da consulta
    resultado = cursor.fetchone()

    # Fecha a conexão com o banco de dados
    cursor.close()
    conexao.close()

    # Retorna True se as credenciais estiverem corretas, caso contrário, False
    return resultado is not None

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
        if verify(usuario, senha): # <<< ---  SUBSTITUIR POR FUNÇAO QUE DETECTA SE O USUARIO ESTA CADASTRADO NO BANCO. (def verify()) #
            app_login.destroy()
            appHome()
        else:
            messagebox_opened = True
            msg_box = CTkMessagebox(master=app_login, title="Erro", message="Falha no login", icon="cancel", cancel_button="cross", width=300, height=100, button_width=100, justify="center", corner_radius=18, icon_size=(30, 30), fade_in_duration=1)
            print(usuario)
            print(senha)
            msg_box.bind("<Destroy>", on_messagebox_closed) # quando o widget msg_box for destruido, aplica o evento(funçao) on_messagebox_closed.

    
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
app_login = customtkinter.CTk()
app_login.title("Login")
app_login.geometry("580x470+630+270")
app_login.resizable(False, False)

img1 = customtkinter.CTkImage(Image.open("images/pattern.png"), size=(580,470))
img2 = customtkinter.CTkImage(dark_image=Image.open("images/logo.png"),  size=(220, 55))


bg = customtkinter.CTkLabel(master=app_login, image=img1)
bg.pack()

frame_login = customtkinter.CTkFrame(master=app_login, width=320, height=360, corner_radius=15)
frame_login.place(relx=0.5, rely=0.5, anchor="center")

entry_user = customtkinter.CTkEntry(master=frame_login, placeholder_text="Usuario", width=220, font=("Century Gothic", 16))
entry_user.place(x=50, y=135)

entry_password = customtkinter.CTkEntry(master=frame_login, placeholder_text="Senha", width=220, show="*", font=("Century Gothic", 16))
entry_password.place(x=50, y=190)

button_register = customtkinter.CTkButton(master=frame_login, width=110, text="Não possui conta? Cadastre-se", fg_color="transparent", font=("Century Gothic", 12,), text_color="#FFFFFF", hover=False)
button_register.place(x=45, y=304)

button_fpassword = customtkinter.CTkButton(master=frame_login, width=110, text="Esqueceu a senha?", fg_color="transparent", font=("Century Gothic", 12,), text_color="#FFFFFF", hover=False)
button_fpassword.place(x=165, y=225)

button_login = customtkinter.CTkButton(master=frame_login, width=220, text="Login", fg_color="#41c269", corner_radius=32, hover_color="#4F5250",font=("Century Gothic", 18), text_color="#FFFFFF")
button_login.place(x=50, y=270)

button_login.bind("<Button-1>", loginButton)
entry_password.bind("<Return>", loginButton)
entry_user.bind("<Return>", lambda event: entry_password.focus_set())



logo = customtkinter.CTkLabel(master=frame_login, text="", image=img2)
logo.place(relx=0.5, rely=0.19, anchor="center")

app_login.mainloop()
    
    
