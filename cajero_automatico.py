# AUTOR: JORGE ARGÜELLES                                                                                                    
inventario = {                                                                                      # Agrega el inventario fuera de la función para que sea global y se actualice por cada uso
    1000: 10,                                                                                       # Agrega las denominaciones de billetes más comunes con 10 billetes por unidad
    500: 10,
    200: 10,
    100: 10,
    50: 10,
    20: 10
}


def total_efectivo_disponible():
    """Calcula el total de dinero disponible en el cajero"""
    return sum(denominac * cantidad_bill for denominac, cantidad_bill in inventario.items())        # Retorna la suma de todos los productos de cada denominación multiplicado por la cantidad de billetes


def verificar_fondos():
    """Verifica si se requiere recargar el cajero"""
    total = total_efectivo_disponible()
    if total <= 1000:                                                                               # Verifica si el efectivo total es menor o igual a 1000, si se cumple esto, muestra advertencia en pantalla
        print("\nATENCIÓN: El cajero requiere ser llenado nuevamente.")


def dispensar_billetes(monto_solicitado):                                                           # Realiza el desarrollo de la función de la dispensadora partiendo del inventario inicial
    global inventario                                                                               # Modifica la variable global 'inventario'    

    if monto_solicitado <= 0 or monto_solicitado % 10 != 0:                                         # Verifica que el monto sea mayor a cero y múltiplo de diez para realizar el retiro
        print("Ingrese un monto válido mayor a cero y múltiplo de 10.")                             # Imprime mensaje en pantalla y salta la función si no cumple lo esperado
        return                                                                                      # Finaliza la función en esta situación

    entrega = {}                                                                                    # Crea variable vacía llamada entrega
    cambio_restante = monto_solicitado                                                              # Iguala el cambio restante junto con el monto ingresado por el usuario

    for valor in sorted(inventario.keys(), reverse=True):                                           # Recorre el bucle desde el billete más grande al más chico
        cantidad_disponible = inventario[valor]                                                     # Define cuántos billetes por tipo hay en el cajero
        cantidad_necesaria = cambio_restante // valor                                               # Define cuántos billetes se necesitarían para cubrir el cambio restante
        cantidad_a_entregar = min(cantidad_disponible, cantidad_necesaria)                          # Define cantidad mínima necesaria respecto a la cantidad disponible

        if cantidad_a_entregar > 0:                                                                 # Verifica si se entregará el efectivo
            entrega[valor] = cantidad_a_entregar
            cambio_restante -= cantidad_a_entregar * valor

    if cambio_restante == 0:                                                                        # Verifica si existe cambio sobrante del dinero del usuario
        print("\nBilletes entregados:")                                                             # Imprime mensaje en pantalla
        for valor in sorted(entrega.keys(), reverse=True):                                          # Recorre secuencialmente cada billete a entregar, 'entrega.keys' Otorga las denominaciones a dispensar
            cantidad = entrega[valor]
            mostrar_billete_s = "billete" if cantidad == 1 else "billetes"                          # Declara variable para imprimir billete o billetes según sea el caso
            print(f"${valor}: {cantidad} {mostrar_billete_s}")                                      # Imprime cada denominación a entregar junto con su cantidad         
            inventario[valor] -= cantidad                                                           # Actualiza el inventario

        verificar_fondos()                                                                          # Llama a la función para verificar fondos del inventario

    else:
        print("No hay combinación suficiente para dispensar ese monto.")                            # Imprime mensaje en caso de que no se cumplan las condiciones anteriores


print("\n--- Esta es una dispensadora de billetes ---")                                             # Inicia el programa principal

while True:                                                                                         # Utiliza bucle para el flujo correcto del programa
    entrada = input("\nIngrese el monto a retirar (0 para salir): ")                                # Imprime mensaje en pantalla para interactuar con el usuario
    try:                                                                                            # Define excepción en programa
        monto_solicitado = int(entrada)
        if monto_solicitado == 0:                                                                   # Termina el programa si el usuario ingresa '0'
            print("Saliendo del programa. Gracias.")
            break                                                                                   # Termina la función
        dispensar_billetes(monto_solicitado)                                                        # Realiza la entrega de efectivo en casos normales
    except ValueError:                                                                              # Maneja error mostrando mensaje al usario
        print("Por favor, ingrese un número válido.")