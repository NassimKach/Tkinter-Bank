import tkinter
import customtkinter
from PIL import ImageTk, Image
import config
import client
import agent

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("custom_theme.json")


class config:
    root_tk = customtkinter.CTk()
    root_tk.title("Banque Application")
    root_tk.iconbitmap("./img/icon.ico")
    root_tk.geometry("900x600")
    root_tk.resizable(False, False)

    menu_frame = customtkinter.CTkFrame(
        root_tk, width=900, height=600, bg="gray10")
    menu_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("./img/logo.png"))
    label = customtkinter.CTkLabel(config.menu_frame, image=img)
    label.pack()
    client_btn = customtkinter.CTkButton(config.menu_frame,
                                         text="Entrer comme un client",
                                         width=250,
                                         height=50,
                                         bg="gray10",
                                         text_font=("Poppins", "12", "bold"),
                                         command=client_page)
    client_btn.pack(pady=20)
    agent_btn = customtkinter.CTkButton(config.menu_frame,
                                        text="Entrer comme un agent",
                                        width=250,
                                        height=50,
                                        text_font=("Poppins", "12", "bold"),
                                        command=agent_page,
                                        )


config.root_tk.mainloop()
