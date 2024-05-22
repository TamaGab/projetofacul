class Session:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Session, cls).__new__(cls)
            cls._instance.logged_name = None
            cls._instance.logged_email = None
            cls._instance.cep = "testecep"
            cls._instance.id = "testeid"
            
        return cls._instance


session = Session()
