import random

def jogar_forca():
    print("*****************************")
    print("Bem-vindo(a) ao jogo da Forca")
    print("*****************************")

    # lendo arquivo e preparando lista de palavras
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip() # limpa string removendo caracter de scape
        palavras.append(linha) # adiciona conteúdo de cada linha na lista
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas) # mostra quantidade de letras na palavra

    while (not enforcou and not acertou):

        chute = input("Escolha uma letra? ").strip().upper() # limpa espaços e transforma em maiúscula
        index = 0

        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros +=1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))
        
        print(letras_acertadas) # coloca letra acertada na posição certa dentro da palavra

        # lógica para sair do while.
        acertou = "_" not in letras_acertadas
        enforcou = erros == 6

        # mesnagens se ganhar ou perder e sai do laço em ambos os casos.
        if(acertou):
            print("Parabéns, você ganhou!")
            break
        elif(enforcou):
            print("Puxa! Você perdeu! A palavra era {}".format(palavra_secreta))
            break

    print("Fim de jogo!")

if (__name__ == "__main__"):
    jogar_forca()
