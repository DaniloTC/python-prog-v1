# A estrutura while necessita que declare uma variável com algum
# valor inicial e dentro da estrutura é OBRIGATÓRIO incrementar,
# a variável, do contrário seu script entrará em looping infinito.

contador = 1                # variável inicial definida com valor 1
while(contador <= 5):       # enquanto contador for <= 5 será executado
	print(contador)         # imprime valor da iteração atual
	contador = contador + 1 # incremento em 1

# Output: 1 2 3 4 5