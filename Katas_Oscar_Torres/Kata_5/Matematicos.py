tierra=149597870
jupiter=778547200

# ¡Asegúrate de quitar las comas!
distancia = tierra-jupiter 
print("la distancia entre la tierra y jupiter es : " + str(abs(distancia)))
print("la distancia entre la tierra y jupiter en millas es: " + str(abs(distancia *0.621))+ " millas")
planeta1=input("primer planeta")
planeta2=input("segundo planeta")
planeta1 =int(planeta1)
planeta2 =int(planeta2)
distancia = abs(planeta1-planeta2)


# Convertir de KM a Millas
distancia1= distancia*0.621
print("la distancia entre ambos planetas es: " + str(distancia))
print(str(distancia1)+" millas")