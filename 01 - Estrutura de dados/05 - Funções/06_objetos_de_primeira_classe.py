def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def subtrair(a, b):
    return a - b


def exibir_resultado(a, b, function):
    resultado = function(a, b)
    if function is multiplicar:
        print(f"O resultado da multiplicação é {a} * {b} = {resultado}")
    if function is somar:
        print(f"O resultado da adição é {a} + {b} = {resultado}")
    if function is subtrair:
        print(f"O resultado da subtração é {a} - {b} = {resultado}")
    

exibir_resultado(15, 6, subtrair)