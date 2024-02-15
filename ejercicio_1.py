"""
parametros 
numero(int):El numero que se repite en la serie
nterminos(int):El numero de terminos en la serie
 
"""
def numeroRepetido (numero,nterminos):
    suma=0
    termino = "" #iniciamos el termino en una cadena vacia 


    for i in range(1,nterminos+1):
        termino +=str(numero) # concatenamos el numero al termino
        suma +=int(termino) # convertimos el termino a numero y lo sumamos 


    return suma     # devolvemos la suma total 

# para hacer pruebas poner numero y nterminos
#print (numeroRepetido(3,5)) #salida ejemplo:xxxx
#print (numeroRepetido(5,3)) #salida ejemplo:xxxx



