import adivinhacao
import imc
import matematica
import forca
import calc_mu as mu
import calc_mf as mf

def inicial():
    # Apresentando opções para o usuário
    print("***********************************")
    print("*******  Escolha uma opção  *******")
    print("***********************************")
    print("* (1) Jogo de Adivinhação         *")
    print("* (2) Jogo da Forca               *")
    print("* (3) Matemática                  *")
    print("* (4) Calcular IMC                *")
    print("* (5) Calcular Média das Unidades *")
    print("* (6) Calcular Média Final        *")
    print("***********************************")

    # Capturando escolha do usuário
    escolha = int(input("O que deseja fazer? "))

    # Processando a escolha do usuário e executando o programa
    # que foi escolhido a partir do menu.
    if (escolha == 1):
        adivinhacao.jogar_adivinhacao()
    elif (escolha == 2):
        forca.jogar_forca()
    elif (escolha == 3):
        matematica.operacoes()
    elif (escolha == 4):
        imc.calcular_imc()
    elif (escolha == 5):
        mu.calcular_mu()
    elif (escolha == 6):
        mf.calcular_mf()
    else:
        print("Opção inválida.")

# Modularizando este arquivo
if(__name__ == "__main__"):
    inicial()