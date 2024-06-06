import customtkinter as ctk
from ui.homewidgets.commonwidgets import CommonWidgets
from backend.session import session
from backend.home import *

class AlunoWidgets(CommonWidgets):
    def __init__(self, master, image_dir):
        super().__init__(master, image_dir)

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
