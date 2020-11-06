# Definindo as funções com base nas operações que precisamos.
# Para retornar apenas o resultado utilize no lugar do print
# a instrução 'retorn resultado'.
#*************************************************************
def soma(x, y):
    resultado = x + y
    print("{} + {} = {:3.2f}".format(x, y, resultado))

def subtracao(x, y):
    resultado = x - y
    print("{} - {} = {:3.2f}".format(x, y, resultado))

def multiplicacao(x, y):
    resultado = x * y
    print("{} x {} = {:3.2f}".format(x, y, resultado))

def divisao(x, y):
    resultado = x / y
    print("{} / {} = {:3.2f}".format(x, y, resultado))
