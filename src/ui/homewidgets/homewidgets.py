import customtkinter as ctk
import os
from ui.homewidgets.alunowidgets import AlunoWidgets
from ui.homewidgets.professorwidgets import ProfessorWidgets
from ui.homewidgets.commonwidgets import CommonWidgets
from backend.session import session


class HomeWidgets:
    def __init__(self, master, user_type):
        self.master = master
        self.user_type = user_type
        self.image_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'images'))
        self.current_frame = None
        self.current_toplevel = None

        self.aluno_widgets = AlunoWidgets(master, self.image_dir)
        self.professor_widgets = ProfessorWidgets(master, self.image_dir, self)
        self.common_widgets = CommonWidgets(master, self.image_dir)

    def welcome_widget(self):
        frame_welcome = ctk.CTkFrame(self.master, corner_radius=24)
        frame_welcome.place(relx=0.5, rely=0.1, anchor="center")
        
        image = self.common_widgets.open_image('logostar.png', 50, 50)
        image_label = ctk.CTkLabel(frame_welcome, image=image.create_scaled_photo_image(1.0, "light"), text="")
        image_label.pack(side="left", padx=(30, 5), pady=15)

        name = session.logged_name
        
        text_label = ctk.CTkLabel(frame_welcome, text=f"Olá {name}!", font=("Century Gothic", 24))
        text_label.pack(side="left", padx=(10, 30), pady=15)

        frame_welcome.update_idletasks()
        width = frame_welcome.winfo_reqwidth()
        height = frame_welcome.winfo_reqheight()
        frame_welcome.place_configure(width=width, height=height)
        
    def place_widget(self, widget_name):
        if self.current_frame is not None:
            self.current_frame.place_forget()
        
        self.get_current_frame(widget_name)
        self.current_frame.place(relx=0.5, rely=0.5, anchor="center")


    def get_current_frame(self, widget_name):
        widget_mapping = {
            'aluno': {
                'alunos': self.aluno_widgets.aluno_info_widget,
                'notas': self.aluno_widgets.aluno_notas_widget,
                'materias': self.aluno_widgets.materia_aluno_widget
            },
            'professor': {
                'professor_info': self.professor_widgets.professor_info_widget,
                'disciplinas_lecionada': self.professor_widgets.professor_disciplinas_widget,
                'alunos_lecionado': self.professor_widgets.professor_alunos_widget
            }
        }

        self.current_frame = widget_mapping.get(self.user_type, {}).get(widget_name, None)()

