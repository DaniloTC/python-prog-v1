# A estrutura do laço for é mais simples do que a estrutura while, ele
# trabalha com a função range como parte de sua estrutura.
#
# A função range pode receber até 3 parâmetros, sendo o terceiro opcional,
# são eles: 
# 
# range(start, stop, [step]) 
# 
# Onde step é o parâmetro que incrementa a cada iteração, por padrão é 1 e
# elimina a necessidade de incrementar dentro do bloco como no while.
#
# Mais uma diferença é que os dois primeiros parâmetros trabalham com
# a seguinte condição: (contador < 5) fazendo com que o 5 não na faça
# parte da condição como verdadeiro.
#
# Para incluir o número definido no segundo parâmetro precisamos somar
# mais um a ele: range(1, 5 + 1) e dessa forma, no resultado final, será
# incluído a quinta iteração como true e retornará o valor: 1 2 3 4 5

for contador in range(1, 5): # enquanto contador for < 5 será executado
	print(contador)          # imprime valor da iteração atual

# Output: 1 2 3 4