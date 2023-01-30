print("ingresar Nombre de perro")
Nombre = input()
print("ingresa el Peso")
Peso = input()+("Kg")

from datetime import date

anio=int(input("ingresar año de Nacimiento:"))
mes=int(input("ingresar mes de nacimiento:" ))
dia=int(input("ingresar dia de nacimiento:" ))

anioActual = date.today().year
mesActual = date.today().month
diaActual= date.today().day

edad= anioActual-anio

if mes > mesActual:
    if dia > diaActual:
        edad = edad - 1 
     
    
else:
    print("Edad del Perro es",edad)

if mes > mesActual:
    if dia < diaActual:
        edad = edad - 1
        

print("Datos del perro:")
print("Nombre:", Nombre)
print("Peso: ", Peso)
print("Edad de "+ Nombre,"es:",edad)