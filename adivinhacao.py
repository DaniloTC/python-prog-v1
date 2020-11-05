print("**************************************")
print("** Bem-vindo ao Jogo de Adivinhação **")
print("**************************************")

numero_secreto = 10
total_tentativas = 3
rodada = 1

# Limitando a quantidade de jogadas
while(rodada <= total_tentativas):
    print("Tentativa: {} de {}".format(rodada, total_tentativas)) # interpolação de string
    numero_digitado = int(input("Adivinhe qual é o número secreto: ")) # convertendo entrada para int

    acertou = numero_digitado == numero_secreto
    maior   = numero_digitado >  numero_secreto
    menor   = numero_digitado <  numero_secreto

    # Processando a jogada para devolver um resultado
    if (acertou):
        print("Você acertou! Parabéns!")
    else:
        if (maior):
            print("Você errou! Tente um número MENOR.")
        elif (menor):
            print("Você errou! Tente um número MAIOR.")
    rodada = rodada + 1 # Evitando looping infinito (necessário apenas no while)
print("Fim de jogo!")