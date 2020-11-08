numero1 = 10        # número
numero2 = int("10") # string (conversão necessária para int)

# Soma valores
print(numero1 + numero2) # Output: 20

# ----------------------------------------------------------

# Caso a variável 'numero2' ou seu valor não seja convertido
# para o tipo int, o seguinte erro será apresentado:
#
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'