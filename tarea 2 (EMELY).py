#Lista
lista = []

#Encabezado del programa
print ("----------------------------------------------")
print("  Bienvenidos al programa 2 de Emely  ")
print ("----------------------------------------------")
print("              Instrucciones:                   ")
print ("----------------------------------------------")
print("")
print("Por favor inserte el texto que desea convertir en una lista de palabras")
print("todas conformadas por letras en minusculas:")
print("")
print ("----------------------------------------------")
print("")

#Solicitud del dato_1 al usuario 
print("por favor ingrese palabras en mayuscula:")
Palabra = input()

#Convertir todo a minusculas
Palabra = Palabra.lower()

#Registrar el string como palabras en la lista
lista = Palabra.split()


#Demostracion de resultados
print("")
print("-----------------------------------------------")
print("  La lista de palabras que ingresaste son :) ")
print("-----------------------------------------------")
print("" )
print(lista)
print("")
print("-----------------------------------------------")
print("          Que increible es programar          ")
print("-----------------------------------------------")
print("")