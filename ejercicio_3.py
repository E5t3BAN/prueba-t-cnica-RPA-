def agrupacionNumeros(lista):
    conjuntos={}  #diccionario para almacenar los elementos 
    for numeros in lista:
        if numeros in conjuntos:
            conjuntos[numeros].append(numeros)
        else:
            conjuntos[numeros] = [numeros]
    
    matriz= list(conjuntos.values())
    return matriz

#para hacer pruebas 
entrada=[12, 25, 1, 1, 7, 25]
print(agrupacionNumeros(entrada))