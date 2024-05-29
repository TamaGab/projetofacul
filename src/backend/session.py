from .database import *

class Session:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Session, cls).__new__(cls)
            cls._instance.logged_id = None
            cls._instance.logged_cpf = None
            cls._instance.logged_name = None
            cls._instance.logged_email = None
            cls._instance.logged_cep = None
        return cls._instance

    def update(self, email):
        db_connection, cursor = get_cursor()

        user_query = """
        SELECT id, cpf, nome, email, cep FROM usuarios
        WHERE email = %s
        """
        cursor.execute(user_query, (email,))
        user_info = cursor.fetchone()

        if user_info:
            self.logged_id = user_info[0]
            self.logged_cpf = user_info[1]
            self.logged_name = user_info[2]
            self.logged_email = user_info[3]
            self.logged_cep = user_info[4]
    
        close_connection(db_connection, cursor)
    
    
session = Session()