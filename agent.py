import tkinter
import customtkinter
import config
import json
import pandas

with open("data\\agent.json", "r") as f_agent:
    agent_data = json.load(f_agent)

client_list = []


def entrer_ag_btn_clicked():

    global nom
    nom = nom_entry.get()
    mpc = mpc_entry.get()
    # Get the values from the entries
    showerror.configure(text="")

    if nom == "" and mpc == "":
        showerror.configure(text="Veuillez remplir tous les champs",
                            text_color="red")
        return
    elif nom == "":
        showerror.configure(text="Veuillez remplir le champ nom",
                            text_color="red")
        return

    elif mpc == "":
        showerror.configure(text="Veuillez remplir le champ mot de passe",
                            text_color="red")
        return

    for i in agent_data:
        if i["nom"] == nom and i["mot de passe"] == mpc:
            agent_services_func()
            return

    showerror.configure(text="Nom ou mot de passe incorrect",
                        text_color="red")


def quitter_agt_btn():
    agent_services_frame.place_forget()
    agent_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def ajouter_btn_command():
    supprimer_msg.place_forget()
    nom_client_supp.place_forget()
    supp_btn.place_forget()
    message_supp_error.place_forget()
    nom_client_ajout.place(relx=0.6, rely=0.45, anchor=tkinter.CENTER)
    solde_client_ajout.place(relx=0.6, rely=0.55, anchor=tkinter.CENTER)
    ajouter_msg.place(relx=0.6, rely=0.35, anchor=tkinter.CENTER)
    confirm_btn.place(relx=0.6, rely=0.65, anchor=tkinter.CENTER)
    message_ajout_error.place(relx=0.6, rely=0.75, anchor=tkinter.CENTER)


def supprimer_btn_command():
    ajouter_msg.place_forget()
    nom_client_ajout.place_forget()
    solde_client_ajout.place_forget()
    confirm_btn.place_forget()
    message_ajout_error.place_forget()
    supprimer_msg.place(relx=0.6, rely=0.35, anchor=tkinter.CENTER)
    nom_client_supp.place(relx=0.6, rely=0.45, anchor=tkinter.CENTER)
    supp_btn.place(relx=0.6, rely=0.55, anchor=tkinter.CENTER)
    message_supp_error.place(relx=0.6, rely=0.65, anchor=tkinter.CENTER)


def agent_services_func():
    agent_frame.place_forget()
    agent_services_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    bnj_text = customtkinter.CTkLabel(agent_services_frame,
                                      text=f"Bienvenue {nom} dans le service d'agent",
                                      text_font=("Poppins", "20"),
                                      text_color="white"
                                      )
    bnj_text.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)


def agent_page():
    config.menu_frame.place_forget()
    agent_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def retour_menu():
    agent_frame.place_forget()
    config.menu_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def ajouter_client():
    if nom_client_ajout.get() == "" or solde_client_ajout.get() == "":
        message_ajout_error.configure(text="Veuillez remplir tous les champs",
                                      text_color="red")
        return
    elif nom_client_ajout.get() == "":
        message_ajout_error.configure(text="Veuillez remplir le champ nom",
                                      text_color="red")
        return
    elif solde_client_ajout.get() == "":
        message_ajout_error.configure(text="Veuillez remplir le champ solde",
                                      text_color="red")
        return
    for i in client_list:
        if i["nom"] == nom_client_ajout.get():
            message_ajout_error.configure(text="Ce client existe déjà",
                                          text_color="red")
            return

    client_list.append({"nom": nom_client_ajout.get(),
                        "sold": solde_client_ajout.get()})

    with open("data\\client.json", "w") as f_client:
        json.dump(client_list, f_client, indent=2)

    message_ajout_error.configure(text="Client ajouté avec succès",
                                  text_color="green")


def supprimer_client():
    if nom_client_supp.get() == "":
        message_supp_error.configure(text="Veuillez remplir le champ nom",
                                     text_color="red")
        return

    for i in client_list:
        if i["nom"] == nom_client_supp.get():
            client_list.remove(i)
            with open("data\\client.json", "w") as f_client:
                json.dump(client_list, f_client, indent=2)
            message_supp_error.configure(text="Client supprimé avec succès",
                                         text_color="green")
            return

        elif i["nom"] != nom_client_supp.get():
            message_supp_error.configure(text="Ce client n'existe pas",
                                         text_color="red")
            return


def exporter_btn_command():
    pandas.DataFrame(client_list).to_csv("data\\client.csv", index=False)


agent_frame = customtkinter.CTkFrame(
    config.root_tk, width=900, height=600, bg="gray10")

# Create a bvn text
bvn_txt = customtkinter.CTkLabel(agent_frame,
                                 text="Bienvenue a la banque",
                                 text_font=("Poppins", "32", "bold"),
                                 )
bvn_txt.pack()

# Create a sub text

sub_txt = customtkinter.CTkLabel(agent_frame,
                                 text="connecter comme un agent",
                                 text_font=("Poppins", "16"))
sub_txt.pack(pady=20)

# Create a login section

nom_entry = customtkinter.CTkEntry(agent_frame,
                                   placeholder_text="Numero de compte",
                                   width=300,
                                   text_font=("Poppins", "10"),
                                   fg_color="gray10",
                                   )
nom_entry.pack(pady=20)


mpc_entry = customtkinter.CTkEntry(agent_frame,
                                   placeholder_text="Mot de pass",
                                   width=300,
                                   text_font=("Poppins", "10"),
                                   fg_color="gray10",
                                   )
mpc_entry.pack()

entrer_btn = customtkinter.CTkButton(agent_frame,
                                     text="Entrer",
                                     bg="gray10",
                                     text_font=("Poppins", "12", "bold"),
                                     command=entrer_ag_btn_clicked)
entrer_btn.pack(pady=20)

quitter_btn = customtkinter.CTkButton(agent_frame,
                                      text="Quitter",
                                      bg="gray10",
                                      text_font=("Poppins", "12", "bold"),
                                      command=retour_menu)
quitter_btn.pack()

showerror = customtkinter.CTkLabel(agent_frame,
                                   text="",
                                   text_font=("Poppins", "12"),
                                   )
showerror.pack(pady=20)

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
                                       text_font=("Poppins", "12"),
                                       command=exporter_btn_command
                                       )
exporter_btn.place(relx=0.13, rely=0.5, anchor=tkinter.CENTER)

quitter_btn = customtkinter.CTkButton(agent_services_frame,
                                      corner_radius=0,
                                      width=250,
                                      height=50,
                                      text="Quitter",
                                      text_font=("Poppins", "12"),
                                      command=quitter_agt_btn
                                      )
quitter_btn.place(relx=0.13, rely=0.6, anchor=tkinter.CENTER)


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
                                      text_font=("Poppins", "10"),
                                      command=ajouter_client
                                      )


message_ajout_error = customtkinter.CTkLabel(agent_services_frame,
                                             text="",
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
                                   text_font=("Poppins", "10"),
                                   command=supprimer_client
                                   )


message_supp_error = customtkinter.CTkLabel(agent_services_frame,
                                            text="",
                                            text_font=("Poppins", "10"),
                                            text_color="red",
                                            )
