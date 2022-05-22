import tkinter
import customtkinter
import config
import json
import client


def client_services_func():
    client.client_frame.place_forget()
    bnj_text.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
    client_services_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def quitter_btn_command():
    client_services_frame.place_forget()
    client.client_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


client_services_frame = customtkinter.CTkFrame(
    width=900, height=600, bg="gray10")

ajouter_btn = customtkinter.CTkButton(client_services_frame,
                                      corner_radius=0,
                                      width=250,
                                      height=50,
                                      text="Afficher le solde",
                                      text_font=("Poppins", "12"),
                                      #   command=ajclient_btn_command
                                      )
ajouter_btn.place(relx=0.13, rely=0.3, anchor=tkinter.CENTER)

supprimer_btn = customtkinter.CTkButton(client_services_frame,
                                        corner_radius=0,
                                        width=250,
                                        height=50,
                                        text="Retirer d'argent",
                                        text_font=("Poppins", "12"),
                                        # command=supprimer_btn_command
                                        )
supprimer_btn.place(relx=0.13, rely=0.4, anchor=tkinter.CENTER)


exporter_btn = customtkinter.CTkButton(client_services_frame,
                                       corner_radius=0,
                                       width=250,
                                       height=50,
                                       text="Verser d'argent",
                                       text_font=("Poppins", "12")
                                       )
exporter_btn.place(relx=0.13, rely=0.5, anchor=tkinter.CENTER)

quitter_btn = customtkinter.CTkButton(client_services_frame,
                                      corner_radius=0,
                                      width=250,
                                      height=50,
                                      text="Quitter",
                                      text_font=("Poppins", "12"),
                                      command=quitter_btn_command
                                      )
quitter_btn.place(relx=0.13, rely=0.6, anchor=tkinter.CENTER)

bnj_text = customtkinter.CTkLabel(client_services_frame,
                                  text="Bonjour dans le menu de client",
                                  text_font=("Poppins", "20"),
                                  text_color="white"
                                  )
