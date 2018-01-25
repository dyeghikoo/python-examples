"""
PROBLEMA: Queremos pasar de texto a diccionario pero el casting dict()
no funciona. 
SOLUCION: Utilizamos el formato JSON como formato intermedio.
"""
from bittrex.bittrex import Bittrex, API_V2_0
import json

#Obtenemos nuestro dict 
my_bittrex = Bittrex(None, None, api_version=API_V2_0)
todayCurrency = my_bittrex.get_currencies()

#Transformamos en json y despues en texto y guardamos en el archivo
file = open("documents\currencys.txt","w")
file.write(str(json.dumps(todayCurrency)))
file.close()

#Si ahora quisiesemos trabajar con el diccionario leemos y 
#transformamos de json a diccionario
file2 = open("documents\currencys.txt","r")
decodedddd = dict(file2.read())
decoded = json.loads(file2.read())
file2.close()
