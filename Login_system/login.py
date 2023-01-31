from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
#cores ----------------------
preto = "#f0f3f5"
branco = "#feffff"
verde = "#3fb5a3"
azul = "#38576b"
azul_cinzento = "#708090"
letra = "#2F4F4F"
# Criação window ----------------------
window = Tk()
window.title("MAIN PAGE")
window.geometry("300x300")
window.configure(background = branco)
window.resizable(width=FALSE, height=FALSE)

# Criação user window ----------------------
def user_window():

    window = Tk()
    window.title("USER PAGE")
    window.geometry("1920x1080")
    window.configure(background = branco)
    window.resizable(width=FALSE, height=FALSE)
    nome = entry_nome.get()
    # Nome do usuário ----------------------
    label_nome = Label(window, text = nome, anchor=NW, font = ("Arial Rounded MT Bold", 40), bg=branco, fg=azul_cinzento)
    label_nome.place(x=10, y=15)
    linha_separadora_1 = Label(window, text = "", width= 1920, anchor=NW, font = ("Arial", 1), bg=azul, fg=letra)
    linha_separadora_1.place(x=0, y=80)

    # Botão de sair 
    b_sair = Button(window, text="Sair", command = window.quit, width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Arial Rounded MT Bold", 20),bg=branco, fg=letra)
    b_sair.place(x=1770, y=15)

# Programação dos Entries ----------------------
Base_de_dados = ["Administrador", "Administrador"]
# Função Login ----------------------
def login():
    if len(Base_de_dados) == 2:
        messagebox.showinfo("LOGIN PAGE","Não existem utilizadores registados.")
        return False
    nome = entry_nome.get()
    password = entry_password.get()
    if nome in Base_de_dados:
        index_nome = Base_de_dados.index(nome)
        index_password = index_nome + 1
        if password == Base_de_dados[index_password]:
            messagebox.showinfo("LOGIN PAGE","Login iniciado com sucesso.")
            return user_window()
        else:
            messagebox.showinfo("LOGIN PAGE","Nome ou palavra passe incorreta.")
    else:
        messagebox.showinfo("LOGIN PAGE","Nome ou palavra passe incorreta.")
#F Função Registar ----------------------   
def registar():
    nome = entry_nome.get()
    password = entry_password.get()
    if nome in Base_de_dados:
        print("Nome já em uso.")
    else:
        Base_de_dados.append(nome)
        Base_de_dados.append(password)
        messagebox.showinfo("REGISTER PAGE","Novo utilizador registado com sucesso.")
        return Base_de_dados
    
# Divisão window ----------------------
subwindow_cima = Frame(window, width=300, height=50, bg=branco,relief="flat")
subwindow_cima.grid(row=0, column=0, padx=0, pady=1, sticky=NSEW)

subwindow_baixo = Frame(window, width=300, height=250, bg=azul,relief="flat")
subwindow_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

# Configuração da window do subwindow_cima ----------------------
nome_pagina = Label(subwindow_cima, text = "LOGIN", anchor=NE, font = ("Arial Rounded MT Bold", 23), bg=branco, fg=letra)
nome_pagina.place(x=5, y=5)

linha_separadora = Label(subwindow_cima, text = "", width= 275,anchor=NW, font = ("Arial", 1), bg=azul, fg=letra)
linha_separadora.place(x=10, y=40)

# Configuração da window do subwindow_baixo ----------------------
label_nome = Label(subwindow_baixo, text = "Nome  *", anchor=NW, font = ("Arial Rounded MT Bold", 15), bg=azul, fg=branco)
label_nome.place(x=10, y=20)
entry_nome = Entry(subwindow_baixo, width=22, justify="left", font=("", 15), highlightthickness=1, relief="solid")
entry_nome.place(x=14, y=50)

label_password = Label(subwindow_baixo, text = "Palavra Passe  *", anchor=NW, font = ("Arial Rounded MT Bold", 15), bg=azul, fg=branco)
label_password.place(x=10, y=90)
entry_password = Entry(subwindow_baixo, width=22, justify="left",show="*", font=("", 15), highlightthickness=1, relief="solid")
entry_password.place(x=14, y=120)
#Button login ----------------------
b_entrar = Button(subwindow_baixo, text="Entrar",command=login ,width=6, height=1, relief=RAISED, overrelief=RIDGE, font=("Arial Rounded MT Bold", 15),bg=branco, fg=letra)
b_entrar.place(x=14, y=180)
#Button registar ----------------------
b_registar = Button(subwindow_baixo, text="Registar",command=registar, width=6, height=1, relief=RAISED, overrelief=RIDGE,  font=("Arial Rounded MT Bold", 15),bg=branco, fg=letra)
b_registar.place(x=109, y=180)
#Button Sair ----------------------
b_sair = Button(subwindow_baixo, text="Sair", command=window.quit, width=6, height=1, relief=RAISED, overrelief=RIDGE,  font=("Arial Rounded MT Bold", 15),bg=branco, fg=letra)
b_sair.place(x=203, y=180)

window.mainloop()