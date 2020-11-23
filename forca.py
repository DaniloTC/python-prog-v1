def jogar_forca():
    print("*****************************")
    print("Bem-vindo(a) ao jogo da Forca")
    print("*****************************")

    palavra_secreta = "banana".upper() # por enquanto a palavra secreta permenecerá fixa
    letras_acertadas = ["_","_","_","_","_","_"] # permanecerá fixa por enquanto

    enforcou = False
    acertou = False

    print(letras_acertadas) # mostra quantidade de letras na palavra

    while (not enforcou and not acertou):

        chute = input("Escolha uma letra? ").strip().upper() # limpa espaços e transforma em maiúscula
        index = 0

        for letra in palavra_secreta:
            if (chute == letra):
                letras_acertadas[index] = letra
            index += 1
        
        print(letras_acertadas) # coloca letra acertada na posição certa dentro da palavra

        # lógica para sair do while.
        # redefinir variável 'enforcou' caso não exista o caractere ( _ ) na lista.
        acertou = "_" not in letras_acertadas

    print("Fim de jogo!")

if (__name__ == "__main__"):
    jogar_forca()
