import tkinter
import customtkinter
import config
import json
import agent_services

with open("data\\agent.json", "r") as f:
    data = json.load(f)

global nom


def entrer_ag_btn_clicked():
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

    for i in data:
        if i["nom"] == nom and i["mot de passe"] == mpc:
            agent_services.agent_services_func()
            return

    showerror.configure(text="Nom ou mot de passe incorrect",
                        text_color="red")


def agent_page():
    config.menu_frame.place_forget()
    agent_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def retour_menu():
    agent_frame.place_forget()
    config.menu_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


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
