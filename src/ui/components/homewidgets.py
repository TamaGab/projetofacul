import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image
from backend.session import session
import os

class HomeWidgets:
    def __init__(self, master):
        self.master = master
        self.welcome()
        self.aluno()  # Mostra o frame do aluno ao iniciar a aplicação

    def welcome(self):
        # Ajuste do frame de boas-vindas para se ajustar ao conteúdo
        self.frame_welcome = ctk.CTkFrame(self.master, corner_radius=24)
        self.frame_welcome.place(relx=0.57, rely=0.1, anchor="center")
        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..', 'images', 'logostar.png')
        image_path = os.path.abspath(image_path)

        self.image = ctk.CTkImage(dark_image=Image.open(image_path), size=(50, 50))

        self.image_label = ctk.CTkLabel(self.frame_welcome, image=self.image, text="")
        self.image_label.pack(side="left", padx=(30, 5), pady=15)

        self.text_label = ctk.CTkLabel(self.frame_welcome, text=f"Olá {session.logged_name}!", font=("Century Gothic", 24))
        self.text_label.pack(side="left", padx=(10, 30), pady=15)

        # Ajuste o tamanho do frame ao tamanho dos widgets
        self.frame_welcome.update_idletasks()
        width = self.frame_welcome.winfo_reqwidth()
        height = self.frame_welcome.winfo_reqheight()
        self.frame_welcome.place_configure(width=width, height=height)

    def aluno(self):
        self.frame_aluno = ctk.CTkFrame(self.master, corner_radius=0)
        self.frame_aluno.place(relwidth=0.5, relheight=0.4, relx=0.6, rely=0.5, anchor="center")

        self.tab_view = ctk.CTkTabview(self.frame_aluno, corner_radius=0)
        self.tab_view.pack(expand=True, fill="both", padx=10, pady=10)
        self.tab_view.add("Informações Aluno")
        self.tab_view.add("Curso")
        
        self.frame_aluno2 = ctk.CTkFrame(self.tab_view.tab("Informações Aluno"), corner_radius=24)
        self.frame_aluno2.pack(expand=True)
        
             
        # Nome
        self.label_nome = ctk.CTkLabel(self.frame_aluno2, text=f"{session.logged_name}", font=("Century Gothic", 18))
        self.label_nome.grid(row=0, column=0, columnspan=2, padx=25, pady=(10, 0))
        self.separator(self.frame_aluno2, row=1, column=0, columnspan=2, padx=25, pady=(5, 15))
        
        # E-mail
        self.label_email_text = ctk.CTkLabel(self.frame_aluno2, text="E-mail:", font=("Century Gothic", 18))
        self.label_email_text.grid(row=2, column=0, padx=(25, 5), pady=(0, 10), sticky="e")

        self.label_email = ctk.CTkLabel(self.frame_aluno2, text=f"{session.logged_email}", font=ctk.CTkFont("Century Gothic", size=18, weight="bold"))
        self.label_email.grid(row=2, column=1, padx=(5, 25), pady=(0, 10), sticky="w")
        self.separator(self.frame_aluno2, row=3, column=0, columnspan=2, padx=25, pady=(5, 10))
        
        
        # CEP
        self.label_cep_text = ctk.CTkLabel(self.frame_aluno2, text="CEP:", font=("Century Gothic", 18))
        self.label_cep_text.grid(row=4, column=0, padx=(25, 5), pady=(0, 10), sticky="e")

        self.label_cep = ctk.CTkLabel(self.frame_aluno2, text=f"{session.cep}", font=ctk.CTkFont("Century Gothic", size=18, weight="bold"))
        self.label_cep.grid(row=4, column=1, padx=(5, 25), pady=(0, 10), sticky="w")
        self.separator(self.frame_aluno2, row=5, column=0, columnspan=2, padx=25, pady=(5, 10))
        
        
        # ID
        self.label_id_text = ctk.CTkLabel(self.frame_aluno2, text="ID:", font=("Century Gothic", 18))
        self.label_id_text.grid(row=6, column=0, padx=(25, 5), pady=(0, 10), sticky="e")

        self.label_id = ctk.CTkLabel(self.frame_aluno2, text=f"{session.id}", font=ctk.CTkFont("Century Gothic", size=18, weight="bold"))
        self.label_id.grid(row=6, column=1, padx=(5, 25), pady=(0, 10), sticky="w")
        
        
        # Curso
        self.label_curso = ctk.CTkLabel(self.tab_view.tab("Curso"), text=f"Curso: {session.course}", font=("Century Gothic", 18))
        self.label_curso.grid(row=0, column=0, padx=5, pady=5, sticky="w")
   
    def materia(self):
        # Criação do frame de matérias
        self.frame_materia = ctk.CTkFrame(self.master)
        self.frame_materia.place(relwidth=0.5, relheight=0.4, relx=0.5, rely=0.5, anchor="center")
        
        # Adicionar widgets específicos para matérias
        self.label_materia = ctk.CTkLabel(self.frame_materia, text="Informações de Matérias", font=("Century Gothic", 18))
        self.label_materia.pack(pady=5)

    def notas(self):
        # Criação do frame de notas
        self.frame_notas = ctk.CTkFrame(self.master)
        self.frame_notas.place(relwidth=0.5, relheight=0.4, relx=0.5, rely=0.5, anchor="center")
        
        # Adicionar widgets específicos para notas
        self.label_notas = ctk.CTkLabel(self.frame_notas, text="Informações de Notas", font=("Century Gothic", 18))
        self.label_notas.pack(pady=5)

    def separator(self, master, row, column, columnspan=1, padx=0, pady=0, sticky="ew"):
        separator = ttk.Separator(master, orient="horizontal")
        separator.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        return separator

