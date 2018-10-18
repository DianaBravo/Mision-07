#Autor: Diana Marisol Medina Bravo
#Ejercicio en el que se hacen divisiones por medio de ciclos y se encuentra el mayor de una serie de numeros y se elige
#lo que se quiere hacer mediante un menú


#Función que divide mediante ciclos restando al dividendo el divisor y contando cuantas veces y calculando tambien el residuo
def dividir (dividendo,divisor):
    contador=0
    dividendo1 = dividendo
    while dividendo >= divisor :
        contador += 1
        dividendo -= divisor

    print(dividendo1,"/",divisor,"=",contador," sobra" ,dividendo)


#Función que encuentra el mayor de una serie de números
def encontrarElMayor():
    numeroM = 0
    numero = int(input("Teclea un número [-1 para salir]:"))
    if numero == -1:
        print("No hay valor mayor")

    while numero != -1 :
        if (numero > numeroM) & (numero > 0):
            numeroM = numero
            numero = int(input("Teclea un número [-1 para salir]: "))
        elif (numero <= numeroM) & (numero > 0):
            numero = int(input("Teclea un número [-1 para salir]: "))

    if numero==-1 and numeroM!=0:
        print("El mayor es: ", numeroM)


#Función principal
def leerOpcionMenu():
    print("Misión 7.Ciclos while.")
    print("Autor:Diana Marisol Medina Bravo")
    print("Matrícula: A01748753")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    print("")
    return opcion

def main():
    opcion = leerOpcionMenu()
    while opcion != 3:
        if opcion == 1:
            print("Calculando divisiones")
            dividendo = int(input("Teclee el dividendo: "))
            divisor = int(input("Teclee el divisor: "))
            dividir(dividendo, divisor)
            print("")
        elif opcion == 2:
            print("Teclea una serie de números para encontrar el mayor")
            encontrarElMayor()
            print("")
        opcion = leerOpcionMenu()
    print("Termina programa")

main()