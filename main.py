# Codigo Principal

# tudo importado do GUI tkinter
import tkinter as tk
from tkinter import ttk

# utilizar para passar parametros na função, já que no command= recebe a instancia da função
from functools import partial

#Importando funções e classes de um script criado
import databaseSqlite3 
import functions as sf

db = databaseSqlite3.database()

# pip install pillow
from PIL import ImageTk, Image

# db.dbCriarTabela()
# db.dbInserirDados([(sf.DataHora("data"),sf.DataHora("tempo"),500,5.5,30,26,20)])
# db.dbLerTodosDados()

# variavel = tk.StringVar()
verde = "#65aa34"


print(sf.DataHora("tempo"))
# criando a janela principal e tela inteira
root = tk.Tk()
root.title("Qualidade dos Nutrientes da Hidroponia de alface")
root.iconphoto(False, tk.PhotoImage(file="assets/alface-icon.png"))
pad = 15
widthMaxPx = root.winfo_screenwidth()
heightMaxPx = root.winfo_screenheight()
root.geometry("{0}x{1}+0+-3".format(widthMaxPx-pad, heightMaxPx-pad))
root["bg"] = verde
# cabeçalho
ctHeader = tk.Frame(root, bg=verde)
lbH1 = tk.Label(ctHeader, text="Hidroponia", bg=verde, font=("Roboto",20))
lbH2 = tk.Label(ctHeader, text="Olá, Waldir", bg="green", padx=200)

ctHeader.pack(side=tk.TOP,fill='x')
lbH1.pack(side=tk.LEFT, expand=1)
lbH2.pack(side=tk.RIGHT, fill='y')


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

bt = tk.Button(win1, text="CLIQUE1", command=sf.botao1)
bt.pack()

# Implementação de dados para janela 2
img2 = ImageTk.PhotoImage(Image.open("assets/bg-config.png"))
background2 = tk.Label(win2, image=img2)
background2.place(x=0, y=0, relwidth=1, relheight=1)

bt2 = tk.Button(win2, text="CLIQUE2")
bt2.pack()

tabControl.pack(expand=1, fill='both')
root.mainloop()
