print("***************************************")
print("***         Cálculando IMC          ***")
print("***************************************")

# Armazenando altura e peso do usuário já convertida para float
altura = float(input("Digite sua altura em metros: "))
peso   = float(input("Digite seu peso em Kg: "))

# Calculando imc
imc = peso / (altura**2)

# Processando informação para devolver uma saída com base no imc calculado
if (imc < 17):
    print("Seu IMC é {:2.4f} e você está muito abaixo do peso".format(imc))
elif (imc >= 17 and imc <= 18.49):
    print("Seu IMC é {:2.4f} e você está abaixo do peso normal".format(imc))
elif (imc >= 18.50 and imc <= 24.99):
    print("Seu IMC é {:2.4f} e você está com peso normal".format(imc))
elif (imc >= 25 and imc <= 29.99):
    print("Seu IMC é {:2.4f} e você está acima do peso normal".format(imc))
elif (imc >= 30 and imc <= 34.99):
    print("Seu IMC é {:2.4f} e você está com Obesidade grau I".format(imc))
elif (imc >= 35 and imc <= 39.99):
    print("Seu IMC é {:2.4f} e você está com Obesidade grau II (severa)".format(imc))
elif (imc > 30):
    print("Seu IMC é {:2.4f} e você está com Obesidade grau III (mórbida)".format(imc))
else:
    print("Valor inválido")

