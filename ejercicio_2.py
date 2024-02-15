

def listaFiltrados(listado):
    salida=[]
    for numero in listado:
        if numero % 5 == 0:
            if numero > 1000:
                return salida
            elif numero <= 600:
                salida.append(numero)
    
    
    return salida            

#para hacer pruebas
entrada =[500,1200,525,1100,1000,1500]
resultado = listaFiltrados(entrada)
print(resultado)





