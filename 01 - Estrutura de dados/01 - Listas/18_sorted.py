linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

nomes = ["Enzo", "Bruno", "Anderson", "Erika"]

print(sorted(nomes, key=lambda x: len(x)))
print(sorted(nomes, key=lambda x: len(x), reverse=True))
print(sorted(nomes))
print(sorted(nomes, reverse=True))