def Heterograma(cadena):
    respuesta=True
    cadena = cadena.lower()
    
    for i in cadena:
        if cadena.count(i)>1 and i!=" ":
            respuesta=False
    
    return respuesta        

def Pangrama(cadena):
    alfabeto="abcdefghijklmnñopqrstuvwxyz"
    respuesta=True
    
    cadena=cadena.lower()
    for i in alfabeto:
        if i not in cadena :
            respuesta=False
            
    return respuesta  
      