import random

# Definindo uma função para conter o jogo, estamos transformando este
# arquivo em um módulo.
def jogar_adivinhacao():
    print("****************************************")
    print("*** Bem-vindo ao Jogo de Adivinhação ***")
    print("****************************************")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000 # Cada jogada é iniciada com 1000 pontos

    # Apresentando níveis de dificuldde
    print("* Qual nível de dificuldade você quer? *")
    print("* (1) Fácil | (2) Médio | (3) Difícil  *")
    print("****************************************")

    # Capturando escolha do jogador via teclado
    nivel = int(input("Digite o nível: "))

    # Setando a variável 'total_tentativas' a partir do nível escolhido pelo
    # jogador onde 1 = 20 tentativas, 2 = 10 tetaticas e 3 = 5 tentativas.
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

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
            print("Você acertou! Sua pontuação é {}".format(pontos), end="\n\n")
            break # Encerra o jogo e sai do loop
        else:
            if (maior):
                print("Você errou! Tente um número MENOR.", end="\n\n")
            elif (menor):
                print("Você errou! Tente um número MAIOR.", end="\n\n")

            # Calculando os pontos que serão perdidos a cada erro comedito pelo jogador.
            # A diferença entre o número secreto e o número digitado será contada a cada
            # erro cometido pelo jogador. Ao final, a pontuação atualizada será mostrada
            # quando o jogador acertar o numero secreto.
            pontos_perdidos = abs(numero_digitado - numero_secreto) # abs(-47) = 47
            pontos = pontos - pontos_perdidos
    print("Fim de jogo!")

# Verificando se a variável __name__ foi setada com o valor __main__, se ela for setada
# com esse valor significa que este arquivo será considerado principal então entrará no
# bloco para executar a função que está sendo chamada.
# Basicamente o if verifica se este programa é o programa principal, pois caso esteja
# sendo importado para ser executado a partir de uma chamada de função, a variável não
# estará setada com o valor __main__, indicando que é apenas um módulo.
# Agora, caso tente executar esse arquivo diretamente no console, então essa variável
# será setada com o valor __main__ e rodará como se fosse o programa principal. Isso se
# chama modularização de arquivos.
if (__name__ == "__main__"):
    jogar_adivinhacao()