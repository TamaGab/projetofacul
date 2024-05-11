import customtkinter
from PIL import Image
from customtkinter import CTkButton, CTkEntry, CTkLabel, CTkFrame
from tkinter import messagebox

def cadastrar_aluno():
    # Obter os dados dos campos de entrada
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()

    # Aqui você pode adicionar a lógica para salvar os dados no banco de dados

    # Exemplo simples de exibição dos dados
    messagebox.showinfo("Cadastro de Aluno", f"Aluno cadastrado:\nNome: {nome}\nEmail: {email}\nSenha: {senha}\nCEP:")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app_signup = customtkinter.CTk()
app_signup.title("Cadastro de Aluno")
app_signup.geometry("{0}x{1}+0+0".format(app_signup.winfo_screenwidth(), app_signup.winfo_screenheight()))


bgimage = customtkinter.CTkImage(Image.open("images/pattern.png"), size=(app_signup.winfo_screenwidth(), app_signup.winfo_screenheight()))
logo = customtkinter.CTkImage(dark_image=Image.open("images/logo.png"), size=(310, 75))


label_bg = customtkinter.CTkLabel(master=app_signup, image=bgimage, text="")
label_bg.grid(row=0, column=0)

frame_signup = CTkFrame(master=app_signup, corner_radius=32)
frame_signup.grid(row=0, column=0)  



label_logo = customtkinter.CTkLabel(master=frame_signup, image=logo, text="")
label_logo.grid(row=0, column=0, padx= 50, columnspan=5, pady=(30, 60))  

entry_nome = CTkEntry(master=frame_signup, width=300, placeholder_text="Nome Completo",font=("Century Gothic", 16)) 
entry_nome.grid(row=1, column=0, columnspan=5, padx=20, pady=(0, 5))  

entry_email = CTkEntry(master=frame_signup, width=300, placeholder_text="Email",font=("Century Gothic", 16)) 
entry_email.grid(row=2, column=0, columnspan=5, padx=20, pady=(15, 5)) 

entry_senha = CTkEntry(master=frame_signup, width=300, placeholder_text="Senha", show="*",font=("Century Gothic", 16))  
entry_senha.grid(row=3, column=0, columnspan=5, padx=20, pady=(15, 5))  

entry_confirmesenha = CTkEntry(master=frame_signup, width=300, placeholder_text="Confirme sua senha", show="*",font=("Century Gothic", 16))  
entry_confirmesenha.grid(row=4, column=0, columnspan=5, padx=20, pady=(15, 55))  

button_signup = CTkButton(master=frame_signup, text="Cadastrar", width=300, height=35, fg_color="#41c269",
                             corner_radius=32, hover_color="#4F5250", text_color="#FFFFFF",
                             command=cadastrar_aluno, font=("Century Gothic", 16))
button_signup.grid(row=5, column=0, columnspan=5, pady=(15, 15))  

label_login = CTkLabel(master=frame_signup, text="Já possui uma conta? Conecte-se", font=("Century Gothic", 12), fg_color="transparent", text_color="#FFFFFF")
label_login.grid(row=7, column=0, columnspan=5, pady=(5, 15))

button_login = CTkButton(master=frame_signup, text="Conectar", width=300, height=35, fg_color="#4F5250",
                             corner_radius=32, hover_color="#41c269", text_color="#FFFFFF",
                              font=("Century Gothic", 16))
button_login.grid(row=8, column=0, columnspan=5, pady=(0, 50))


app_signup.mainloop()