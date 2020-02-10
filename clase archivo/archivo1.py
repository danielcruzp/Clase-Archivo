import shutil   #Esta libreria nos sirve para usar la funcion de copiar archivos
from sys import exit

class Archivo: #Aqui se define la clase archivo, asi como su constructor
    def __init__(self,nombre):
        try:
            self.f=open(nombre,'r')  #Abrimos el archivo con el nombre dado
            self.nombre=nombre
        except:
            print("No se puede abrir el archivo",nombre) #Aparecera este letrero en caso de que no se encuentre el archivo o no se pueda abrir
            exit()

#Muestra contenido del archivo
    def muestra(self):
        i=1
        for linea in self.f:
            print("{:3}:{}".format(i,linea)) #imprime linea a linea el contenido del archivo enumerando cada linea
            i+=1 #incrementa el contador segun el numero de lineas
        self.f.seek(0) #nos sirve para ir al byte 0 del fichero

#Cuenta vocales
    def cuentaVocales(self):
        def vocales(s):
            contador=0
            for i in range(len(s)): #recorre el archivo 
                if s[i] in set("aeiouáéíóúAEIOUÁÉÍÓÚ"): #verifica cada posicion del archivo en busca de vocales
                    contador += 1 #incrementa el contador en caso de encontrar alguna
            return contador
        contador=0
        for linea in self.f:
            contador += vocales(linea)
        self.f.seek(0) #nos sirve para ir al byte 0 del fichero
        return contador

#Cuenta consonantes
    def cuentaConsonantes(self):
        def consonantes(s):
            contador=0
            for i in range(len(s)): #recorre el archivo
                if s[i] in set("bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"): #verifica cada posicion del archivo en busca de consonantes
                    contador += 1 #incrementa el contador en caso de encontrar aguna consonante
            return contador
        contador=0
        for linea in self.f:
            contador += consonantes(linea)
        self.f.seek(0) #nos sirve para ir al byte 0 del fichero
        return contador

#Cuenta signos de puntuacion
    def cuentaSignosP(self):
        def signos(s):
            contador=0
            for i in range(len(s)):  #recorre el archivo
                if s[i] in set(".,;:[]¿!?()-"): #verifica cada posicion del archivo en busca de algun elemento del conjunto
                    contador += 1 #incrementa el contador en caso de encontrar algun elemento del conjunto anterior
            return contador
        contador=0
        for linea in self.f:
            contador += signos(linea)
        self.f.seek(0) #nos sirve para ir al byte 0 del fichero
        return contador

#Cuenta espacios
    def cuentaEspacios(self):
        def espacios(s):
            contador=0
            for i in range(len(s)): #recorre el archivo
                if s[i] in set(" "): #verifica si en esa posicion del archivo hay un espacio
                    contador += 1 #incrementa en caso de encontrar espacios
            return contador
        contador=0
        for linea in self.f:
            contador += espacios(linea)
        self.f.seek(0) #nos sirve para ir al byte 0 del fichero
        return contador

#Cuenta palabras
    def cuentaPalabras(self):
        def palabras(s):
            tot = len(s) #le asignamos a tot el numero total de posiciones en el archivo
            contador = 0    
            for i in range(len(s)): #recorre el archivo
                if s[i] == ' ' and i > 0 and s[i - 1] != ' ': #verifica que se cumplan las condiciones 
                    contador += 1 #aumenta el contador si se cumplen las condiciones anteriores
                else:
                    if s[i] == "\n": #si lo anterior fue falso, entonces se hace esta comparacion
                        contador += 1 #incrementa en caso verdadero
                    else:
                        if i == tot-1: #en otro caso verifica que sea la ultima posicion del archivo
                            if s[tot-1] != "\n" and s[tot-2] != ' ': #verifica si se cumplen las condiciones
                                contador += 1 #en caso de cumplirse, se umenta el contador
            return contador
        contador = 0
        for linea in self.f:
            contador += palabras(linea)
        self.f.seek(0) #nos sirve para ir al byte 0 del fichero
        return contador

#Cuenta lineas
    def cuentaLineas(self):
        i=0
        for linea in self.f:
            i+=1 #si es una linea se aumenta el contador
        conta = "{:3}".format(i) #se le asigna a la variable "conta" el contenido de "i" ya con formato de salida        
        self.f.seek(0) #nos sirve para ir al byte 0 del fichero
        return conta #se retorna el numero de lineas en el archivo


#Cuenta mayusculas
    def cuentaMayusculas(self):
        def mayus(s):
            conta = 0
            for i in range(len(s)): #recorre el archivo
                if s[i] in set ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"): #"verifica que en la posicion s[i] contenga alguna letra mayuscula"
                    conta += 1 #se incrementa el contador en caso de encontrar alguna
            return conta
        conta = 0
        for linea in self.f:
            conta += mayus(linea)
        self.f.seek(0) #nos sirve para ir al byte 0 del fichero
        return conta
      

#Cuenta minusculas
    def cuentaMinusculas(self):
        def minusculas(s):
            contador = 0
            for i in range(len(s)): #recorre el archivo
                if s[i] in set ("abcdefghijklmnñopqrstuvwxyzáéíóú"): #verifica que en la posicion s[i] contenga alguna letra minuscula
                    contador += 1 #se incrementa el contador en caso de encontrar alguna
            return contador
        contador = 0
        for linea in self.f:
            contador += minusculas(linea)
        self.f.seek(0) #nos sirve para ir al byte 0 del fichero
        print("Minusculas: ",contador)

#Copia archivo
    def copiarArchivo(self):
        print("\n>>>>>>>>>>COPIAR ARCHIVO<<<<<<<<<<<<<")
        des = input("Proporcione el nombre/ruta del archivo de destino: ") #se lee el nombre o la ruta del archivo de destino
        shutil.copy(self.f.name , des) #copia el archivo al destino especificado
        print("\nEl contenido del archivo se ha copiado a ",des)

#Convierte a mayusculas
    def convierteEnMayusculas(self):
        for linea in self.f: 
            print(linea.upper()) #esta funcion convierte el texto a mayusculas y lo imprime
        self.f.seek(0) #nos sirve para ir al byte 0 del fichero

#Convierte en minusculas
    def convierteEnMinusculas(self):
        for linea in self.f:
            print(linea.lower())#esta funcion convierte el texto a mayusculas y lo imprime
        self.f.seek(0) #nos sirve para ir al byte 0 del fichero


#Muestra en hexadecimal
    def Hexadecimal(self):
        h = []
        def hexa(s):
            for i in range(len(s)): #recorre el archivo
                h.append(hex(ord(s[i]))) #convierte a formato hexadecimal
        for linea in self.f:
            hexa(linea)
        
        self.f.seek(0) #nos sirve para ir al byte 0 del fichero
        return h
