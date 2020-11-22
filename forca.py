def jogar_forca():
    print("*****************************")
    print("Bem-vindo(a) ao jogo da Forca")
    print("*****************************")

    palavra_secreta = "banana" # por enquanto a palavra secreta permenecerá fixa

    enforcou  = False
    acertou = False

    while (not enforcou and not acertou):

        chute = input("Escolha uma letra? ")
        index = 0

        for letra in palavra_secreta:
            if (chute == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            else:
                index += 1

if (__name__ == "__main__"):
    jogar_forca()
