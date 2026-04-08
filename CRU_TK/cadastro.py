import tkinter as tk
from conexao import conectar

def abrir_cadastro():
    tela = tk.Toplevel()
    tela.title("Cadastro")

    nome = tk.Entry(tela)
    nome.pack()

    email = tk.Entry(tela)
    email.pack()

    def salvar():
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome.get(), email.get())
            )

        conn.commit()
        conn.close()

    tk.Button(tela, text="Salvar", command = salvar).pack()

