import sys

try:
    with open(sys.argv[1], "r") as file:
        texto=file.read()
        
    #print(texto)
    nroCaracteres = len(set(texto)) 
    nroPalabras = len(set(texto.split(" ")))
    
    print(f"La cantidad de caracteres distintos es: {nroCaracteres}")
    print(f"La cantidad de palabras distintas es: {nroPalabras}")
except:
    print("No se logró ubicar el archivo que deseas abrir...")