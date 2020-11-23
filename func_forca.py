import random

def imprime_mensagem_abertura():
    print("*****************************")
    print("Bem-vindo(a) ao jogo da Forca")
    print("*****************************")

def carrega_palavra_secreta_de_arquivo():
    arquivo = open("palavras.txt", "r") # abre arquivo existente em modo leitura
    palavras = []
    for linha in arquivo:
        linha = linha.strip() # limpa string removendo caracter de scape
        palavras.append(linha) # adiciona conteúdo de cada linha na lista
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def chute_do_jogador():
    chute = input("Qual o seu chute? ")
    chute = chute.strip().upper() # limpa espaços e transforma em maiúscula
    return chute

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________       ")
    print("   /               \      ")
    print("  /                 \     ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /  ")
    print(" |   XXXX     XXXX   |/   ")
    print(" |   XXX       XXX   |    ")
    print(" |                   |    ")
    print(" \__      XXX      __/    ")
    print("   |\     XXX     /|      ")
    print("   | |           | |      ")
    print("   | I I I I I I I |      ")
    print("   |  I I I I I I  |      ")
    print("   \_             _/      ")
    print("     \_         _/        ")
    print("       \_______/          ")
