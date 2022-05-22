import tkinter
import customtkinter
import config
import json
import agent


def quitter_gant_btn():
    agent_services_frame.place_forget()
    agent_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def ajouter_btn_command():
    supprimer_msg.place_forget()
    nom_client_supp.place_forget()
    supp_btn.place_forget()
    message_supp_error.place_forget()
    message_supp.place_forget()
    nom_client_ajout.place(relx=0.6, rely=0.45, anchor=tkinter.CENTER)
    solde_client_ajout.place(relx=0.6, rely=0.55, anchor=tkinter.CENTER)
    ajouter_msg.place(relx=0.6, rely=0.35, anchor=tkinter.CENTER)
    confirm_btn.place(relx=0.6, rely=0.65, anchor=tkinter.CENTER)
    message_ajout.place(relx=0.6, rely=0.75, anchor=tkinter.CENTER)
    message_ajout_error.place(relx=0.6, rely=0.75, anchor=tkinter.CENTER)


def supprimer_btn_command():
    ajouter_msg.place_forget()
    nom_client_ajout.place_forget()
    solde_client_ajout.place_forget()
    confirm_btn.place_forget()
    message_ajout.place_forget()
    message_ajout_error.place_forget()
    supprimer_msg.place(relx=0.6, rely=0.35, anchor=tkinter.CENTER)
    nom_client_supp.place(relx=0.6, rely=0.45, anchor=tkinter.CENTER)
    supp_btn.place(relx=0.6, rely=0.55, anchor=tkinter.CENTER)
    message_supp_error.place(relx=0.6, rely=0.65, anchor=tkinter.CENTER)
    message_supp.place(relx=0.6, rely=0.65, anchor=tkinter.CENTER)


def agent_services_func():
    agent_frame.place_forget()
    bnj_text.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
    agent_services_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


agent_services_frame = customtkinter.CTkFrame(
    width=900, height=600, bg="gray10")


ajouter_btn = customtkinter.CTkButton(agent_services_frame,
                                      corner_radius=0,
                                      width=250,
                                      height=50,
                                      text="Ajouter client",
                                      text_font=("Poppins", "12"),
                                      command=ajouter_btn_command
                                      )
ajouter_btn.place(relx=0.13, rely=0.3, anchor=tkinter.CENTER)

supprimer_btn = customtkinter.CTkButton(agent_services_frame,
                                        corner_radius=0,
                                        width=250,
                                        height=50,
                                        text="Supprimer client",
                                        text_font=("Poppins", "12"),
                                        command=supprimer_btn_command
                                        )
supprimer_btn.place(relx=0.13, rely=0.4, anchor=tkinter.CENTER)


exporter_btn = customtkinter.CTkButton(agent_services_frame,
                                       corner_radius=0,
                                       width=250,
                                       height=50,
                                       text="Exporter list des clients",
                                       text_font=("Poppins", "12")
                                       )
exporter_btn.place(relx=0.13, rely=0.5, anchor=tkinter.CENTER)

quitter_btn = customtkinter.CTkButton(agent_services_frame,
                                      corner_radius=0,
                                      width=250,
                                      height=50,
                                      text="Quitter",
                                      text_font=("Poppins", "12"),
                                      command=quitter_gant_btn
                                      )
quitter_btn.place(relx=0.13, rely=0.6, anchor=tkinter.CENTER)

bnj_text = customtkinter.CTkLabel(agent_services_frame,
                                  text="Bonjour dans le menu d'administration",
                                  text_font=("Poppins", "20"),
                                  text_color="white"
                                  )

# ajouter client section

ajouter_msg = customtkinter.CTkLabel(agent_services_frame,
                                     text="Ajouter un client",
                                     text_font=("Poppins", "16"),
                                     text_color="white"
                                     )


nom_client_ajout = customtkinter.CTkEntry(agent_services_frame,
                                          placeholder_text="Nom de client",
                                          width=500,
                                          text_font=("Poppins", "10"),
                                          fg_color="gray10",
                                          )


solde_client_ajout = customtkinter.CTkEntry(agent_services_frame,
                                            placeholder_text="Solde initial",
                                            width=500,
                                            text_font=("Poppins", "10"),
                                            fg_color="gray10",
                                            )


confirm_btn = customtkinter.CTkButton(agent_services_frame,
                                      corner_radius=10,
                                      width=120,
                                      height=30,
                                      text="Confirmer",
                                      text_font=("Poppins", "10")
                                      )


message_ajout = customtkinter.CTkLabel(agent_services_frame,
                                       text="Le client a été ajouté avec succès",
                                       text_font=("Poppins", "10"),
                                       text_color="green",
                                       )


message_ajout_error = customtkinter.CTkLabel(agent_services_frame,
                                             text="Le client a été dejà ajouté",
                                             text_font=("Poppins", "10"),
                                             text_color="red",
                                             )


# supprimer client section

supprimer_msg = customtkinter.CTkLabel(agent_services_frame,
                                       text="Supprimer un client",
                                       text_font=("Poppins", "16"),
                                       text_color="white"
                                       )


nom_client_supp = customtkinter.CTkEntry(agent_services_frame,
                                         placeholder_text="Nom de client",
                                         width=500,
                                         text_font=("Poppins", "10"),
                                         fg_color="gray10",
                                         )


supp_btn = customtkinter.CTkButton(agent_services_frame,
                                   corner_radius=10,
                                   width=120,
                                   height=30,
                                   text="Supprimer",
                                   text_font=("Poppins", "10")
                                   )


message_supp = customtkinter.CTkLabel(agent_services_frame,
                                      text="Le client a été supprimer avec succès",
                                      text_font=("Poppins", "10"),
                                      text_color="green",
                                      )


message_supp_error = customtkinter.CTkLabel(agent_services_frame,
                                            text="Le client n'existe pas",
                                            text_font=("Poppins", "10"),
                                            text_color="red",
                                            )
