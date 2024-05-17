# src/backend/auth.py
from .database import *
from ui.components.messagebox import show_invalid_password_message, show_invalid_cpf_message, show_missing_info_message, show_existing_email_message, show_invalid_passuser_message


def auth_user(email, senha):
    
    db_connection, cursor = get_cursor()

    query_aluno = "SELECT * FROM aluno WHERE email = %s"
    cursor.execute(query_aluno, (email,))
    aluno = cursor.fetchone()  

    if aluno:  
        if aluno[4] == senha:  
            close_connection(db_connection, cursor)
            return "aluno"
    else:
        query_professor = "SELECT * FROM professor WHERE email = %s"
        cursor.execute(query_professor, (email,))
        professor = cursor.fetchone()  

        if professor: 
            if professor[4] == senha:  
                close_connection(db_connection, cursor)
                return "professor"

    close_connection(db_connection, cursor)
    return None

def login_user(entry_user, entry_password, callback):
    user = entry_user.get()
    password = entry_password.get()
    user_type = auth_user(user, password)
    if user_type:
        callback(user_type)
    else:
        msgbox = show_invalid_passuser_message()

##########################################################

def cpf_exist(cpf):

    db_connection, cursor = get_cursor()
    
    query="SELECT * FROM aluno WHERE cpf = %s"
    cursor.execute(query, (cpf,))
    cpf = cursor.fetchone()

    close_connection(db_connection, cursor)
    
    if cpf:
        return True
    else:
        return False
   
def add_infos(validatecpf, email, senha, cpf):
    if validatecpf:
        db_connection, cursor = get_cursor()

        query_email = "SELECT email FROM aluno WHERE cpf = %s"
        cursor.execute(query_email, (cpf,))
        exist_email = cursor.fetchone()

        if exist_email[0] is None:
        
            query_update = "UPDATE aluno SET email = %s, senha = %s WHERE cpf = %s"
            cursor.execute(query_update, (email, senha, cpf))
            db_connection.commit()
            close_connection(db_connection, cursor)
        else:
            show_existing_email_message()        
            close_connection(db_connection, cursor)
    else:
        show_invalid_cpf_message()

        
        
    
def register_user(entry_cpf, entry_email, entry_senha, entry_confirmesenha, callback):
    cpf = entry_cpf.get()
    email = entry_email.get()
    senha = entry_senha.get()
    confirmesenha = entry_confirmesenha.get()

    validatecpf = cpf_exist(cpf)
    if validatecpf:
        if email.strip() == "" or senha.strip() == "":
            show_missing_info_message()
        elif senha == confirmesenha:
            add_infos(validatecpf, email, senha, cpf)
            callback()
        else:
            show_invalid_password_message()
    else:
        show_invalid_cpf_message()
       
   
def recover_password():
    pass