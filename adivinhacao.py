print("**************************************")
print("** Bem-vindo ao Jogo de Adivinhação **")
print("**************************************")

numero_secreto = 10
total_tentativas = 3

# Limitando a quantidade de jogadas
for rodada in range(1, total_tentativas + 1):
    print("Tentativa: {} de {}".format(rodada, total_tentativas)) # interpolação de string
    numero_digitado = int(input("Qual é o número secreto entre 1 e 100: ")) # convertendo entrada para int

    if (numero_digitado < 1 or numero_digitado > 100):
        print("Valor inválido, digite um número entre 1 e 100.")
        continue # Aborta a iteração atual e pula para a próxima

    acertou = numero_digitado == numero_secreto
    maior   = numero_digitado >  numero_secreto
    menor   = numero_digitado <  numero_secreto

    # Processando a jogada para devolver um resultado
    if (acertou):
        print("Você acertou! Parabéns!", end="\n\n")
        break # Encerra o jogo e sai do loop
    else:
        if (maior):
            print("Você errou! Tente um número MENOR.", end="\n\n")
        elif (menor):
            print("Você errou! Tente um número MAIOR.", end="\n\n")
print("Fim de jogo!")