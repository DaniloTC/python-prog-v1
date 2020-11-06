import adivinhacao
import imc
import matematica

def inicial():
    # Apresentando opções para o usuário
    print("***************************")
    print("***  Escolha uma opção  ***")
    print("***************************")
    print("* (1) Jogo de Adivinhação *")
    print("* (2) Matemática          *")
    print("* (3) Calcular IMC        *")
    print("***************************")

    # Capturando escolha do usuário
    escolha = int(input("O que deseja fazer? "))

    # Processando a escolha do usuário e executando o programa
    # que foi escolhido a partir do menu.
    if (escolha == 1):
        adivinhacao.jogar_adivinhacao()
    elif (escolha == 2):
        matematica.operacoes()
    elif (escolha == 3):
        imc.calcular_imc()
    else:
        print("Calcular imc")

# Modularizando este arquivo
if(__name__ == "__main__"):
    inicial()