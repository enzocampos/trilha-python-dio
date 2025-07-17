linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # Ordenar por ordem alfabética = ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # Ordenar por ordem alfabética ao contrário = ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # Ordenar pela quantidade de letras de uma palavra = ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # Ordenar pela quantidade de letras de uma palavra ao contrário = ["python", "csharp", "java", "js", "c"]
print(linguagens)
