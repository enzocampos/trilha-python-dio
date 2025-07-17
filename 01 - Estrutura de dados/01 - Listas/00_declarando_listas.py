frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)
print(letras[::-1])

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[-1][-1])

numbers = [1, 30, 21, 2, 9, 65, 34]
pares = [number for number in numbers if number % 2 == 0]
print(pares)

for number in numbers:
    if number % 2 == 0:
        pares.append(number)
        print(pares)

numbers = [1, 30, 21, 2, 9, 65, 34]
quadrado = [number ** 2 for number in numbers]
print(quadrado)

for number in numbers:
    quadrado.append(number ** 2)
    print(quadrado)