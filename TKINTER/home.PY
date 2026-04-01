import tkinter as tk

janela = tk.Tk()
janela.geometry("400x200")
janela.title("Estácio 2026.1")


label = tk.Label(janela, text="Hello world!")
label.pack()

def clicar():
    label.config(text="Conseguimos, finalmente!")

botao = tk.Button(janela, text="Clique me", command=clicar)
botao.pack()










janela.mainloop()