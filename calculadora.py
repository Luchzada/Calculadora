import tkinter as tk

janela = tk.Tk()

numero_anterior = 0
operacao_atual = ""


def digitar_7():
    visor.insert(tk.END, "7")
   
def digitar_8():
    visor.insert(tk.END, "8")
    
def digitar_9():
    visor.insert(tk.END, "9")

def digitar_4():
    visor.insert(tk.END, "4")

def digitar_5():
    visor.insert(tk.END, "5")

def digitar_6():
    visor.insert(tk.END, "6")

def digitar_1():
    visor.insert(tk.END, "1")

def digitar_2():
    visor.insert(tk.END, "2")

def digitar_3():
    visor.insert(tk.END, "3")

def digitar_0():
    visor.insert(tk.END, "0")
    
def limpar():
    global numero_anterior, operacao_atual
    visor.delete(0, tk.END)
    numero_anterior = 0
    operacao_atual = ""

def apagar():
    ultimo = len(visor.get()) - 1
    if ultimo >= 0:
        visor.delete(ultimo)


def escolher_operacao(operacao):
    global numero_anterior, operacao_atual
    texto = visor.get()
    if texto == "":
        return
    numero_anterior = float(texto)
    operacao_atual = operacao
    visor.delete(0, tk.END)


def digitar_soma():
    escolher_operacao("+")

def digitar_subtracao():
    escolher_operacao("-")

def digitar_multiplicacao():
    escolher_operacao("×")

def digitar_divisao():
    escolher_operacao("÷")


def digitar_resultado():
    global numero_anterior, operacao_atual
    texto = visor.get()
    if operacao_atual == "" or texto == "":
        return

    numero_atual = float(texto)

    if operacao_atual == "+":
        resultado = numero_anterior + numero_atual
    elif operacao_atual == "-":
        resultado = numero_anterior - numero_atual
    elif operacao_atual == "×":
        resultado = numero_anterior * numero_atual
    elif operacao_atual == "÷":
        if numero_atual == 0:
            visor.delete(0, tk.END)
            visor.insert(0, "Erro")
            numero_anterior = 0
            operacao_atual = ""
            return
        resultado = numero_anterior / numero_atual

    if resultado == int(resultado):
        resultado = int(resultado)

    visor.delete(0, tk.END)
    visor.insert(0, str(resultado))
    numero_anterior = 0
    operacao_atual = ""


def digitar_ponto():
    visor.insert(tk.END, ".")


def digitar_porcentagem():
    texto = visor.get()
    if texto == "":
        return
    resultado = float(texto) / 100
    if resultado == int(resultado):
        resultado = int(resultado)
    visor.delete(0, tk.END)
    visor.insert(0, str(resultado))


visor = tk.Entry(janela, width=32, justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

botao_7 = tk.Button(janela, text="7", width=6, command=digitar_7)
botao_7.grid(row=2, column=0, padx=2, pady=2)

botao_8 = tk.Button(janela, text="8", width=6, command=digitar_8)
botao_8.grid(row=2, column=1, padx=2, pady=2)

botao_9 = tk.Button(janela, text="9", width=6, command=digitar_9)
botao_9.grid(row=2, column=2, padx=2, pady=2,)

botao_4 = tk.Button(janela, text="4", width=6, command=digitar_4)
botao_4.grid(row=3, column=0, padx=2, pady=2)

botao_5 = tk.Button(janela, text="5", width=6, command=digitar_5)
botao_5.grid(row=3, column=1, padx=2, pady=2)

botao_6 = tk.Button(janela, text="6", width=6, command=digitar_6)
botao_6.grid(row=3, column=2, padx=2, pady=2)

botao_1 = tk.Button(janela, text="1", width=6, command=digitar_1)
botao_1.grid(row=4, column=0, padx=2, pady=2)

botao_2 = tk.Button(janela, text="2", width=6, command=digitar_2)
botao_2.grid(row=4, column=1, padx=2, pady=2)

botao_3 = tk.Button(janela, text="3", width=6, command=digitar_3)
botao_3.grid(row=4, column=2, padx=2, pady=2)

botao_0 = tk.Button(janela, text="0", width=6, command=digitar_0)
botao_0.grid(row=5, column=1, padx=2, pady=2)

botao_c = tk.Button(janela, text="C", width=6, command=limpar)
botao_c.grid(row=1, column=0, padx=2, pady=2)

botao_apagar = tk.Button(janela, text="⌫", width=6, command=apagar)
botao_apagar.grid(row=1, column=1, padx=2, pady=2)

botao_soma = tk.Button(janela, text="+", width=6, command=digitar_soma)
botao_soma.grid(row=4, column=3, padx=2, pady=2)

botao_subtracao = tk.Button(janela, text="-", width=6, command=digitar_subtracao)
botao_subtracao.grid(row=3, column=3, padx=2, pady=2)

botao_multiplicacao = tk.Button(janela, text="×", width=6, command=digitar_multiplicacao)
botao_multiplicacao.grid(row=2, column=3, padx=2, pady=2)

botao_divisao = tk.Button(janela, text="÷", width=6, command=digitar_divisao)
botao_divisao.grid(row=1, column=3, padx=2, pady=2)

botao_resultado = tk.Button(janela, text="=", width=6, command=digitar_resultado)
botao_resultado.grid(row=5, column=3, padx=2, pady=2)

botao_ponto = tk.Button(janela, text=".", width=6, command=digitar_ponto)
botao_ponto.grid(row=5, column=2, padx=2, pady=2)

botao_porcentagem = tk.Button(janela, text="%", width=6, command=digitar_porcentagem)
botao_porcentagem.grid(row=1, column=2, padx=2, pady=2)

janela.mainloop()