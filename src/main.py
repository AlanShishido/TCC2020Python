
# tudo importado do GUI tkinter
import tkinter as tk
from tkinter import ttk

#Importando funções e classes de um script criado
from rootCreate import window

# pip install pillow
from PIL import ImageTk, Image


# criando a janela principal e tela inteira
root = tk.Tk()
root.title("Qualidade dos Nutrientes da Hidroponia de alface")
root.iconphoto(False, tk.PhotoImage(file="assets/alface-icon.png"))
pad = 15
root.geometry("{0}x{1}+0+-3".format(root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad))
root["bg"] = "#6534ff"

# criando tab na janela principal
tabControl = ttk.Notebook(root)
win1 = ttk.Frame(tabControl)
win2 = ttk.Frame(tabControl)

tabControl.add(win1, text="Dashboard")
tabControl.add(win2, text="Configurações")

# Implementação de dados para janela 1
# background
img1 = ImageTk.PhotoImage(Image.open("assets/bg.jpg"))
background1 = tk.Label(win1, image=img1)
background1.place(x=0, y=win1.winfo_screenheight()/6, relwidth=1, relheight=1)

bt = tk.Button(win1, text="CLIQUE1")
bt.pack()

# Implementação de dados para janela 2
img2 = ImageTk.PhotoImage(Image.open("assets/bg-config.png"))
background2 = tk.Label(win2, image=img2)
background2.place(x=0, y=0, relwidth=1, relheight=1)

bt2 = tk.Button(win2, text="CLIQUE2")
bt2.pack()

tabControl.pack(expand=1, fill='both')
root.mainloop()
