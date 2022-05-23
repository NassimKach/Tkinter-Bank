import tkinter
import customtkinter
import config
import json


with open("data\\client.json", "r") as f:
    client_data = json.load(f)

# def retirer_argent_command():


def client_services_func():
    client_frame.place_forget()
    client_services_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    bnj_text = customtkinter.CTkLabel(client_services_frame,
                                      text=f"Bonjour {nom} dans le menu de client",
                                      text_color="white",
                                      )
    bnj_text.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)


def quitter_btn_command():
    client_services_frame.place_forget()
    client_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def entrer_client_btn_clicked():
    # Get the values from the entries
    global nom

    nom = nom_entry.get()
    mpc = mpc_entry.get()

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

    for i in client_data:
        if i["nom"] == nom and i["mot de passe"] == mpc:
            client_services_func()
            return

    showerror.configure(text="Nom ou mot de passe incorrect",
                        text_color="red")


def afficher_solde_func():
    for i in client_data:
        if i["nom"] == nom:
            afficher_sold_text.configure(text=f"Votre solde est de {i['sold']}€",
                                         text_color="white",
                                         text_font=("Poppins", "20"))
            return


# def retirer_argent_func():
#     for i in client_data:
#         if i["nom"] == nom:
#             i["sold"] -= int(retirer_argent_entry.get())
#             afficher_solde_func()
#             return


def client_page():
    config.menu_frame.place_forget()
    client_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def retour_menu():
    client_frame.place_forget()
    config.menu_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


client_services_frame = customtkinter.CTkFrame(
    width=900, height=600, bg="gray10")

afficher_sold = customtkinter.CTkButton(client_services_frame,
                                        corner_radius=0,
                                        width=250,
                                        height=50,
                                        text="Afficher le solde",
                                        text_font=("Poppins", "12"),
                                        command=afficher_solde_func
                                        )
afficher_sold.place(relx=0.13, rely=0.3, anchor=tkinter.CENTER)

afficher_sold_text = customtkinter.CTkLabel(client_services_frame,
                                            text="",
                                            text_font=("Poppins", "12"),
                                            text_color="white"
                                            )
afficher_sold_text.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

retirer_btn = customtkinter.CTkButton(client_services_frame,
                                      corner_radius=0,
                                      width=250,
                                      height=50,
                                      text="Retirer d'argent",
                                      text_font=("Poppins", "12"),
                                    #   command=retirer_argent_command
                                      )
retirer_btn.place(relx=0.13, rely=0.4, anchor=tkinter.CENTER)


verser_btn = customtkinter.CTkButton(client_services_frame,
                                     corner_radius=0,
                                     width=250,
                                     height=50,
                                     text="Verser d'argent",
                                     text_font=("Poppins", "12")
                                     )
verser_btn.place(relx=0.13, rely=0.5, anchor=tkinter.CENTER)

quitter_btn = customtkinter.CTkButton(client_services_frame,
                                      corner_radius=0,
                                      width=250,
                                      height=50,
                                      text="Quitter",
                                      text_font=("Poppins", "12"),
                                      command=quitter_btn_command
                                      )
quitter_btn.place(relx=0.13, rely=0.6, anchor=tkinter.CENTER)


client_frame = customtkinter.CTkFrame(
    config.root_tk, width=900, height=600, bg="gray10")

# Create a bvn text

bvn_txt = customtkinter.CTkLabel(client_frame,
                                 text="Bienvenue a la banque",
                                 text_font=("Poppins", "32", "bold"),
                                 )
bvn_txt.pack()

# Create a sub text

sub_txt = customtkinter.CTkLabel(client_frame,
                                 text="connecter comme un client",
                                 text_font=("Poppins", "16"))
sub_txt.pack(pady=20)

# Create a login section

nom_entry = customtkinter.CTkEntry(client_frame,
                                   placeholder_text="Nom",
                                   width=300,
                                   text_font=("Poppins", "10"),
                                   fg_color="gray10",
                                   )
nom_entry.pack(pady=20)

mpc_entry = customtkinter.CTkEntry(client_frame,
                                   placeholder_text="Mot de pass",
                                   width=300,
                                   text_font=("Poppins", "10"),
                                   fg_color="gray10",
                                   )
mpc_entry.pack()

entrer_btn = customtkinter.CTkButton(client_frame,
                                     text="Entrer",
                                     text_font=("Poppins", "12", "bold"),
                                     bg="gray10",
                                     command=entrer_client_btn_clicked)
entrer_btn.pack(pady=20)

quitter_btn = customtkinter.CTkButton(client_frame,
                                      text="Quitter",
                                      bg="gray10",
                                      text_font=("Poppins", "12", "bold"),
                                      command=retour_menu)
quitter_btn.pack()

showerror = customtkinter.CTkLabel(client_frame,
                                   text="",
                                   text_font=("Poppins", "12"),
                                   )
showerror.pack(pady=20)

argent_retirer_entry = customtkinter.CTkEntry(client_frame,
                                              placeholder_text="Montant à retirer",
                                              width=300,
                                              text_font=("Poppins", "10"),
                                              fg_color="gray10",
                                              )
