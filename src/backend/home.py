# src/backend/home.py
from backend.database import get_cursor, close_connection


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
    SELECT u_a.nome AS aluno_nome, d.nome AS disciplina_nome FROM usuarios u_p
    INNER JOIN professor p ON u_p.id = p.usuarios_id
    INNER JOIN disciplinas d ON p.id = d.professor_id
    INNER JOIN curso_disciplinas cd ON d.id = cd.disciplinas_id
    INNER JOIN cursos c ON cd.cursos_id = c.id
    INNER JOIN matriculas m ON c.id = m.cursos_id
    INNER JOIN aluno a ON m.aluno_id = a.id
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
    SELECT nome, carga FROM disciplinas d
    JOIN curso_disciplinas cd ON d.id = cd.disciplinas_id
    JOIN matriculas m ON cd.cursos_id = m.cursos_id
    JOIN aluno a ON m.aluno_id = a.id
    WHERE a.usuarios_id = %s    
    """
    cursor.execute(query, (user_id,))
    results = cursor.fetchall()
    close_connection(db_connection, cursor)
    return results


def load_home_data():
    pass