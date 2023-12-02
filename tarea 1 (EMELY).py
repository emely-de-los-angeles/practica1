#Lista
lista = []

#Encabezado del programa
print ("-----------------------------------")
print("  Bienvenidos al programa de Emely  ")
print ("-----------------------------------")
print("")
print("Instrunciones:")
print("")
print("Se le van a solicitar 3 numerons enteros")
print("")

#Condicion

#Solicitud del dato_1 al usuario 
print("por favor ingrese el primer numero entero:")
numero = input()
numero = int(numero)

#Agregar numero a la lista
lista.append (numero)

#Solicitud del dato_2 al usuario 
print("por favor ingrese el segundo numero entero:")
numero = input()
numero = int(numero)


#Agregar numero a la lista
lista.append (numero)

#Solicitud del dato_3 al usuario 
print("por favor ingrese el tercer numero entero:")
numero = input() 
numero = int(numero)


#Agregar numero a la lista
lista.append (numero)


#Ordenar la lista
lista.sort()

#Demostracion de resultados
print("")
print("-----------------------------------------------")
print("Felicidades, has ingresado todos los numeros :)")
print("-----------------------------------------------")
print("Los numeros que ingresastes son:" )
print(lista)