import func_matematica as f

# Definindo função contendo operações básicas de matemáticas
def operacoes():
    # Apresentando menu de opções
    print("***************************************************")
    print("***         ESCOLHA UMA OPÇÃO DO MENU           ***")
    print("***************************************************")
    print("(1) Soma (2) Subração (3) Multiplicação (4) Divisão")
    print("***************************************************")

    # Obtendo a escolha do usuário com base nas opções do menu
    operacao = int(input("Qual operação você quer fazer: "))

    # Armazenando dois valores digitados pelo usuário
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    # Processando operação com base na escolha do usuário em
    # relação ao menu de opções.
    if(operacao == 1):
        f.soma(numero1, numero2)
    elif(operacao == 2):
        f.subtracao(numero1, numero2)
    elif(operacao == 3):
        f.multiplicacao(numero1, numero2)
    elif(operacao == 4):
        f.divisao(numero1, numero2)
    else:
        print("A operação escolhida é inválida.")

# Modularizando este arquivo
if(__name__ == "__main__"):
    operacoes()