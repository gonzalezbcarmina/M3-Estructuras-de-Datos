import sys

try:
    tasas = {
        "sol":float(sys.argv[1]),
        "argentino": float(sys.argv[2]),
        "dolar": float(sys.argv[3])
    }

    montoConvertir = float(sys.argv[4])
    
    print(f"Los {montoConvertir} equivalen a: ")
    print(f"{montoConvertir * tasas["sol"]} soles")
    print(f"{montoConvertir * tasas["argentino"]} pesos argentinos")
    print(f"{montoConvertir * tasas["dolar"]} dólares")    

except ValueError:
    print("Alguno de los valores ingresados no es un número...")
except:
    print("Ups... algo pasó pero no se qué...")
