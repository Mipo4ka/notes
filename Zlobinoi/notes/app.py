import customtkinter as ctk
import os
from tkinter import PhotoImage

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

NOTES_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "notes.json")

class NotesApp:
    def __init__(self, master):
        self.root = master
        self.root.title("Заметки")
        self.root.geometry("1000x600")
        self.root.minsize(1000, 600)
        self.icon = PhotoImage(file=os.path.join(os.path.dirname(__file__), "images", "notes.png"))
        self.root.iconphoto(False, self.icon)
        
if __name__ == "__main__":
    root = ctk.CTk()
    app = NotesApp(root)
    root.mainloop()