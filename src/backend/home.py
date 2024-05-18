# src/backend/home.py
from backend.database import *

buttons_aluno = {
    "0": {
        "url_imagem": "/../../../images/logostar.png",
        "nome": "logo"
    },
    "1": {
        "url_imagem": "/../../../images/user.png",
        "nome": "Alunos"
    },
    "2": {
        "url_imagem": "/../../../images/notas.png",
        "nome": "Notas"
    },
    "3": {
        "url_imagem": "/../../../images/calendar.png",
        "nome": "Matérias"
    },
}

buttons_professor = {
    "0": {
        "url_imagem": "/../../../images/logostar.png",
        "nome": "logo"
    },
    "1": {
        "url_imagem": "/../../../images/user.png",
        "nome": "Curso Lecionado"
    },
    "2": {
        "url_imagem": "/../../../images/notas.png",
        "nome": "Alunos Lecionado"
    },
}


def get_name(user_entry):
    email = user_entry.get()
    db_connection, cursor = get_cursor()
    
    query = "SELECT nome FROM aluno WHERE email = %s"
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    
    close_connection(db_connection, cursor)
    
    if result:
        return result[2]  
    else:
        return None 







def load_home_data():
    pass