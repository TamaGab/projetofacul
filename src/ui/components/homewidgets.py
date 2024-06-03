import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image
from backend.session import session
import os
from backend.home import *


class HomeWidgets:
    def __init__(self, master, user_type):
        self.master = master
        self.image_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'images'))
        self.current_frame = None
        self.current_toplevel = None  
    
    def welcome_widget(self, user_type):
        frame_welcome = ctk.CTkFrame(self.master, corner_radius=24)
        frame_welcome.place(relx=0.5, rely=0.1, anchor="center")
        
        image = self.open_image('logostar.png', 50, 50)
        image_label = ctk.CTkLabel(frame_welcome, image=image.create_scaled_photo_image(1.0, "light"), text="")
        image_label.pack(side="left", padx=(30, 5), pady=15)

        name = session.logged_name if user_type == "aluno" else session.logged_name
        
        text_label = ctk.CTkLabel(frame_welcome, text=f"Olá {name}!", font=("Century Gothic", 24))
        text_label.pack(side="left", padx=(10, 30), pady=15)

        frame_welcome.update_idletasks()
        width = frame_welcome.winfo_reqwidth()
        height = frame_welcome.winfo_reqheight()
        frame_welcome.place_configure(width=width, height=height)
        
    def place_widget(self, widget_name):
        if self.current_frame is not None:
            self.current_frame.place_forget()

        if widget_name == 'alunos':
            self.current_frame = self.aluno_info_widget()
        elif widget_name == 'notas':
            self.current_frame = self.aluno_notas_widget()
        elif widget_name == 'materias':
            self.current_frame = self.materia_aluno_widget()
        elif widget_name == 'professor_info':
            self.current_frame = self.professor_info_widget()
        elif widget_name == 'disciplinas_lecionada':
            self.current_frame = self.professor_disciplinas_widget()
        elif widget_name == 'alunos_lecionado':
            self.current_frame = self.professor_alunos_widget()
        
        self.current_frame.place(relx=0.5, rely=0.5, anchor="center")        
 
    def aluno_info_widget(self):
        tab_view = ctk.CTkTabview(self.master, corner_radius=24)
        tab_view.add("DADOS")
        tab_view.add("CURSO")

        # TAB INFO ALUNO
        # NOME
        name_icon = self.open_image('user.png', 25, 25)
        label_nome = ctk.CTkLabel(tab_view.tab("DADOS"), text=f"{session.logged_name}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=name_icon, compound="left", anchor="w", padx=15)
        label_nome.grid(row=0, column=0, padx=50, pady=(15, 15), sticky="ew")
        self.add_horizontal_separator(tab_view.tab("DADOS"), row=1, column=0, padx=50, pady=15, sticky="ew")

        # EMAIL
        email_icon = self.open_image('email.png', 25, 25)
        label_email = ctk.CTkLabel(tab_view.tab("DADOS"), text=f"{session.logged_email}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=email_icon, compound="left", anchor="w", padx=15)
        label_email.grid(row=2, column=0, padx=50, pady=15, sticky="ew")
        self.add_horizontal_separator(tab_view.tab("DADOS"), row=3, column=0, padx=50, pady=15, sticky="ew")

        # CEP
        cep_icon = self.open_image('cep.png', 25, 25)
        label_cep = ctk.CTkLabel(tab_view.tab("DADOS"), text=f"{session.logged_cep}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=cep_icon, compound="left", anchor="w", padx=15)
        label_cep.grid(row=4, column=0, padx=50, pady=15, sticky="ew")
        self.add_horizontal_separator(tab_view.tab("DADOS"), row=5, column=0, padx=50, pady=15, sticky="ew")

        # ID
        id_icon = self.open_image('id.png', 25, 25)
        label_id = ctk.CTkLabel(tab_view.tab("DADOS"), text=f"{session.logged_id}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=id_icon, compound="left", anchor="w", padx=15)
        label_id.grid(row=6, column=0, padx=50, pady=(15, 25), sticky="ew")
        
        # TAB CURSO
        label_cursonome = ctk.CTkLabel(tab_view.tab("CURSO"), text=f"{get_course_name(session.logged_id)}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"))
        label_cursonome.grid(row=0, column=0, padx=50, pady=0, sticky="ew")
        self.add_horizontal_separator(tab_view.tab("CURSO"), row=1, column=0, padx=50, pady=15, sticky="ew")

        label_cursocarga = ctk.CTkLabel(tab_view.tab("CURSO"), text=f"Carga: {get_course_carga(session.logged_id)} semestres", font=("Century Gothic", 20))
        label_cursocarga.grid(row=2, column=0, padx=50, pady=15, sticky="ew")
        
        label_infocurso = ctk.CTkLabel(tab_view.tab("CURSO"), text=f"Coordenador: {get_course_coordenador(session.logged_id)}", font=("Century Gothic", 20))
        label_infocurso.grid(row=3, column=0, padx=50, pady=15, sticky="ew")
        return tab_view
    
    def materia_aluno_widget(self):
        frame = ctk.CTkScrollableFrame(self.master, width=500, height=450)
        
    
        label_disciplinatitle = ctk.CTkLabel(frame, text="DISCIPLINA", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"))
        label_disciplinatitle.grid(row=0, column=0, padx=(50,25), pady=(40,10), sticky="w")
        
        label_cargadisciplina = ctk.CTkLabel(frame, text="CARGA HORÁRIA", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"))
        label_cargadisciplina.grid(row=0, column=2, padx=(25,50), pady=(40,10), sticky="w")

       
        self.add_horizontal_separator(frame, row=1, column=0, columnspan=3, padx=50, pady=5, sticky="ew")

        materia = get_disciplina_carga(session.logged_id)

    
        for idx, (disciplina_nome, disciplina_carga) in enumerate(materia):
            current_row = 2 + 2 * idx 
            
            label_disciplinanome = ctk.CTkLabel(frame, text=disciplina_nome, font=ctk.CTkFont("Century Gothic", size=20))
            label_disciplinanome.grid(row=current_row, column=0, padx=(50,25), pady=15, sticky="w")
            
            label_disciplinacarga = ctk.CTkLabel(frame, text=disciplina_carga, font=ctk.CTkFont("Century Gothic", size=20))
            label_disciplinacarga.grid(row=current_row, column=2, padx=(25,50), pady=15, sticky="w")
            
            self.add_vertical_separator(frame, row=current_row, column=1, pady=15)

    
            if idx < len(materia) - 1:
                self.add_horizontal_separator(frame, row=current_row + 1, column=0, columnspan=3, padx=50, pady=5, sticky="ew")

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        return frame
        
        
    def aluno_notas_widget(self):
        frame = ctk.CTkScrollableFrame(self.master, width=450, height=450)
        
        label_disciplinatitle = ctk.CTkLabel(frame, text="DISCIPLINA", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"))
        label_disciplinatitle.grid(row=0, column=0, padx=(50,25), pady=(40,10), sticky="w")
        
        label_notatitle = ctk.CTkLabel(frame, text="NOTA", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"))
        label_notatitle.grid(row=0, column=2, padx=(25,50), pady=(40,10), sticky="w")

       
        self.add_horizontal_separator(frame, row=1, column=0, columnspan=3, padx=50, pady=5, sticky="ew")
        
      
        notas_disciplinas = get_aluno_nota(session.logged_id)

    
        for idx, (nota, disciplina_nome) in enumerate(notas_disciplinas):
            current_row = 2 + 2 * idx 
            
            label_disciplina = ctk.CTkLabel(frame, text=disciplina_nome, font=ctk.CTkFont("Century Gothic", size=20))
            label_disciplina.grid(row=current_row, column=0, padx=(50,25), pady=15, sticky="w")
            
            label_nota = ctk.CTkLabel(frame, text=nota, font=ctk.CTkFont("Century Gothic", size=20))
            label_nota.grid(row=current_row, column=2, padx=(25,50), pady=15, sticky="w")
            
            self.add_vertical_separator(frame, row=current_row, column=1, pady=15)

    
            if idx < len(notas_disciplinas) - 1:
                self.add_horizontal_separator(frame, row=current_row + 1, column=0, columnspan=3, padx=50, pady=5, sticky="ew")

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        
        return frame
    
    def professor_info_widget(self):
        frame = ctk.CTkFrame(self.master, corner_radius=24)
        
        label_title = ctk.CTkLabel(frame, text="DADOS", font=ctk.CTkFont("Century Gothic", size=28, weight="bold"))
        label_title.grid(row=0, column=0, padx=50, pady=(25, 15), sticky="nsew")
        self.add_horizontal_separator(frame, row=1, column=0, padx=50, pady=15, sticky="ew")
        
        name_icon = self.open_image('user.png', 25, 25)
        label_nome = ctk.CTkLabel(frame, text=f"{session.logged_name}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=name_icon, compound="left", anchor="w", padx=15)
        label_nome.grid(row=2, column=0, padx=50, pady=(15, 15), sticky="ew")
        self.add_horizontal_separator(frame, row=3, column=0, padx=50, pady=15, sticky="ew")

        email_icon = self.open_image('email.png', 25, 25)
        label_email = ctk.CTkLabel(frame, text=f"{session.logged_email}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=email_icon, compound="left", anchor="w", padx=15)
        label_email.grid(row=4, column=0, padx=50, pady=15, sticky="ew")
        self.add_horizontal_separator(frame, row=5, column=0, padx=50, pady=15, sticky="ew")

        cep_icon = self.open_image('cep.png', 25, 25)
        label_cep = ctk.CTkLabel(frame, text=f"{session.logged_cep}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=cep_icon, compound="left", anchor="w", padx=15)
        label_cep.grid(row=6, column=0, padx=50, pady=15, sticky="ew")
        self.add_horizontal_separator(frame, row=7, column=0, padx=50, pady=15, sticky="ew")
 
        id_icon = self.open_image('id.png', 25, 25)
        label_id = ctk.CTkLabel(frame, text=f"{session.logged_id}", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"), image=id_icon, compound="left", anchor="w", padx=15)
        label_id.grid(row=8, column=0, padx=50, pady=(15, 25), sticky="ew")
        return frame
    
    def professor_disciplinas_widget(self):
        frame = ctk.CTkScrollableFrame(self.master, width=450, height=450)
        
        label_title = ctk.CTkLabel(frame, text="DISCIPLINAS", font=ctk.CTkFont("Century Gothic", size=28, weight="bold"))
        label_title.grid(row=0, column=0, padx=50, pady=(25, 15), sticky="nsew")
        self.add_horizontal_separator(frame, row=1, column=0, padx=50, pady=5)
        
        cursos = get_professor_disciplina(session.logged_email)
        
        for idx, curso_nome in enumerate(cursos):
            label = ctk.CTkLabel(frame, text=curso_nome, font=ctk.CTkFont("Century Gothic", size=20, weight="bold"))
            label.grid(row=idx*2+2, column=0, padx=50, pady=15, sticky="ew")
            
            if idx < len(cursos) - 1:
                self.add_horizontal_separator(frame, row=idx*2 + 3, column=0, padx=50, pady=5)

        frame.grid_columnconfigure(0, weight=1)
        return frame
    
    def professor_alunos_widget(self):   
        tab_view = ctk.CTkTabview(self.master, corner_radius=24, height=450)
        alunos = get_professor_aluno(session.logged_email)

        disciplinas_dict = {}
        for aluno_id, aluno_nome, disciplina_id, disciplina_nome, nota_aluno in alunos:
            if disciplina_nome not in disciplinas_dict:
                disciplinas_dict[disciplina_nome] = []
            disciplinas_dict[disciplina_nome].append((aluno_id, aluno_nome, disciplina_id, nota_aluno))

        for disciplina_nome, alunos_notas in disciplinas_dict.items():
            tab_view.add(f"{disciplina_nome}".upper())
            frame = ctk.CTkScrollableFrame(tab_view.tab(f"{disciplina_nome}".upper()), width=450)
            
            label_alunostitle = ctk.CTkLabel(frame, text="ALUNOS", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"))
            label_alunostitle.grid(row=0, column=0, padx=(50,25), pady=(0,10), sticky="w")
            
            label_notatitle = ctk.CTkLabel(frame, text="NOTA", font=ctk.CTkFont("Century Gothic", size=22, weight="bold"))
            label_notatitle.grid(row=0, column=2, padx=(25,50), pady=(0,10), sticky="nsew")
            
            self.add_horizontal_separator(frame, row=1, column=0, columnspan=3, padx=50, pady=5, sticky="ew")
            
            for idx, (aluno_id, aluno_nome, disciplina_id, nota_aluno) in enumerate(alunos_notas):
                current_row = 2 + 2 * idx 
                labelnome = ctk.CTkLabel(frame, text=aluno_nome, font=ctk.CTkFont("Century Gothic", size=20))
                labelnome.grid(row=current_row, column=0, padx=(50,25), pady=15, sticky="w")
                
                nota = "DEFINIR" if nota_aluno is None else str(nota_aluno)
                buttonnota = ctk.CTkButton(frame, text=nota, font=ctk.CTkFont("Century Gothic", size=20), hover=False, fg_color="transparent", 
                                           command=lambda n=nota, ai = aluno_id, di = disciplina_id: self.nota_toplevel(n, ai, di))
                buttonnota.grid(row=current_row, column=2, padx=(25,50), pady=15, sticky="nsew")
                
                self.add_vertical_separator(frame, row=current_row, column=1, pady=15)
                            
                if idx < len(alunos_notas) - 1:
                    self.add_horizontal_separator(frame, row=current_row + 1, column=0, columnspan=3, padx=50, pady=5, sticky="ew")


                frame.grid_columnconfigure(0, weight=1)
                frame.grid_columnconfigure(1, weight=1)
                frame.grid_columnconfigure(2, weight=1)
                
                frame.pack(fill="both", expand=True)

        tab_view.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        return tab_view


    def add_horizontal_separator(self, master, row, column, columnspan=1, padx=0, pady=0, sticky="ew"):
        separator = ttk.Separator(master, orient="horizontal")
        separator.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        return separator
    
    def add_vertical_separator(self, master, row, column, pady=0, padx=0):
        separator = ttk.Separator(master, orient="vertical")
        separator.grid(row=row, column=column, rowspan=1, pady=pady, padx=padx, sticky="ns")
        return separator
    
    def open_image(self, image_name, width, height):
        image_path = os.path.join(self.image_dir, image_name)
        return ctk.CTkImage(dark_image=Image.open(image_path), size=(width, height))
    
    def nota_toplevel(self, nota, aluno_id, disciplina_id):
        if nota == "DEFINIR":
            if self.current_toplevel is not None:
                self.current_toplevel.destroy()

            self.current_toplevel = ctk.CTkToplevel(self.master)
            
            if self.current_toplevel is not None:
                self.current_toplevel.title("Definir Nota")
        
                label = ctk.CTkLabel(self.current_toplevel, text="INSIRA A NOTA:", font=ctk.CTkFont("Century Gothic", size=20, weight="bold"))
                label.grid(row=0, column=0, sticky="ew", padx=50, pady=(25, 25))

                nota_entry = ctk.CTkEntry(self.current_toplevel, width=200)
                nota_entry.grid(row=1, column=0, padx=50, pady=15)
                nota_entry.bind("<KeyRelease>", format_nota)
                nota_entry.bind("<Enter>", enable_nota_editing)
                nota_entry.bind("<Button-1>", enable_nota_editing)
                
                save_button = ctk.CTkButton(self.current_toplevel, text="Salvar",fg_color="#41c269", corner_radius=32,
                                          hover_color="#4F5250", width=200, font=("Century Gothic", 18), command=lambda: save_and_destroy(self, nota_entry.get(), aluno_id, disciplina_id))
                save_button.grid(row=2, column=0, padx=50, pady=(25, 25))
    
                self.current_toplevel.grid_columnconfigure(0, weight=1)
                
                
                self.current_toplevel.update_idletasks()
              
                x = (self.current_toplevel.winfo_screenwidth() - self.current_toplevel.winfo_reqwidth()) // 2
                y = (self.current_toplevel.winfo_screenheight() - self.current_toplevel.winfo_reqheight()) // 2
                self.current_toplevel.geometry(f"+{x}+{y}")
                self.current_toplevel.resizable(False,False)
                
                self.current_toplevel.lift()
                self.current_toplevel.attributes("-topmost", True)
                
            else:
                return None
            
    def data_att(self):
        return self.place_widget('alunos_lecionado')       
