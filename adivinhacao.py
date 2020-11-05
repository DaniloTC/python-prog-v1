print("**************************************")
print("** Bem-vindo ao Jogo de Adivinhação **")
print("**************************************")

numero_secreto = 10
numero_digitado = int(input("Adivinhe qual é o número secreto: ")) # convertendo entrada para int

acertou = numero_digitado == numero_secreto
maior   = numero_digitado >  numero_secreto
menor   = numero_digitado <  numero_secreto

if (acertou):
    print("Você acertou! Parabéns!")
else:
    if (maior):
        print("Você errou! Tente um número MENOR.")
    elif (menor):
        print("Você errou! Tente um número MAIOR.")
