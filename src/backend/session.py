from .database import *

class AlunoSession:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AlunoSession, cls).__new__(cls)
            cls._instance.logged_id = None
            cls._instance.logged_cpf = None
            cls._instance.logged_name = None
            cls._instance.logged_email = None
            cls._instance.logged_cep = None
            cls._instance.logged_curso = None
            cls._instance.logged_cargacurso = None
            cls._instance.logged_coordenadorcurso = None
            

        return cls._instance

    def update(self, email):
        db_connection, cursor = get_cursor()

        user_query = """
        SELECT * FROM usuarios
        WHERE email = %s
        """
        cursor.execute(user_query, (email,))
        user_info = cursor.fetchone()

        if user_info:
            self.logged_id = user_info[0]
            self.logged_cpf = user_info[1]
            self.logged_name = user_info[2]
            self.logged_email = user_info[3]
            self.logged_cep = user_info[5]

           
            curso_query = """
            SELECT cursos_id FROM matriculas
            WHERE aluno_id = %s
            """
            cursor.execute(curso_query, (self.logged_id,))
            curso_id = cursor.fetchone()

            if curso_id:
                
                curso_info_query = """
                SELECT c.nome, c.carga, u.nome AS nome_coordenador
                FROM cursos c
                JOIN professor p ON c.coordenador_id = p.id
                JOIN usuarios u ON p.usuarios_id = u.id
                WHERE c.id = %s
                """
                cursor.execute(curso_info_query, (curso_id[0],))
                curso_info = cursor.fetchone()

                if curso_info:
                    self.logged_curso = curso_info[0]
                    self.logged_cargacurso = curso_info[1]
                    self.logged_coordenadorcurso = curso_info[2]

        close_connection(db_connection, cursor)
        
        
        
        
class ProfessorSession:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ProfessorSession, cls).__new__(cls)
            cls._instance.logged_id = None
            cls._instance.logged_cpf = None
            cls._instance.logged_name = None
            cls._instance.logged_email = None
            cls._instance.logged_cep = None
            cls._instance.logged_cursos_lecionados = None

        return cls._instance

    def update(self, email):
        db_connection, cursor = get_cursor()

        user_query = """
        SELECT * FROM usuarios
        WHERE email = %s
        """
        cursor.execute(user_query, (email,))
        user_info = cursor.fetchone()

        if user_info:
            self.logged_id = user_info[0]
            self.logged_cpf = user_info[1]
            self.logged_name = user_info[2]
            self.logged_email = user_info[3]
            self.logged_cep = user_info[5]

            curso_query = """
            SELECT cursos_id FROM matriculas
            WHERE aluno_id = %s
            """
            cursor.execute(curso_query, (self.logged_id,))
            cursor.fetchone()

        close_connection(db_connection, cursor)
        

alunosession = AlunoSession()
professorsession = ProfessorSession()

    