import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image
from backend.session import alunosession, professorsession
import os
from backend.home import professordisciplinas, professoralunos

class HomeWidgets:
    def __init__(self, master, user_type):
        self.master = master
        self.image_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'images'))
        self.current_frame = None
    
    def welcomewidget(self, user_type):
        
        self.frame_welcome = ctk.CTkFrame(self.master, corner_radius=24)
        self.frame_welcome.place(relx=0.5, rely=0.1, anchor="center")
        
        self.image = self.open_image('logostar.png', 50, 50)
        self.image_label = ctk.CTkLabel(self.frame_welcome, image=self.image.create_scaled_photo_image(1.0, "light"), text="")
        self.image_label.pack(side="left", padx=(30, 5), pady=15)

        name = alunosession.logged_name if user_type == "aluno" else professorsession.logged_name
                
        
        self.text_label = ctk.CTkLabel(self.frame_welcome, text=f"Olá {name}!", font=("Century Gothic", 24))
        self.text_label.pack(side="left", padx=(10, 30), pady=15)

        self.frame_welcome.update_idletasks()
        width = self.frame_welcome.winfo_reqwidth()
        height = self.frame_welcome.winfo_reqheight()
        self.frame_welcome.place_configure(width=width, height=height)
        
    def placewidget(self, widget_name):
        if self.current_frame is not None:
            self.current_frame.place_forget()

        if widget_name == 'alunos':
            self.current_frame = self.alunoinfowidget()
        elif widget_name == 'notas':
            self.current_frame = self.notasalunowidget()
        elif widget_name == 'materias':
            self.current_frame = self.materiaalunowidget()
        elif widget_name == 'professor_info':
            self.current_frame = self.professorinfowidget()
        elif widget_name == 'disciplinas_lecionada':
            self.current_frame = self.professordisciplinaswidget()
        elif widget_name == 'alunos_lecionado':
            self.current_frame = self.professoralunoswidget()
        

        self.current_frame.place(relx=0.5, rely=0.5, anchor="center")        
 
 
    def alunoinfowidget(self):
            
        self.tab_view = ctk.CTkTabview(self.master, corner_radius=24)
        self.tab_view.add("Informações Aluno")
        self.tab_view.add("Curso")

        # TAB INFO ALUNO
        # NOME
        self.nameicon = self.open_image('user.png', 25, 25)
        self.label_nome = ctk.CTkLabel(self.tab_view.tab("Informações Aluno"), text=f"{alunosession.logged_name}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=self.nameicon, compound="left", anchor= "w", padx=15)
        self.label_nome.grid(row=0, column=0, padx=50,  pady=15, sticky="ew")
        self.separator(self.tab_view.tab("Informações Aluno"), row=1, column=0, padx=50, pady=15, sticky="ew")

        # EMAIL
        self.email_icon = self.open_image('email.png', 25, 25)
        self.label_email = ctk.CTkLabel(self.tab_view.tab("Informações Aluno"), text=f"{alunosession.logged_email}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=self.email_icon, compound="left", anchor= "w", padx=15)
        self.label_email.grid(row=2, column=0, padx=50, pady=15, sticky="ew")
        self.separator(self.tab_view.tab("Informações Aluno"), row=3, column=0, padx=50, pady=15, sticky="ew")

        # CEP
        self.cep_icon = self.open_image('cep.png', 25, 25)
        self.label_cep = ctk.CTkLabel(self.tab_view.tab("Informações Aluno"), text=f"{alunosession.logged_cep}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=self.cep_icon, compound="left", anchor= "w", padx=15)
        self.label_cep.grid(row=4, column=0, padx=50, pady=15, sticky="ew")
        self.separator(self.tab_view.tab("Informações Aluno"), row=5, column=0, padx=50, pady=15, sticky="ew")

        # ID
        self.id_icon = self.open_image('id.png', 25, 25)
        self.label_id = ctk.CTkLabel(self.tab_view.tab("Informações Aluno"), text=f"{alunosession.logged_id}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=self.id_icon, compound="left", anchor= "w", padx=15)
        self.label_id.grid(row=6, column=0, padx=50, pady=(15, 25), sticky="ew")
        
        # TAB CURSO
        
        self.label_cursonome = ctk.CTkLabel(self.tab_view.tab("Curso"), text=f"{alunosession.logged_curso}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"))
        self.label_cursonome.grid(row=0, column=0, padx=50, pady=0, sticky="ew")
        self.separator(self.tab_view.tab("Curso"), row=1, column=0, padx=50, pady=15, sticky="ew")

        self.label_cursoid = ctk.CTkLabel(self.tab_view.tab("Curso"), text=f"Carga: {alunosession.logged_cargacurso} semestres", font=("Century Gothic", 20))
        self.label_cursoid.grid(row=2, column=0, padx=50, pady=15, sticky="ew")
        
        self.label_infocurso = ctk.CTkLabel(self.tab_view.tab("Curso"), text=f"Coordenador: {alunosession.logged_coordenadorcurso}", font=("Century Gothic", 20))
        self.label_infocurso.grid(row=3, column=0, padx=50, pady=15, sticky="ew")
        return self.tab_view
    
    
    def materiaalunowidget(self):
        frame = ctk.CTkFrame(self.master)
        
        self.label_materia = ctk.CTkLabel(frame, text="Informações de Matérias", font=("Century Gothic", 18))
        self.label_materia.pack(pady=5)
        return frame
    
    def notasalunowidget(self):
        
        frame = ctk.CTkFrame(self.master)

        self.label_notas = ctk.CTkLabel(frame, text="Informações de Notas", font=("Century Gothic", 18))
        self.label_notas.pack(pady=5)    
        return frame
    
    def professorinfowidget(self):
        frame = ctk.CTkFrame(self.master, corner_radius=24)
        
        # TAB INFO ALUNO
        # NOME
        self.nameicon = self.open_image('user.png', 25, 25)
        self.label_nome = ctk.CTkLabel(frame, text=f"{professorsession.logged_name}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=self.nameicon, compound="left", anchor= "w", padx=15)
        self.label_nome.grid(row=0, column=0, padx=50,  pady=(25,15), sticky="ew")
        self.separator(frame, row=1, column=0, padx=50, pady=15, sticky="ew")

        # EMAIL
        self.email_icon = self.open_image('email.png', 25, 25)
        self.label_email = ctk.CTkLabel(frame, text=f"{professorsession.logged_email}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=self.email_icon, compound="left", anchor= "w", padx=15)
        self.label_email.grid(row=2, column=0, padx=50, pady=15, sticky="ew")
        self.separator(frame, row=3, column=0, padx=50, pady=15, sticky="ew")

        # CEP
        self.cep_icon = self.open_image('cep.png', 25, 25)
        self.label_cep = ctk.CTkLabel(frame, text=f"{professorsession.logged_cep}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=self.cep_icon, compound="left", anchor= "w", padx=15)
        self.label_cep.grid(row=4, column=0, padx=50, pady=15, sticky="ew")
        self.separator(frame, row=5, column=0, padx=50, pady=15, sticky="ew")

        # ID
        self.id_icon = self.open_image('id.png', 25, 25)
        self.label_id = ctk.CTkLabel(frame, text=f"{professorsession.logged_id}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=self.id_icon, compound="left", anchor= "w", padx=15)
        self.label_id.grid(row=6, column=0, padx=50, pady=(15, 25), sticky="ew")
        return frame
    
    def professordisciplinaswidget(self):
        frame = ctk.CTkScrollableFrame(self.master, width=400)
        
        cursos = professordisciplinas(professorsession.logged_email)
        
        for idx, curso_nome in enumerate(cursos):
            label = ctk.CTkLabel(frame, text=curso_nome, font=ctk.CTkFont("Century Gothic", size=20, weight="bold"))
            label.grid(row=idx*2, column=0, padx=50, pady=15, sticky="ew")  
            
            if idx < len(cursos) - 1:  
                self.separator(frame, row=idx*2 + 1, column=0, padx=50, pady=5, sticky="ew")

        frame.grid_columnconfigure(0, weight=1)
    
        return frame
    def professoralunoswidget(self):   
        frame = ctk.CTkScrollableFrame(self.master, width=400)
        alunos = professoralunos(professorsession.logged_email)
    
        for idx, aluno in enumerate(alunos):
            aluno_nome = aluno['aluno_nome']
            
            label = ctk.CTkLabel(frame, text=aluno_nome, font=ctk.CTkFont("Century Gothic", size=20, weight="bold"))
            label.grid(row=idx*2, column=0, padx=50, pady=15, sticky="ew")  
            
            if idx < len(alunos) - 1:  
                separator = ctk.CTkFrame(frame, height=2, fg_color="gray")
                separator.grid(row=idx*2 + 1, column=0, padx=50, pady=5, sticky="ew")

        frame.grid_columnconfigure(0, weight=1)
        
            
            
    def separator(self, master, row, column, columnspan=1, padx=0, pady=0, sticky="ew"):
        
        separator = ttk.Separator(master, orient="horizontal")
        separator.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        return separator

    def open_image(self, image_name, a, b):
        
        image_path = os.path.join(self.image_dir, image_name)
        return ctk.CTkImage(dark_image=Image.open(image_path), size= (a, b))
