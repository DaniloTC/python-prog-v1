idade = int(input("Digite sua idade: "))

# if elif else, estrutura aninhada
if (idade > 18):
    print("Você é maior de idade.")
else:
    if (idade < 10):
        print("Você é uma criança.")
    elif (idade > 10):
        print("Você é um adolescente.")

#-----------------------------------------

# Testes condicionais, retorna true/false
crianca     = idade < 12
adolescente = idade < 18
maior_idade = idade > 18

print(crianca, adolescente, maior_idade)