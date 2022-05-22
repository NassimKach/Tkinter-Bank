import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("custom_theme.json")

root_tk = customtkinter.CTk()
root_tk.title("Banque Application")
root_tk.iconbitmap("./img/icon.ico")
root_tk.geometry("900x600")
root_tk.resizable(False, False)


menu_frame = customtkinter.CTkFrame(
    root_tk, width=900, height=600, bg="gray10")
menu_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
