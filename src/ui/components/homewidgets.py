import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image
from backend.session import session
import os

class HomeWidgets:
    def __init__(self, master):
        self.master = master
        self.image_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'images'))
        self.welcome()
        self.aluno()
    

    def welcome(self):
        # Ajuste do frame de boas-vindas para se ajustar ao conteúdo
        self.frame_welcome = ctk.CTkFrame(self.master, corner_radius=24)
        self.frame_welcome.place(relx=0.5, rely=0.1, anchor="center")
        
        self.image = self.open_image('logostar.png', 50, 50)
        self.image_label = ctk.CTkLabel(self.frame_welcome, image=self.image.create_scaled_photo_image(1.0, "light"), text="")
        self.image_label.pack(side="left", padx=(30, 5), pady=15)


        self.text_label = ctk.CTkLabel(self.frame_welcome, text=f"Olá {session.logged_name}!", font=("Century Gothic", 24))
        self.text_label.pack(side="left", padx=(10, 30), pady=15)

        # Ajusta o tamanho do frame ao tamanho dos widgets
        self.frame_welcome.update_idletasks()
        width = self.frame_welcome.winfo_reqwidth()
        height = self.frame_welcome.winfo_reqheight()
        self.frame_welcome.place_configure(width=width, height=height)
    
    def aluno(self):
        self.tab_view = ctk.CTkTabview(self.master, corner_radius=24)
        self.tab_view.place(relx=0.5, rely=0.5, anchor="center")

        # Adicionando as abas
        self.tab_view.add("Informações Aluno")
        self.tab_view.add("Curso")

        # Ícone e label de nome
        self.nameicon = self.open_image('user.png', 25, 25)
        self.label_nome = ctk.CTkLabel(self.tab_view.tab("Informações Aluno"), text=f"{session.logged_name}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=self.nameicon, compound="left", anchor= "w", padx=15)
        self.label_nome.grid(row=0, column=0, padx=50,  pady=15, sticky="ew")
        self.separator(self.tab_view.tab("Informações Aluno"), row=1, column=0, padx=50, pady=15, sticky="ew")

        # Ícone e label de e-mail
        self.email_icon = self.open_image('email.png', 25, 25)
        self.label_email = ctk.CTkLabel(self.tab_view.tab("Informações Aluno"), text=f"{session.logged_email}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=self.email_icon, compound="left", anchor= "w", padx=15)
        self.label_email.grid(row=2, column=0, padx=50, pady=15, sticky="ew")
        self.separator(self.tab_view.tab("Informações Aluno"), row=3, column=0, padx=50, pady=15, sticky="ew")

        # Ícone e label de CEP
        self.cep_icon = self.open_image('cep.png', 25, 25)
        self.label_cep = ctk.CTkLabel(self.tab_view.tab("Informações Aluno"), text=f"{session.cep}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=self.cep_icon, compound="left", anchor= "w", padx=15)
        self.label_cep.grid(row=4, column=0, padx=50, pady=15, sticky="ew")
        self.separator(self.tab_view.tab("Informações Aluno"), row=5, column=0, padx=50, pady=15, sticky="ew")

        # Ícone e label de ID
        self.id_icon = self.open_image('id.png', 25, 25)
        self.label_id = ctk.CTkLabel(self.tab_view.tab("Informações Aluno"), text=f"{session.id}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=self.id_icon, compound="left", anchor= "w", padx=15)
        self.label_id.grid(row=6, column=0, padx=50, pady=(15, 25), sticky="ew")
        
        # Curso
        self.label_curso = ctk.CTkLabel(self.tab_view.tab("Curso"), text=f"Curso: {session.course}", font=("Century Gothic", 20))
        self.label_curso.grid(row=0, column=0, padx=5, pady=5, sticky="n")
   
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

    def open_image(self, image_name, a, b):
        """
        Abre uma imagem a partir do diretório de imagens e retorna a imagem aberta.
        
        Args:
            image_name (str): O nome do arquivo da imagem a ser aberta.
        
        Returns:
            CTkImage: A imagem aberta como um objeto CTkImage.
        """
        image_path = os.path.join(self.image_dir, image_name)
        return ctk.CTkImage(dark_image=Image.open(image_path), size= (a, b))
