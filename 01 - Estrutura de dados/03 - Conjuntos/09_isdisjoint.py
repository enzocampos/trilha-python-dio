conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {5, 6, 7, 8, 9}
conjunto_c = {1, 0}
conjunto_d = {6, 7, 8, 9}

resultado = conjunto_a.isdisjoint(conjunto_d) # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_b)  # False
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)
