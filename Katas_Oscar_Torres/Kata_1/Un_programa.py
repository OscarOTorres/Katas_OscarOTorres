from datetime import date
# Impirmir por pantalla
print("Hola Mundo desde la consola")
# Declaración de variables
distancia_a_alfa_centauri = 4.367

print(type(distancia_a_alfa_centauri))
print(f"la distancia entre la tierra y alfa centauri es de : {distancia_a_alfa_centauri} millones de kilometros")

# Fecha en pantalla Modulo DateTime()
hoy = date.today()
print(f"Hoy es: {hoy}")

# Conversión de datos
print("Hoy es: " + str(date.today()))

# Recopilar información
print("Bienvenido al programa de bienvenida")
name=input("Ingresa tu nombre: ")
print(f"Bienvenido {name}")

# Trabajar con numeros
print("Calculadora")
first_number=int(input("Primer número"))
second_number=int(input("segundo numero"))
print("La suma de ambos numeros es de " + str(first_number+second_number))

