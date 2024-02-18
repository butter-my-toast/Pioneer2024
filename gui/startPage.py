import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class StartPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = ctk.CTkLabel(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button1 = ctk.CTkButton(self, hover=True, text="Focus Mode", command=lambda: controller.show_frame("WebcamPage"))
        button2 = ctk.CTkButton(self, text="Graph your focus", command=lambda: controller.show_frame("GraphPage"))
        button3 = ctk.CTkButton(self, text="Overlay Mode", command=lambda: controller.show_frame("OverlayPage"))
        
        button1.pack()
        button2.pack()
        button3.pack()

