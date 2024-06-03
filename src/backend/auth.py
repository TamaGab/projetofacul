# src/backend/auth.py
from .database import *
from ui.components.messagebox import show_invalid_password_message, show_invalid_cpf_message, show_missing_info_message, show_existing_email_message, show_invalid_passuser_message, show_nonexisting_email_message
from backend.session import session
import bcrypt

def auth_user(email, senha):
    db_connection, cursor = get_cursor()

    query_user = """
    SELECT u.id, u.nome, u.email, u.senha, a.id AS id_aluno, p.id AS id_professor
    FROM usuarios u 
    LEFT JOIN aluno a ON u.id = a.usuarios_id 
    LEFT JOIN professor p ON u.id = p.usuarios_id
    WHERE u.email = %s
    """
    cursor.execute(query_user, (email,))
    usuario = cursor.fetchone()
    
    if usuario and bcrypt.checkpw(senha.encode('utf-8'), usuario[3].encode('utf-8')):
        session.update(email)
        close_connection(db_connection, cursor)
        if usuario[4]:
            return "aluno"
        elif usuario[5]:
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
        show_invalid_passuser_message()

##########################################################

def cpf_exist(cpf):

    db_connection, cursor = get_cursor()
    query="SELECT * FROM usuarios WHERE cpf = %s"
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

        query_email = "SELECT email FROM usuarios WHERE cpf = %s"
        cursor.execute(query_email, (cpf,))
        exist_email = cursor.fetchone()
        if exist_email is not None and exist_email[0] is not None and exist_email[0].strip() != "":
            show_existing_email_message()
            close_connection(db_connection, cursor)
        else:
            hashed_senha = hash_password(senha)
            query_update = "UPDATE usuarios SET email = %s, senha = %s WHERE cpf = %s"
            cursor.execute(query_update, (email, hashed_senha, cpf))
            db_connection.commit()
            close_connection(db_connection, cursor)
    else:
        show_invalid_cpf_message()
        
        
    
def register_user(entry_cpf, entry_email, entry_senha, entry_confirmesenha, callback):
    cpf = entry_cpf.get().replace(".","").replace("-","")
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
       

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def validate_email(email):
    db_connection, cursor = get_cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    user = cursor.fetchone()
    close_connection(db_connection, cursor)
    return bool(user)

def update_password(screen):
    email = screen.entry_email.get()
    senha = screen.entry_senha.get()
    confirmesenha = screen.entry_confirmesenha.get()
    
    if validate_email(email):
        if email.strip() == "" or senha.strip() == "":
            show_missing_info_message()
        elif senha == confirmesenha:
            db_connection, cursor = get_cursor()
            cursor.execute("UPDATE usuarios SET senha = %s WHERE email = %s", (hash_password(senha), email,))
            db_connection.commit()
            close_connection(db_connection, cursor)
            screen.master.show_login_screen()
        else:
            show_invalid_password_message()
    else:
        show_nonexisting_email_message()
        
def logoff(screen):
    screen.master.show_login_screen()
    session.clear()