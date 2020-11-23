import func_forca as func

def jogar_forca():
    func.imprime_mensagem_abertura()
    palavra_secreta = func.carrega_palavra_secreta_de_arquivo()
    letras_acertadas = func.inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print("Palavra:", letras_acertadas) # mostra quantidade de letras na palavra

    while (not enforcou and not acertou):
        chute = func.chute_do_jogador()
        
        if(chute in palavra_secreta):
            func.marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            func.desenha_forca(erros)
        
        print(letras_acertadas, end="\n\n") # coloca letra acertada na posição certa dentro da palavra

        # lógica para sair do while.
        acertou = "_" not in letras_acertadas
        enforcou = erros == 7

    # mensagem se acertou ou errou
    if(acertou):
        func.imprime_mensagem_vencedor()
    elif(enforcou):
        func.imprime_mensagem_perdedor(palavra_secreta)

if (__name__ == "__main__"):
    jogar_forca()