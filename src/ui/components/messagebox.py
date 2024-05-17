import CTkMessagebox as ctk

def show_invalid_password_message():
    msgbox = ctk.CTkMessagebox(
        title="Senha Inválida",
        message="As senhas não coincidem.",
        width=300,
        height=150,
        icon="cancel",
        option_1="Tente novamente",
        font=("Century Gothic", 12),
        button_hover_color="#4F5250",
        button_width=100,
        button_height=60,
        button_color="#41c269",
        button_text_color="#FFFFFF",
        justify="center"
    )
    msgbox.mainloop()

def show_invalid_cpf_message():
    msgbox = ctk.CTkMessagebox(
        title="CPF Inválido",
        message="CPF não consta no sistema",
        width=300,
        height=150,
        icon="cancel",
        option_1="Tente novamente",
        font=("Century Gothic", 12),
        button_hover_color="#4F5250",
        button_width=100,
        button_height=60,
        button_color="#41c269",
        button_text_color="#FFFFFF",
        justify="center"
    )
    msgbox.mainloop()

def show_missing_info_message():
    msgbox = ctk.CTkMessagebox(
        title="Informações Inválidas",
        message="Insira as devidas informações.",
        width=300,
        height=150,
        icon="cancel",
        option_1="Tente novamente",
        font=("Century Gothic", 12),
        button_hover_color="#4F5250",
        button_width=100,
        button_height=60,
        button_color="#41c269",
        button_text_color="#FFFFFF",
        justify="center"
    )
    msgbox.mainloop()

def show_existing_email_message():
    msgbox = ctk.CTkMessagebox(message="Este CPF já possui um e-mail cadastrado.",
                               width=300,
                               height=150,
                               title="CPF já cadastrado",
                               icon="cancel",
                               option_1="OK",
                               font=("Century Gothic", 12),
                               button_hover_color="#4F5250",
                               button_width=100,
                               button_height=60,
                               button_color="#41c269",
                               button_text_color="#FFFFFF",
                               justify="center")
    msgbox.mainloop()
    
def show_invalid_passuser_message():
    msgbox = ctk.CTkMessagebox(message="Usuario ou Senha Inválidos",
                               width=300,
                               height=150,
                               title="Falha no Login",
                               icon="cancel",
                               option_1="Tente novamente",
                               font=("Century Gothic", 12),
                               button_hover_color="#4F5250",
                               button_width=100,
                               button_height=60,
                               button_color="#41c269",
                               button_text_color="#FFFFFF",
                               justify="center")
    msgbox.mainloop()