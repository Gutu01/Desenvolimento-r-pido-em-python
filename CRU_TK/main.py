import tkinter as tk
from cadastro import abrir_cadastro

janela = tk.Tk()
janela.title("Sistema CRUD")

tk.Label(janela, text = "MENU PRINCIPAL", font=("Arial", 16)).pack(pady=10)

tk.Button(janela,text="Cadastrar", command=abrir_cadastro).pack(pady=5)

janela.mainloop()