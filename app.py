import customtkinter
from PIL import ImageTk, Image
import config
import client
import agent

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("./img/logo.png"))

label = customtkinter.CTkLabel(config.menu_frame, image=img)
label.pack()

# Create Buttons

client_btn = customtkinter.CTkButton(config.menu_frame,
                                     text="Entrer comme un client",
                                     width=250,
                                     height=50,
                                     bg="gray10",
                                     text_font=("Poppins", "12", "bold"),
                                     command=client.client_page)
client_btn.pack(pady=20)

agent_btn = customtkinter.CTkButton(config.menu_frame,
                                    text="Entrer comme un agent",
                                    width=250,
                                    height=50,
                                    text_font=("Poppins", "12", "bold"),
                                    command=agent.agent_page,
                                    )
agent_btn.pack()


config.root_tk.mainloop()
