# Apresentando opções para o usuário
print("***************************")
print("***  Escolha uma opção  ***")
print("***************************")
print("* (1) Jogo de Adivinhação *")
print("* (2) Matemática          *")
print("* (3) Calcular IMC        *")
print("***************************")

# Capturando escolha do usuário
escolha = int(input("O que deseja fazer? "))

# Processando a escolha do usuário e executando o programa
# que foi escolhido a partir do menu.
if (escolha == 1):
    print("Jogar jogo de adivinhação")
elif (escolha == 2):
    print("Fazer cálculo matemático")
else:
    print("Calcular imc")

