"""
Prácticas VLA
Fabián Guevara
24/05/2024
Version 4.0
"""
#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#══════════════════════════════MENU PRINCIPAL════════════════════════
#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

def menuprincipal():
    print("\n¿Que desea revisar?",
          "\n1. Práctica 1",
          "\n2. Práctica 2",
          "\n3. Práctica 3",
          "\n4. Práctica 4",
          "\n5. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        practica1()
    elif opcion == "2":
        practica2()
    elif opcion == "3":
        practica3()
    elif opcion == "4":
        practica4()
    elif opcion == "5":
        print("Hasta luego")
        quit()



#═════════════════════════════════Sub Menú═════════════════════════════

        
#═════════════════════════════════Menú Práctica 1
def practica1():
    print("\nPRACTICA 1",
          "\n1¿Que ejercicio desea revisar?",
          "\n1. Ejercicio 1",
          "\n2. Ejercicio 2",
          "\n3. Ejercicio 3",
          "\n4. Ejercicio 4",
          "\n5. Ejercicio 5",
          "\n6. Ejercicio 6",
          "\n7. Ejercicio 7",
          "\n8. Ejercicio 8",
          "\n9. Ejercicio 9",
          "\n10. Ejercicio 10",
          "\n11. volver al menu anterior")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        p1e1()
    elif opcion == "2":
        p1e2()
    elif opcion == "3":
        p1e3()
    elif opcion == "4":
        p1e4()
    elif opcion == "5":
        p1e5()
    elif opcion == "6":
        p1e6()
    elif opcion == "7":
        p1e7()
    elif opcion == "8":
        p1e8()
    elif opcion == "9":
        p1e9()
    elif opcion == "10":
        p1e10()
    elif opcion == "11":
        menuprincipal()

#═════════════════════════════════Menú Práctica 2
def practica2():
    print("\nPRACTICA 2",
          "\n1¿Que ejercicio desea revisar?",
          "\n1. Ejercicio 1",
          "\n2. Ejercicio 2",
          "\n3. Ejercicio 3",
          "\n4. Ejercicio 4",
          "\n5. Volver al menu anterior")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        p2e1()
    elif opcion == "2":
        p2e2()
    elif opcion == "3":
        p2e3()
    elif opcion == "4":
        p2e4()
    elif opcion == "5":
        menuprincipal()

#═════════════════════════════════Menú Práctica 3
def practica3():
    print("\nPRACTICA 3",
          "\n1¿Que ejercicio desea revisar?",
          "\n1. Ejercicio 1",
          "\n2. Ejercicio 2",
          "\n3. Ejercicio 3",
          "\n4. Ejercicio 4",
          "\n5. Ejercicio 5",
          "\n6. Ejercicio 6",
          "\n7. volver al menu anterior")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        p3e1()
    elif opcion == "2":
        p3e2()
    elif opcion == "3":
        p3e3()
    elif opcion == "4":
        p3e4()
    elif opcion == "5":
        p3e5()
    elif opcion == "6":
        p3e6()
    elif opcion == "7":
        menuprincipal()
        
#═════════════════════════════════Menú Práctica 4
def practica4():
    print("\nPRACTICA 4",
          "\n1¿Que ejercicio desea revisar?",
          "\n1. Ejercicio 1",
          "\n2. Ejercicio 2",
          "\n3. Ejercicio 3",
          "\n4. Ejercicio 4",
          "\n5. Ejercicio 5",
          "\n6. Ejercicio 6",
          "\n7. Ejercicio 7",
          "\n8. Ejercicio 8",
          "\n9. volver al menu anterior")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        EscribirCentrado()
    elif opcion == "2":
        EsMultiplo()
    elif opcion == "3":
        p4e3()
    elif opcion == "4":
        ConvertirEspaciado()
    elif opcion == "5":
        calcularMinMax()
    elif opcion == "6":
        p4e6()
    elif opcion == "7":
        Login()
    elif opcion == "8":
        p4e8()
    elif opcion == "9":
        menuprincipal()


#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#══════════════════════════════PRACTICA 1════════════════════════════
#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


            
#═════════════════════════════════Practica 1, Ejercicio 1
def p1e1():
    print("\nEscribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.")
    
    edad = int(input("\nPor favor introduzca su edad: "))
    if (edad >= 18):
        print("\nUsted es mayor de edad")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e1()
        elif repetir == "n":
            practica1()
    else:
        print("\nUsted no es mayor de edad")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e1()
        elif repetir == "n":
            practica1()

#═════════════════════════════════Practica 1, Ejercicio 2
def p1e2():
    print("\nEscribir un programa que almacene la cadena de caracteres contraseña en una variable,",
          "\npregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida",
          "\npor el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y",
          "\nminúsculas.")
    
    password = "password"
    contra = input("\nIntroduzca la contraseña: ")
    if contra.upper() == password.upper():
        print("\ncontraseña correcta!")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e2()
        elif repetir == "n":
            practica1()
    else:
        print("\ncontraseña incorrecta")
        practica1()

#═════════════════════════════════Practica 1, Ejercicio 3
def p1e3():
    print("\nEscribir un programa que pida al usuario dos números y muestre por pantalla su división.",
          "\nSi el divisor es cero el programa debe mostrar un error.")

    numero1 = int(input("\n1Introduzca el primer número: "))
    numero2 = int(input("Introduzca el segundo número: "))
    if (numero2 == 0):
        print("\nError: No se puede dividir por 0")
        p1e3()
    else:
        print(str(numero1) + "/" + str(numero2)+"="+str(numero1/numero2))
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e3()
        elif repetir == "n":
            practica1()

#═════════════════════════════════Practica 1, Ejercicio 4
def p1e4():
    print("\nEscribir un programa que pida al usuario un número entero y muestre por pantalla si es",
          "\npar o impar.")
    
    numero = int(input("\n1Introduzca un número: "))
    if (numero%2 == 0):
        print("\nEl número introducido es un número par")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e4()
        elif repetir == "n":
            practica1()
    else:
        print("\nEl número introducido es un número impar")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e4()
        elif repetir == "n":
            practica1()

#═════════════════════════════════Practica 1, Ejercicio 5
def p1e5():
    print("\nPara tributar un determinado impuesto se debe ser mayor de 16 años y tener unos",
          "\ningresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al",
          "\nusuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que",
          "\ntributar o no.")
    
    edad = int(input("\n1Intrudzca su edad: "))
    ingreso = int(input("intruduzca sus ingresos mensuales: "))
    if (edad >= 16) and (ingreso >= 1000):
        print("\nUsted tiene que tributar")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e5()
        elif repetir == "n":
            practica1()
    else:
        print("\nUsted no tiene que tributar")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e5()
        elif repetir == "n":
            practica1()


#═════════════════════════════════Practica 1, Ejercicio 6
def p1e6():
    print("\nLos alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el",
          "\nnombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los",
          "\nhombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa",
          "\nque pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le",
          "\ncorresponde.")
    
    alfabeto1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    alfabeto2 = ["n","o","p","q","r","s","t","u","v","w","x","y","z"] 
    sexo = input("\n1Intruduzca su sexo(M/F): ")
    nombre = input("Introduzca su nombre en minúscula: ")
    if ((sexo == "M") and (nombre[0] in alfabeto2)) or ((sexo == "F") and (nombre[0] in alfabeto1)):
        print("\nUsted pertenece al grupo A")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e6()
        elif repetir == "n":
            practica1()
    else:
        print("\nUsted pertenece al grupo B")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e6()
        elif repetir == "n":
            practica1()

#═════════════════════════════════Practica 1, Ejercicio7
def p1e7():
    print("\nLos tramos impositivos para la declaración de la renta en un determinado país son los",
          "\nsiguientes:",
          "\n● Renta Tipo impositivo",
          "\n● Menos de 10000€ 5%",
          "\n● Entre 10000€ y 20000€ 15%",
          "\n● Entre 20000€ y 35000€ 20%",
          "\n● Entre 35000€ y 60000€ 30%",
          "\n● Más de 60000€ 45%",
          "\nEscribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo",
          "\nimpositivo que le corresponde.")
    
    rentaanual = int(input("\n1Ingrese su renta anual: "))
    if (rentaanual < 10000):
        print("\nSu tramo impositivo es de 5%: "+str(rentaanual*0.05)+"€")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e7()
        elif repetir == "n":
            practica1()
    elif (rentaanual >= 10000) and (rentaanual < 20000): 
        print("\nSu tramo impositivo es de 15%: "+str(rentaanual*0.15)+"€")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e7()
        elif repetir == "n":
            practica1()
    elif (rentaanual >= 20000) and (rentaanual < 35000): 
        print("\nSu tramo impositivo es de 20%: "+str(rentaanual*0.20)+"€")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e7()
        elif repetir == "n":
            practica1()
    elif (rentaanual >= 35000) and (rentaanual < 60000): 
        print("\nSu tramo impositivo es de 30%: "+str(rentaanual*0.30)+"€")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e7()
        elif repetir == "n":
            practica1()
    else:
        print("\nSu tramo impositivo es de 45%: "+str(rentaanual*0.45)+"€")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e7()
        elif repetir == "n":
            practica1()

#═════════════════════════════════Practica 1, Ejercicio 8
def p1e8():
    print("\nEn una determinada empresa, sus empleados son evaluados al final de cada año. Los",
          "\npuntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,",
          "\ntraduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados",
          "\npueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.",
          "\nA continuación se muestra una tabla con los niveles correspondientes a cada puntuación.",
          "\nLa cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la",
          "\npuntuación del nivel.",
          "\nNivel Puntuación",
          "\nInaceptable 0.0",
          "\nAceptable 0.4",
          "\nMeritorio 0.6 o más",
          "\nEscribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento,",
          "\nasí como la cantidad de dinero que recibirá el usuario.")
    
    rendimiento = float(input("\nIndique la puntuación recibida(0.0, 0.4, 0.6 o más): "))
    if (rendimiento == 0.0):
        print("\nSu nivel de rendimiento es: INACEPTABLE, su beneficio será de 0€")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e8()
        elif repetir == "n":
            practica1()
    elif (rendimiento == 0.4):
        print("\nSu nivel de rendimiento es: ACEPTABLE, su beneficio será de "+str(rendimiento*2400)+"€")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e8()
        elif repetir == "n":
            practica1()
    elif (rendimiento >= 0.6):
        print("\nSu nivel de rendimiento es: MERITORIO, su beneficio será de "+str(rendimiento*2400)+"€")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e8()
        elif repetir == "n":
            practica1()
    else:
        print("\nLa puntuación sólo puede ser 0.0, 0.4, 0.6 o más, por favor ingrese la puntuación de nuevo")
        p1e8()

#═════════════════════════════════Practica 1, Ejercicio 9
def p1e9():
    print("\nEscribir un programa para una empresa que tiene salas de juegos para todas las edades",
          "\ny quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.",
          "\nEl programa debe preguntar al usuario la edad del cliente y mostrar el precio de la",
          "\nentrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años",
          "\ndebe pagar 5€ y si es mayor de 18 años, 10€.")
    
    edad = int(input("\n1Introduzca la edad del cliente: "))
    if (edad < 4):
        print("\nLa entrada para el cliente es gratuita")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e9()
        elif repetir == "n":
            practica1()
    elif (edad >= 4 and edad < 18):
        print("\nLa entrada para el cliente será de 5€")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e9()
        elif repetir == "n":
            practica1()
    else:
        print("\nLa entrada para el cliente será de 10€")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e9()
        elif repetir == "n":
            practica1()

#═════════════════════════════════Practica 1, Ejercicio 10
def p1e10():
    print("\nLa pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los",
          "\ningredientes para cada tipo de pizza aparecen a continuación.",
          "\nIngredientes vegetarianos: Pimiento y tofu.",
          "\nIngredientes no vegetarianos: Peperoni, Jamón y Salmón.",
          "\nEscribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en",
          "\nfunción de su respuesta le muestre un menú con los ingredientes disponibles para que",
          "\nelija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están",
          "\nen todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana",
          "\no no y todos los ingredientes que lleva.")
    
    pizza = ["Mozzarella", "Tomate"]
    veg = input("\n1¿Desea una pizza vegetariana? (si/no) ")
    if (veg == "si"):
        ingrveg = input("\n¿Desea una pizza de Pimiento o Tofu? ")
        if ingrveg == "Pimiento" or ingrveg == "Tofu":
            pizza.append(ingrveg)
            print("\nLa pizza elegida es vegetariana")
            print("\nSus ingredientes son: ")
            for i in pizza:
                print(i)
            practica1()
        else:
            print("\nPor favor elija entre los Pimiento o Tofu")
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e10()
        elif repetir == "n":
            practica1()
    elif (veg == "no"):
        ingrnoveg = input("\n¿Desea una pizza de Peperoni, Jamon o Salmon? ")
        if ingrnoveg == "Peperoni" or ingrnoveg == "Jamon" or ingrnoveg == "Salmon":
            pizza.append(ingrnoveg)
            print("\nLa pizza elegida no es vegetariana")
            print("\nSus ingredientes son: ")
            for i in pizza:
                print(i)
        repetir = input("\n¿Desea repetir la tarea? (s/n)")
        if repetir == "s":
            p1e10()
        elif repetir == "n":
            practica1()
        else:
            print("\nPor favor elija entre los Peperoni, Jamon o Salmon")
            p1e10()



#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#══════════════════════════════PRACTICA 2════════════════════════════
#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


                   
#═════════════════════════════════Practica 2, Ejercicio 1
materia = ["Matemáticas", "Físico", "Química", "Historia", "Lengua"]

def p2e1():
    print("Las materias impartidas por el centro educativo son: Matemáticas, Física, Química,",
          "\nHistoria y Lengua, realice un programa le debe permitir al usuario ver las materias en",
          "\npantalla, agregar y eliminar, materias en caso que sea necesario.")
    
    print("\n¿Qué desea realizar?",
          "\n1.Ver Materias",
          "\n2.Agregar Materia",
          "\n3.Eliminar Materia")
    
    opcion = input("\nSeleccione una opción: ")
    if opcion == "1":
       for i in materia:
           print(i)
       repetir = input("\n¿Desea repetir la tarea? (s/n) ")
       if repetir == "s":
           p2e1()
       elif repetir == "n":
           practica2()
        
    elif opcion == "2":
        materianueva = input("\nIntroduzca el nombre de la materia por agregar: ")
        materia.append(materianueva)
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p2e1()
        elif repetir == "n":
            practica2()
           
    elif opcion == "3":
        remover = input("\nIntroduzca el nombre de la materia por agregar: ")
        materia.remove(remover)
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p2e1()
        elif repetir == "n":
            practica2()


#═════════════════════════════════Practica 2, Ejercicio 2
libros = []
def p2e2():
    print("\nEl día de hoy ha abierto una biblioteca con cero libros, y necesita un programa el cual le",
          "\npermite agregar y eliminar libros, también desea ver los libros que se han agregado.")
    
    print("\n¿Qué desea realizar?",
          "\n1.Ver libros",
          "\n2.Agregar libro",
          "\n3.Eliminar libro")
    
    opcion = input("\nSeleccione una opción: ")
    if opcion == "1":
       for i in libros:
           print(i)
       repetir = input("\n¿Desea repetir la tarea? (s/n) ")
       if repetir == "s":
           p2e2()
       elif repetir == "n":
           practica2()
        
    elif opcion == "2":
        libronuevo = input("\nIntroduzca el nombre del libro por agregar: ")
        libros.append(libronuevo)
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p2e2()
        elif repetir == "n":
            practica2()
           
    elif opcion == "3":
        remover = input("\nIntroduzca el nombre de la materia por agregar: ")
        libros.remove(remover)
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p2e2()
        elif repetir == "n":
            practica2()

#═════════════════════════════════Practica 2, Ejercicio 3
password2 = ["123","abc"]
intentos = 0

def p2e3():
    print("\nContraseñas = ‘123’ , ‘abc’",
          "\nElabore una simulación del cajero automático, exactamente la siguiente indicación:",
          "\nEn el momento que la persona introduzca la contraseña mal 3 veces deberá aparecer en",
          "\npantalla cuenta bloqueada. La variable contraseñas tiene dos posibles opciones, debemos",
          "\ncuidar que esto no pueda ser modificado por el usuario.")
    
    global intentos
    if intentos == 3:
        print("\nSu cuenta ha sido bloqueada")
        unblock = input("\n¿Desea desbloquearla? (s/n) ")
        if unblock == "s":
            intentos = 0
            p2e3()
        elif unblock == "n":
            repetir = input("\n¿Desea repetir la tarea? (s/n) ")
            if repetir == "s":
                p2e3()
            elif repetir == "n":
                practica2()
    contra = input("\nIntroduzca la contraseña: ")
    if (contra in password2):
        print("\nHa ingresado a su cuenta exitosamente")
        intentos = 0
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p2e3()
        elif repetir == "n":
            practica2()
    else:
        print("\nIntente nuevamente")
        intentos += 1
        p2e3()

#═════════════════════════════════Practica 2, Ejercicio 4
DatosNombres = ["Juan","María","Carlos","Laura","Andrés","Ana","Pedro","Gabriela","Alejandro","Sofia","Diego",
                "Valentina","Manuel","Camila","José","Isabella","Miguel","Valeria","Francisco","Natalia",
                "Luis","Gabriela","Javier","Paula","Antonio","Martina","Ricardo","Victoria","Daniel","Elena",
                "Fernando","Daniela","Sergio","Adriana","Jorge","Sara","Eduardo","Mónica","Rodrigo","Patricia",
                "Alberto","Isabel","Guillermo","Clara","Raúl"]
def p2e4():
    print("\nDatosNombres: Juan, María, Carlos, Laura, Andrés, Ana, Pedro, Gabriela, Alejandro,",
          "\nSofia, Diego, Valentina, Manuel, Camila, José, Isabella, Miguel, Valeria, Francisco,",
          "\nNatalia, Luis, Gabriela, Javier, Paula, Antonio, Martina, Ricardo, Victoria, Daniel, Elena,",
          "\nFernando, Daniela, Sergio, Adriana, Jorge, Sara, Eduardo, Mónica, Rodrigo, Patricia,",
          "\nAlberto, Isabel, Guillermo, Clara, Raúl.",
          "\nNecesitamos un programa que le permita al usuario digitar el nombre del colaborador y",
          "\nsaber si trabaja para la compañía.")
    
    Nombre = input("\nIntroduzca el nombre que desea consultar: ")
    if Nombre in DatosNombres:
        print("\nEl colaborador sí trabaja en la compañía")
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p2e4()
        elif repetir == "n":
            practica2()
    else:
        print("\nEl colaborador no trabaja en la compañía")
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p2e4()
        elif repetir == "n":
            practica2()



#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#══════════════════════════════PRACTICA 3════════════════════════════
#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


            
#═════════════════════════════════Practica 3, Ejercicio 1
DicDivisas ={
                "Euro":"€",
                "Dollar":"$",
                "Yen":"¥"
            }

def p3e1():
    print("\nEscribir un programa que guarde en una variable el diccionario {'Euro';:'€';, ';Dollar';:';$';,",
          "\n';Yen';:';¥';}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso",
          "\nsi la divisa no está en el diccionario.")
    
    Divisa = input("\nEscoja una divisa: ")
    if (Divisa in DicDivisas):
        print("\nEl símbolo de esta divisa es: "+DicDivisas[Divisa])
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p3e1()
        elif repetir == "n":
            practica3()
    else:
        print("\nLa divisa seleccionada no está en el diccionario")
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p3e1()
        elif repetir == "n":
            practica3()

#═════════════════════════════════Practica 3, Ejercicio 2

def p3e2():
    print("\nEscribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo",
          "\nguarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene",
          "\n<edad>; años, vive en >dirección< y su número de teléfono es <teléfono>.")
    
    DicUsuario ={}
    DicUsuario["Nombre"] = input("\n¿Cuál es su nombre? ")
    DicUsuario["Edad"] = input("¿Cuál es su edad? ")
    DicUsuario["Dirección"] = input("¿Cuál es su dirección? ")
    DicUsuario["Telefono"] = input("¿Cuál es su telefono? ")
    print("\n"+DicUsuario["Nombre"]+" tiene "+DicUsuario["Edad"]+" años, vive en "+DicUsuario["Dirección"]+ " y su número de teléfono es "+DicUsuario["Telefono"])
    repetir = input("\n¿Desea repetir la tarea? (s/n) ")
    if repetir == "s":
        p3e2()
    elif repetir == "n":
        practica3()

#═════════════════════════════════Practica 3, Ejercicio 3
DicFrutas ={
                "Platano":1.35,
                "Manzana":0.80,
                "Pera":0.85,
                "Naranja":0.70
            }

def p3e3():
    print("Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,",
          "\npregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de",
          "\nese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje",
          "\ninformando de ello.",
          "\nFruta Precio",
          "\nPlátano 1,35",
          "\nManzana 0,80",
          "\nPera 0,85",
          "\nNaranja 0,70")
    
    Fruta = input("\nEscoja una fruta: ")
    if (Fruta in DicFrutas):
        Kilos = float(input("¿Cuántos kilos va comprar? "))
        print("\n"+str(Kilos)+" kilos de "+Fruta+" cuestan: "+str(Kilos*DicFrutas[Fruta])+"$")
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p3e3()
        elif repetir == "n":
            practica3()
    else:
        print("La fruta seleccionada no está en la lista")
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p3e3()
        elif repetir == "n":
            practica3()

#═════════════════════════════════Practica 3, Ejercicio 4
DicMeses ={
            1:"Enero",
            2:"Febrero",
            3:"Marzo",
            4:"Abril",
            5:"Mayo",
            6:"Junio",
            7:"Julio",
            8:"Agosto",
            9:"Setiembre",
            10:"Octubre",
            11:"Noviembre",
            12:"Diciembre"
        }

def p3e4():
    print("\nEscribir un programa que le pregunte al usuario una fecha haciendo uso del formato",
          "\ndd/mes/año, el usuario deberá introducir de forma numérica el día, mes y año, como",
          "\nresultado se mostrará en pantalla 23 de octubre de 2018.",
          "\nLos meses deben estar dentro de un arreglo.",
          "\n{1:;'enero';, 2:&'febrero';, 3:;'marzo';}")
    
    Day, Month, Year = input("\nIngrese el Dia, el Mes y el Año en número, separados por un espacio: ").split()
    print(str(Day)+" de "+DicMeses[int(Month)]+" de "+str(Year))
    repetir = input("\n¿Desea repetir la tarea? (s/n) ")
    if repetir == "s":
        p3e4()
    elif repetir == "n":
        practica3()

#═════════════════════════════════Practica 3, Ejercicio 5
DicPersona ={}

def p3e5():
    print("\nEscribir un programa que cree un diccionario vacío y lo vaya llenado con información",
          "\nsobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)",
          "\nque se le pida al usuario. Cada vez que se añade un nuevo dato debe imprimirse el",
          "\ncontenido del diccionario.")
    
    global DicPersona

    print("\n¿Que desea realizar?",
          "\n1. Agregar informacion a la lista",
          "\n2. Consultar informacion actual",
          "\n3. Borrar informacion de la lista",
          "\n4. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
            Categoria = input("\nIngrese la categoria: ")
            DicPersona[Categoria] = input("Ingrese la informacion: ")
            print(DicPersona)
            repetir = input("\n¿Desea repetir la tarea? (s/n) ")
            if repetir == "s":
                p3e5()
            elif repetir == "n":
                practica3()
            
    elif opcion == "2":
        print(DicPersona)
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p3e5()
        elif repetir == "n":
            practica3()
            
    elif opcion == "3":
        DicPersona ={}
        print("Toda la información ha sido borrada")
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p3e5()
        elif repetir == "n":
            practica3()
        
    elif opcion == "4":
        practica3()

#═════════════════════════════════Practica 3, Ejercicio 6
DicIngles ={
            "Rojo":"Red",
            "Azul":"Blue",
            "Verde":"Green"
            }
def p3e6():
    print("\nEscribir un programa que cree un diccionario de traducción español-inglés. El usuario",
          "\nintroducirá las palabras en español. Realice una opción por si el usuario desea agregar",
          "\nmás palabras.")
          
    global DicIngles

    print("\n¿Que desea realizar?",
          "\n1. Consultar una palabra en específico",
          "\n2. Consultar todo el diccionario",
          "\n3. Agregar definiciones al diccionario",
          "\n4. Borrar definiciones del diccionario",
          "\n5. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        Consulta = input("\nIngrese la palabra: ")
        if Consulta in DicIngles:
            print("\nLa traducción de "+Consulta+" es "+DicIngles[Consulta])
            repetir = input("\n¿Desea repetir la tarea? (s/n) ")
            if repetir == "s":
                p3e6()
            elif repetir == "n":
               practica3()            
    elif opcion == "2":
        print(DicIngles)
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p3e6()
        elif repetir == "n":
            practica3()
            
    elif opcion == "3":
        Palabra = input("\nIngrese la Palabra: ")
        DicIngles[Palabra] = input("\nIngrese la traducción: ")
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p3e6()
        elif repetir == "n":
            practica3()
            
    elif opcion == "4":
        Palabra = input("\nIngrese la Palabra que desea borrar: ")
        del DicIngles[Palabra]
        print("La palabra ha sido borrada exitosamente.")
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            p3e6()
        elif repetir == "n":
            practica3()



#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#══════════════════════════════PRACTICA 4════════════════════════════
#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


            
#═════════════════════════════════Practica 4, Ejercicio 1

def EscribirCentrado():
    print("\nCrea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba",
          "\ncentrado en pantalla (suponiendo una anchura de 80 columnas; pista: deberás escribir 40",
          "\n- longitud/2 espacios antes del texto). Además subraya el mensaje utilizando el carácter =.")
    texto = input("\nIntroduzca el texto: ")
    sub = ("="*len(texto))
    print(texto.center(40))
    print(sub.center(40))
    repetir = input("\n¿Desea repetir la tarea? (s/n) ")
    if repetir == "s":
        EscribirCentrado()
    elif repetir == "n":
        practica4()

#═════════════════════════════════Practica 4, Ejercicio 2

def EsMultiplo():
    print("\nCrea un programa que pida dos números enteros al usuario y diga si alguno de ellos es",
          "\nmúltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el",
          "\nprimero es múltiplo del segundo.")
    A = int(input("\nIntroduzca el primer número: "))
    B = int(input("Introduzca el segundo número: "))
    if A % B == 0:
        print("\nEl primer número es múltiplo del segundo")
    else:
        print("\nEl primer número no es múltiplo del segundo")
    repetir = input("\n¿Desea repetir la tarea? (s/n) ")
    if repetir == "s":
        EsMultiplo()
    elif repetir == "n":
        practica4()

#═════════════════════════════════Practica 4, Ejercicio 3

def p4e3():
    print("\nCrear una función que calcule la temperatura media de un día a partir de la temperatura",
          "\nmáxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya",
          "\npidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El",
          "\nprograma pedirá el número de días que se van a introducir.")
    CantidadDias = int(input("\nIntroduzca la cantidad de días: "))
    for x in range(CantidadDias):
        Max = float(input("\nIntroduzca la temperatura máxima: "))
        Min = float(input("\nIntroduzca la temperatura mínima: "))
        print("La temperatura media fue: "+str((Max+Min)/2))
    repetir = input("\n¿Desea repetir la tarea? (s/n) ")
    if repetir == "s":
        p4e3()
    elif repetir == "n":
        practica4()

#═════════════════════════════════Practica 4, Ejercicio 4

def ConvertirEspaciado():
    print("\nCrea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve",
          "\nuna cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H",
          "\no l a , t ú “. Crea un programa principal donde se use dicha función.")
    texto = input("\nIngrese el texto: ")
    print(" ".join(texto))
    repetir = input("\n¿Desea repetir la tarea? (s/n) ")
    if repetir == "s":
        ConvertirEspaciado()
    elif repetir == "n":
        practica4()

#═════════════════════════════════Practica 4, Ejercicio 5

def calcularMinMax():
    print("\nCrea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve",
          "\nel valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre",
          "\nel máximo y el mínimo, utilizando la función anterior.")
    valores = [int(valores) for valores in input("Ingrese múltiples valores separados por un espacio: ").split()]
    print("\nValor máximo: "+str(max(valores)))
    print("Valor mmínimo: "+str(min(valores)))
    repetir = input("\n¿Desea repetir la tarea? (s/n) ")
    if repetir == "s":
        calcularMinMax()
    elif repetir == "n":
        practica4()

#═════════════════════════════════Practica 4, Ejercicio 6

def p4e6():
    print("\nDiseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha",
          "\nfunción en un programa principal que lea el radio de una circunferencia y muestre su área",
          "\ny perímetro.")
    radio = float(input("\nIngrese el valor del radio: "))
    print("\nEl área de la circunferencia es: "+str(3.14*((radio)**2)))
    print("El perímetro de la circunferencia es: "+str((3.14*(radio)*2)))
    repetir = input("\n¿Desea repetir la tarea? (s/n) ")
    if repetir == "s":
        calcularMinMax()
    elif repetir == "n":
        practica4()

#═════════════════════════════════Practica 4, Ejercicio 7
intentos2 = 0
password3 = {"usuario1":"asdasd"}

def Login():
    print("\nCrear una función llamada “Login”, que recibe un nombre de usuario y una contraseña y",
          "\nte devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es",
          "\n“asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se",
          "\nha podido hacer login incremente este valor.",
          "\nCrear un programa principal donde se pida un nombre de usuario y una contraseña y se",
          "\nintente hacer login, solamente tenemos tres oportunidades para intentarlo.")
    
    global intentos2
    if intentos2 == 3:
        print("\nSu cuenta ha sido bloqueada")
        unblock = input("\n¿Desea desbloquearla? (s/n) ")
        if unblock == "s":
            intentos2 = 0
            Login()
        elif unblock == "n":
            repetir = input("\n¿Desea repetir la tarea? (s/n) ")
            if repetir == "s":
                Login()
            elif repetir == "n":
                practica4()
    user = input("\nIntroduzca el nombre de usuario: ")
    if (user in password3):
        contra = input("Ingrese su contraseña: ")
        if contra == password3[user]:
            print("Inicio de sesión exitoso!")
        else:
            print("\nIntente nuevamente")
            intentos2 += 1
            Login()
            repetir = input("\n¿Desea repetir la tarea? (s/n) ")
            if repetir == "s":
                Login()
            elif repetir == "n":
                practica4()
        repetir = input("\n¿Desea repetir la tarea? (s/n) ")
        if repetir == "s":
            Login()
        elif repetir == "n":
            practica4()
    else:
        print("\nIntente nuevamente")
        intentos2 += 1
        Login()

#═════════════════════════════════Practica 4, Ejercicio 8

def p4e8():
    print("\nEscribir dos funciones que permitan calcular:",
          "\nLa cantidad de segundos en un tiempo dado en horas, minutos y segundos.",
          "\nLa cantidad de horas, minutos y segundos de un tiempo dado en segundos.",
          "\nEscribe un programa principal con un menú donde se pueda elegir la opción de convertir a",
          "\nsegundos, convertir a horas,minutos y segundos o salir del programa.",
          "\n1¿Que desea hacer?",
          "\n1. Convertir horas, minutos y segundos a segundos",
          "\n2. Convertir segundos en horas, minutos y segundos",
          "\n3. volver al menu anterior")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        convertirSegundos()
    elif opcion == "2":
        convertirHoras()
    elif opcion == "3":
        practica4()

def convertirSegundos():
    Horas = int(input("\nIngrese las horas: "))
    Minutos = int(input("Ingrese los minutos: "))
    Segundos = int(input("Ingrese los segundos: "))

    print("\nEn segundos esto es: "+str((Horas*3600)+(Minutos*60)+Segundos))
    repetir = input("\n¿Desea repetir la tarea? (s/n) ")
    if repetir == "s":
        convertirSegundos()
    elif repetir == "n":
        p4e8()

def convertirHoras():
    Segundos = int(input("Ingrese los segundos: "))
    Horas = (Segundos//3600)
    Minutos = ((Segundos%3600)//60)
    Segundos = ((Segundos%3600)%60)

    print(f"\nEn horas, minutos y segundos esto es: {Horas}:{Minutos}:{Segundos}")
    repetir = input("\n¿Desea repetir la tarea? (s/n) ")
    if repetir == "s":
        convertirHoras()
    elif repetir == "n":
        p4e8()

#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#════════════════════INVOCANDO AL MENU PRINCIPAL═════════════════════
#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

menuprincipal()
