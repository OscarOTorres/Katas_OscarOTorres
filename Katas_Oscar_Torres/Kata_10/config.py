def agua_restante(astronautas,agua,dias):
    for argument in [astronautas, agua, dias]:
        try:
            
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
                # TypError will be raised only if it isn't the right type 
                # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    uso_de_agua=astronautas*11
    total_de_agua=uso_de_agua*dias
    agua_queda=agua-total_de_agua
    if agua_queda<0:
        raise RuntimeError( f"No habra suficiente agua antes de {dias} dias para {astronautas} astronautas")
    return f"el agua restante despues de {dias} dias es de {agua_queda}"
#aguas=agua_restante(5,100,2)
#print(aguas)

try:
    agua_restante(5, 100, 2)
    print(agua_restante(5,200,2))
except RuntimeError as err:
    print(err)