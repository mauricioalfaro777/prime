"""""
# Solicita al usuario que introduzca una cadena y la formatea eliminando espacios en los extremos y convirtiéndola a minúsculas
cadena = input("Introduce la cadena relacionada con la noche de Halloween: ").strip().lower()

# Inicializa una nueva cadena para almacenar el formato alternado de mayúsculas y minúsculas
cadena_nueva = ""
estado = True  # Variable de control para alternar entre mayúsculas y minúsculas

# Recorre cada carácter en la cadena
for caracter in cadena:
    if caracter == " ":
        # Si el carácter es un espacio, lo agrega tal cual a la nueva cadena
        cadena_nueva += caracter
    else:
        # Alterna mayúsculas y minúsculas en función del valor de estado
        if estado:
            cadena_nueva += caracter.upper()
        else:
            cadena_nueva += caracter.lower()
    estado = not estado  # Cambia el estado para el próximo carácter

# Imprime la cadena con formato alternado de mayúsculas y minúsculas
print(cadena_nueva)

# Reemplaza las vocales con caracteres especiales para "encriptar" la cadena
encriptado = cadena.replace("a", "@").replace("e", "3").replace("i", "1").replace("o", "0").replace("u", "μ")
print("La cadena encriptada es:", encriptado)

# Cuenta las apariciones del símbolo '@' en la cadena encriptada
apariciones_del_a = encriptado.count("@")
print("El número de apariciones de la letra '@' es:", apariciones_del_a)

# Busca la subcadena "h@ll0w33n" en la cadena encriptada
subindice = encriptado.find("h@ll0w33n")
if subindice != -1:
    # Si la subcadena está presente, imprime la posición
    print("La cadena contiene la cadena 'Halloween' en la posición", subindice)

    # Extrae la subcadena y la imprime
    subcadena = encriptado[subindice:subindice+9]
    print("La subcadena es:", subcadena)

    # Invierte la subcadena y la imprime
    invertida = subcadena[::-1]
    print("La subcadena invertida es:", invertida)

    # Genera una nueva cadena en la que cada carácter se repite en secuencia
    repeticiones_de_la_subcadena = ""
    for i in range(len(subcadena)):
        repeticiones_de_la_subcadena += subcadena[i] * (i + 1)
    print("La subcadena repetida es:", repeticiones_de_la_subcadena)

    # Calcula la mitad de la cadena encriptada (independientemente de si su longitud es par o impar)
    mitad = len(encriptado) // 2

    # Crea la cadena final con la segunda mitad, la subcadena repetida y la primera mitad de la cadena encriptada
    cadena_final = encriptado[mitad:] + repeticiones_de_la_subcadena + encriptado[:mitad]
    print("La cadena final es:", cadena_final)

    # Define una función para verificar si un número es primo
    def es_primo(numero):
        if numero < 2:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True

    # Calcula la longitud de la cadena final y verifica si es un número primo
    longitud = len(cadena_final)
    if es_primo(longitud):
        print("¡Feliz Halloween!")
    else:
        print("Noche de brujas")

else:
    # Si la subcadena "h@ll0w33n" no está presente en la cadena encriptada
    print("La cadena no contiene la cadena 'Halloween'")
"""""
"""""
cadena = input("Introduce la cadena relacionada con la Navidad:").strip().lower()
cadena_alternada = ""
estado = True
for caracter in cadena:
    if caracter == " ":
        cadena_alternada += caracter
    else:
        if estado:
            cadena_alternada += caracter.upper()
        else:
            cadena_alternada += caracter.lower()
    estado = not estado
print(cadena_alternada)
cadena_encriptada= cadena.replace("a", "*").replace("e", "#").replace("i", "!").replace("o", "0").replace("u", "μ")
print("La cadena encriptada es:", cadena_encriptada)
apariciones_del_a = cadena_encriptada.count("*")
print("El número de apariciones de la letra '*' es:", apariciones_del_a)
subindice = cadena_encriptada.find("N*V!D*D".lower())
if subindice != -1:
    subcadena = cadena_alternada[subindice:subindice+9]
    invertida = subcadena[::-1]
    repeticiones_de_la_subcadena = ""
    for i in range(len(subcadena)):
        repeticiones_de_la_subcadena += subcadena[i] * (i + 1)
    mitad = len(cadena_alternada) // 2
    cadena_final = cadena_alternada[mitad:] + repeticiones_de_la_subcadena + cadena_alternada[:mitad]
    def es_primo(numero):
        if numero < 2:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True
    longitud = len(cadena_final)
    if es_primo(longitud):
        print("¡Feliz Navidad!")
    else:
        print("Noche silenciosa")
else:
    print("La cadena no contiene la cadena 'Navidad'")
"""
"""""
#Codigo Misterioso del Solsticio de inverno
opcion_valida="El solsticio de invierno es especial".lower().strip()
pista="El ******* de ******** es especial"
cadena_nueva=""
estado=True
while True:
    cadena = input("Introduce la cadena relacionada con el solsticio de invierno: ").strip().lower()
    if cadena == opcion_valida:
        for caracter in cadena:
            if caracter == " ":
                cadena_nueva += caracter
            else:
                if estado:
                    cadena_nueva += caracter.upper()
                else:
                    cadena_nueva += caracter.lower()
            estado = not estado
        cadena_encriptada= cadena.replace("a", "*").replace("e", "#").replace("i", "1").replace("o", "0").replace("u", "μ")
        print("La cadena encriptada es:", cadena_encriptada)
        apariciones_del_a = cadena_encriptada.count("*")
        print("El número de apariciones de la letra '*' es:", apariciones_del_a)
        indice = cadena_encriptada.find("s0lst1c10".lower())
        print(f"El indice de la subcadena es: {indice}")
        if indice != -1:
            subcadena = cadena_nueva[indice:indice+8]
            print(f"La subcadena es: {subcadena}")
            cadena_invertida = subcadena[::-1]
            print(f"La subcadena invertida es: {cadena_invertida}")
            repeticiones_de_la_subcadena = ""
            for i in range(len(subcadena)):
                repeticiones_de_la_subcadena += subcadena[i] * (i + 1)
            print(f"La subcadena repetida es: {repeticiones_de_la_subcadena}")
            mitad = len(cadena_nueva) // 2
            cadena_final = cadena_encriptada[mitad:] + repeticiones_de_la_subcadena + cadena_encriptada[:mitad]
            print(f"La cadena final es: {cadena_final}")
            def es_primo(numero):
                if numero < 2:
                    return False
                for i in range(2, int(numero**0.5) + 1):
                    if numero % i == 0:
                        return False
                return True
            longitud = len(cadena_final)
            if es_primo(longitud):
                print("¡Feliz Solsticio!")
            else:
                print("Noche larga")
        break
    else:
         print(f"Opción invalida, intentalo de nuevo, pista: {pista}")   
giuon="-" *55
print(f"{giuon}El programa Termino{giuon}")         
"""
#Repaso de Algoritmos
#1 vectores
"""
vector1=[1,2,3,4,5]
print("El vector es:",vector1)
numero=int(input("Introduce un numero por el que quieres multiplicar: "))
vector2=[]
for i in range(len(vector1)):
    vector2.append(vector1[i]*numero)
print("El nuevo vector es:",vector2)
"""
""""
Vector=[1,2,3,4,5,6,7,8,9,10]
mayor=float("-inf")

menor=float("inf")
for i in range(len(Vector)):
    if Vector[i]>mayor:
        mayor=Vector[i]
    if Vector[i]<menor:
        menor=Vector[i]
print("El mayor elemento es:",mayor)
print("El menor elemento es:",menor)
"""
""""
V=[]
for i in range(16):
    V.append(i)
print("Los elementos del vector son:",V)
print("El promedio es:",sum(V)/len(V))
print("Sus índices son:", [i for i in range(len(V))])
"""
"""
lista= input("Introduce una lista de números separados por comas: ").strip().split(",")
print("La lista es:",lista)
for contenido in lista:
    print(contenido)
"""
