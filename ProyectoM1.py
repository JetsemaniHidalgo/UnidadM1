def inputNombre(message):#Validación de nombre solo datos str
    while True:
        Nombre = input(message)
        if Nombre.isalpha():
            return Nombre
        else:
            print("Error: Ingrese su nombre correctamente utilizando solo letras.")
def inputApellidoP(message):#Validación de apellido paterno solo datos str
    while True:
        ApellidoP = input(message)
        if ApellidoP.isalpha():
            return ApellidoP
        else:
            print("Error: Ingrese su nombre correctamente utilizando solo letras.")
def inputApellidoM(message):#Validación de apellido paterno solo datos str
    while True:
        ApellidoM = input(message)
        if ApellidoM.isalpha():
            return ApellidoM
        else:
            print("Error: Ingrese su nombre correctamente utilizando solo letras.")

def inputEdad(message):#Validación de Edad solo datos int
  while True:
    try:
       Edad = int(input(message))       
    except ValueError:
       print("Error: ¡Debe ingresar una edad numérica!")
       continue
    else:
       return Edad
    
def inputPeso(message):#Validación de Peso solo datos int
  while True:
    try:
       Peso = float(input(message))       
    except ValueError:
       print("Error: ¡Debe ingresar un valor numérico!")
       continue
    else:
       return Peso
    
def inputEstatura(message):#Validación de Estatura solo datos int
  while True:
    try:
       Altura = float(input(message))       
    except ValueError:
       print("Error: ¡Debe ingresar su estatura en metros ejemplo:1.72!")
       continue
    else:
       return Altura

#Programa principal
print("Bienvenido a la calculadora de IMC")
Nombre= inputNombre("\nIngrese su nombre: ")
ApellidoP= inputNombre("\nIngrese su apellido parterno por favor: ")
ApellidoM= inputNombre("\nIngrese su apeliido materno por favor: ")
Edad = inputEdad("\nIngrese su edad por favor: ")
Peso = inputPeso("\nIngrese su peso en kilogramos por favor: ")
Altura = inputEstatura("\nIngrese su estastura en metros por favor: ")
IMC = Peso / Altura**2
print(f"Hola {Nombre} {ApellidoP} {ApellidoM}, tu IMC es de: {IMC:.2f}")
#Con la sentencia If se compara el valor del IMC para determinar la categoría de peso
if IMC >= 0 and IMC <= 15.99 :
        print ("Usted presenta: Delgadez severa")
elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Usted presenta: Delgadez moderada")
elif IMC >= 17.00 and IMC <= 18.49:
        print ("Usted presenta: Delgadez leve")
elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Usted se encuentra: Normal")
elif IMC >= 25.00 and IMC <= 29.99:
        print ("Usted presenta: Sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
        print ("Usted presenta: Obesidad leve")
elif IMC >= 35.00 and IMC <= 39.00:
        print ("Usted presenta: obesidad media")
elif IMC >= 40.00:
        print ("Usted presenta: Obesidad morbida")