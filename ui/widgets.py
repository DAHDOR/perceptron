import customtkinter as ctk

def create_custom_button(text, command): return ctk.CTkButton(text=text, command=command)

def create_custom_label(text): return ctk.CTkLabel(text=text)

def create_input_field(placeholder): return ctk.CTkEntry(placeholder_text=placeholder)