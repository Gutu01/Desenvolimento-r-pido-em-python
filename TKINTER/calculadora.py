import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora Estácio")
entrada = tk.Entry(janela, width=25)
entrada.grid(row=0, column=0, columnspan=4)

def clicar(valor):
    atual = entrada.get()
    entrada.delete(0,tk.END)
    entrada.insert(0, atual +str(valor))

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0,tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "ERRO")

def limpar():
    entrada.delete(0, tk.END)




botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for(texto, linha, coluna) in botoes:
    if texto == "=":
        tk.Button(janela, text = texto, width=5, command=calcular).grid(row=linha, column = coluna)
    elif texto == "C":
        tk.Button(janela, text = texto, width=5, command=limpar).grid(row=linha, column = coluna)
    else:
        tk.Button(janela, text = texto, width=5, command=lambda t=texto:clicar(t)).grid(row=linha, column = coluna)











janela.mainloop()