def duplicates(lista):
    unicos = set()
    repetidos = set()
    for num in lista:
        if num in unicos:
            repetidos.add(num)
        else:
            unicos.add(num)
    return list(repetidos)

numeros = [1, 2, 2, 2, 2, 3, 4, 4, 5]
print(duplicates(numeros))