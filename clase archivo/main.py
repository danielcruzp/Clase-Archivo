from archivo1 import *   #importamos el archivo "archivo1.py" para poder usar sus funciones

#"FUNCION PRINCIPAL"
#main

nomb=input("Nombre del archivo: ")  #Pide al usuario que proporcione el nombre del archivo de origen
archivo=Archivo(nomb) #Creamos un objeto de tipo archivo pasando como parametro el archivo a leer
print("\n>>>>>>>>>>TEXTO ORIGINAL<<<<<<<<<<")
archivo.muestra() #imprime en pantalla el texto original del archivo
print("\n>>>>>>>>>>TEXTO EN MAYUSCULAS<<<<<<<<<<")
archivo.convierteEnMayusculas() #muestra en pantalla el texto del archivo convertido a mayusculas
print("\n>>>>>>>>>>TEXTO EN MINUSCULAS<<<<<<<<<<") 
archivo.convierteEnMinusculas() #muestra en pantalla el texto del archivo convertido a mayusculas
print("\n>>>>>>>>>>TEXTO EN HEXADECIMAL<<<<<<<<<<") 
print(archivo.Hexadecimal(),"\n") #convierte el texto original en formato hexadecimal
archivo.cuentaMinusculas() #imprime en pantalla el numero de letra minusculas que hay en el texto
print("Mayusculas: ",archivo.cuentaMayusculas()) #imprime el numero de mayusculas en el texto
print("Vocales: ",archivo.cuentaVocales()) #muestra en pantalla el numero de vocales
print("Consonantes: ",archivo.cuentaConsonantes()) #muestra en el numero de consonantes en el texto
print("Signos de puntuacion: ",archivo.cuentaSignosP()) #muestra en el numero de signos de puntuacion
print("Espacios: ",archivo.cuentaEspacios()) #muestra el numero de espacios 
print("Palabras: ",archivo.cuentaPalabras()) #muestra el numero de palabras
print("Lineas: ",archivo.cuentaLineas()) #imprime en pantalla el numero de lineas en el texto
archivo.copiarArchivo() #ejecuta la funcion de copiar archivo

