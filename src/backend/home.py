# src/backend/home.py
from backend.database import get_cursor, close_connection
from ui.components.messagebox import show_invalid_nota
import customtkinter as ctk

def get_professor_disciplina(email):
    db_connection, cursor = get_cursor()
    query = """
    SELECT d.nome AS disciplina_nome FROM usuarios u
    JOIN professor p ON u.id = p.usuarios_id
    JOIN disciplinas d ON p.id = d.professor_id
    WHERE u.email = %s;
    """
    cursor.execute(query, (email,))
    results = cursor.fetchall()
    close_connection(db_connection, cursor)
    return [results[0] for results in results]

def get_professor_aluno(email):
    db_connection, cursor = get_cursor()
    
    query = """
    SELECT a.id AS aluno_id, u_a.nome AS aluno_nome, d.id AS disciplina_id, d.nome AS disciplina_nome, na.nota AS aluno_nota 
    FROM usuarios u_p
    INNER JOIN professor p ON u_p.id = p.usuarios_id
    INNER JOIN disciplinas d ON p.id = d.professor_id
    INNER JOIN curso_disciplinas cd ON d.id = cd.disciplinas_id
    INNER JOIN cursos c ON cd.cursos_id = c.id
    INNER JOIN matriculas m ON c.id = m.cursos_id
    INNER JOIN aluno a ON m.aluno_id = a.id
    LEFT JOIN nota_alunos na ON m.aluno_id = na.aluno_id AND d.id = na.disciplinas_id
    INNER JOIN usuarios u_a ON a.usuarios_id = u_a.id
    WHERE u_p.email = %s
    """
    
    cursor.execute(query, (email,))
    results = cursor.fetchall()
    close_connection(db_connection, cursor)
    return results

def get_course_name(user_id):
    db_connection, cursor = get_cursor()

    query = """
    SELECT c.nome FROM aluno a
    JOIN matriculas m ON a.id = m.aluno_id
    JOIN cursos c ON m.cursos_id = c.id
    WHERE a.usuarios_id = %s
    """
    cursor.execute(query, (user_id,))
    curso_name = cursor.fetchone()
    
    close_connection(db_connection, cursor)
    
    return curso_name[0] if curso_name else None

def get_course_carga(user_id):
    db_connection, cursor = get_cursor()

    query = """
    SELECT c.carga FROM aluno a
    JOIN matriculas m ON a.id = m.aluno_id
    JOIN cursos c ON m.cursos_id = c.id
    WHERE a.usuarios_id = %s
    """
    cursor.execute(query, (user_id,))
    curso_carga = cursor.fetchone()
    
    close_connection(db_connection, cursor)
    
    return curso_carga[0] if curso_carga else None

def get_course_coordenador(user_id):
    db_connection, cursor = get_cursor()

    query = """
    SELECT u.nome AS nome_coordenador FROM aluno a
    JOIN matriculas m ON a.id = m.aluno_id
    JOIN cursos c ON m.cursos_id = c.id
    JOIN professor p ON c.coordenador_id = p.id
    JOIN usuarios u ON p.usuarios_id = u.id
    WHERE a.usuarios_id = %s
    """
    cursor.execute(query, (user_id,))
    coordenador_curso = cursor.fetchone()
    
    close_connection(db_connection, cursor)
    
    return coordenador_curso[0] if coordenador_curso else None

def get_aluno_nota(user_id):
    db_connection, cursor = get_cursor()

    query = """
    SELECT nota, d.nome FROM nota_alunos na
    JOIN aluno a ON a.id = na.aluno_id
    JOIN disciplinas d ON d.id = na.disciplinas_id
    WHERE a.usuarios_id = %s
    """
    cursor.execute(query, (user_id,))
    results = cursor.fetchall()
    close_connection(db_connection, cursor)
    return results
        

def get_disciplina_carga(user_id):
    db_connection, cursor = get_cursor()
    
    query = """
    SELECT nome AS nome_disciplina, carga AS disciplina_carga FROM disciplinas d
    JOIN curso_disciplinas cd ON d.id = cd.disciplinas_id
    JOIN matriculas m ON cd.cursos_id = m.cursos_id
    JOIN aluno a ON m.aluno_id = a.id
    WHERE a.usuarios_id = %s    
    """
    cursor.execute(query, (user_id,))
    results = cursor.fetchall()
    close_connection(db_connection, cursor)
    return results

def add_nota(nota, aluno_id, disciplina_id):
    db_connection, cursor = get_cursor()

    query = """
    INSERT INTO nota_alunos (nota, aluno_id, disciplinas_id)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (nota, aluno_id, disciplina_id))
    db_connection.commit()
    close_connection(db_connection, cursor)


def save_and_destroy(homewidget, nota, aluno_id, disciplina_id):
    nota = float(nota.replace(",", "."))
    if nota <= 10:
        add_nota(nota, aluno_id, disciplina_id)
        homewidget.current_toplevel.destroy()
        homewidget.data_att()
    else:
        show_invalid_nota()
 
def format_nota(event):
    entry = event.widget
    grade = ''.join(c for c in entry.get() if c.isdigit())

    if len(grade) >= 2:
        grade = grade[:2] + '.' + grade[2:]

    if len(grade) == 3 and grade[2] == '.':
        grade = grade[:2]

    entry.delete(0, "end")
    entry.insert(0, grade[:5])

    entry.configure(state="disabled" if len(grade) >= 5 else "normal")
    if len(grade) < 5:
        entry.bind("<KeyRelease>", format_nota)

def enable_nota_editing(event):
    event.widget.configure(state="normal")
    event.widget.bind("<KeyRelease>", format_nota)
    
    
def load_home_data():
    pass