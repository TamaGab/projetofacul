# src/backend/home.py
from backend.database import get_cursor, close_connection


def professordisciplinas(email):
    db_connection, cursor = get_cursor()
    query = """
    SELECT d.nome AS disciplina_nome
    FROM usuarios u
    JOIN professor p ON u.id = p.usuarios_id
    JOIN disciplinas d ON p.id = d.professor_id
    WHERE u.email = %s;
    """
    cursor.execute(query, (email,))
    results = cursor.fetchall()
    close_connection(db_connection, cursor)
    return [results[0] for results in results]

def professoralunos(email):
    db_connection, cursor = get_cursor()
    query = """
    SELECT u_aluno.nome AS aluno_nome
    FROM usuarios u_professor
    INNER JOIN professor ON u_professor.id = professor.usuarios_id
    INNER JOIN disciplinas ON professor.id = disciplinas.professor_id
    INNER JOIN curso_disciplinas ON disciplinas.id = curso_disciplinas.disciplinas_id
    INNER JOIN cursos ON curso_disciplinas.cursos_id = cursos.id
    INNER JOIN matriculas ON cursos.id = matriculas.cursos_id
    INNER JOIN aluno ON matriculas.aluno_id = aluno.id
    INNER JOIN usuarios u_aluno ON aluno.usuarios_id = u_aluno.id
    WHERE u_professor.email = %s
    """
    cursor.execute(query, (email,))
    results = cursor.fetchall()
    alunos = []
    for row in results:
        aluno_nome = row[0]
        alunos.append(aluno_nome)
    close_connection(db_connection, cursor)
    return alunos



def load_home_data():
    pass