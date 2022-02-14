#Crear lista
planets=["Mercury", "Venus", "Earth","Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# Agregamos a plutón y mostramos el último elemento
ultimo=len(planets)
planets.insert(ultimo,"Pluton")
print(planets[ultimo])
planets.pop(ultimo)
print(planets)
print(len(planets))
# Lista de planetas

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
planeta=input("Elije un planeta")
# Busca el planeta en la lista
menos=planets.index(planeta)
# Muestra los planetas más cercanos al sol
if menos !=0:
    
    print(f"el planeta mas cercano que {planeta},es: " + str(planets[menos-1]))
else: 
    print("Mercurio es el mas proximo al sol ")
planeta=input("Elije un planeta")
# Busca el planeta en la lista
menos=planets.index(planeta)
# Muestra los planetas más lejanos al sol
if menos !=8:
    
    print(f"el planeta mas cercano que {planeta},es: " + str(planets[menos+1]))
else: 
    print("Neptuno es el planeta mas lejano al sol ")
