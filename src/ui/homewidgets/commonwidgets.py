import customtkinter as ctk
from PIL import Image
import tkinter as tk
from tkinter import ttk
import os


class CommonWidgets:
    def __init__(self, master, image_dir):
        self.master = master
        self.image_dir = image_dir

    def open_image(self, image_name, width, height):
        image_path = os.path.join(self.image_dir, image_name)
        return ctk.CTkImage(dark_image=Image.open(image_path), size=(width, height))

    def add_horizontal_separator(self, master, row, column, columnspan=1, padx=0, pady=0, sticky="ew"):
        separator = ttk.Separator(master, orient="horizontal")
        separator.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        return separator

    def add_vertical_separator(self, master, row, column, pady=0, padx=0):
        separator = ttk.Separator(master, orient="vertical")
        separator.grid(row=row, column=column, rowspan=1, pady=pady, padx=padx, sticky="ns")
        return separator 