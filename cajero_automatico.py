"""
Este programa funciona como cajero automático interactivo para utilizar hasta que
el inventario quede vacío o el usuario desee salir oprimiendo '0'. El sistema se 
puede reutilizar fácilmente editando o agregando más valores al inventario, así 
como la cantidad de billetes disponibles.

El usuario debe escribir manualmente un monto a retirar y el cajero tratará de 
dispensar dicha cantidad con la menor cantidad de billetes posibles comenzando
con el de mayor denominación; Si no puede dispensar esa cantidad imprime msj.

Cuando quedan $1000 o menos en el inventario el sistema genera una alerta.

Autor: JorgeAdx
Fecha: 28 de septiembre de 2025
"""
inventario = {    # Define inventario de forma global
    1000: 10,    # Comienza con 10 billetes por unidad
    500: 10,
    200: 10,
    100: 10,
    50: 10,
    20: 10
}


def total_efectivo_disponible():
    """Calcula el total de dinero disponible en el cajero"""
    return sum(denominac * cantidad_bill for denominac, cantidad_bill in inventario.items())    # Realiza sumatoria del efectivo total


def verificar_fondos():
    """Verifica si se requiere recargar el cajero"""
    total = total_efectivo_disponible()
    if total <= 1000:    # Verifica el monto a la izquierda para imprimir advertencia (VALOR EDITABLE)
        print("\nATENCIÓN: El cajero requiere ser llenado nuevamente.")


def dispensar_billetes(monto_solicitado):    # Define función principal
    global inventario    # Modifica variable global

    if monto_solicitado <= 0 or monto_solicitado % 10 != 0:    # Verifica monto válido para realizar el retiro
        print("Ingrese un monto válido mayor a cero y múltiplo de 10.")
        return    # Salta función si se cumple condición

    entrega = {}
    cambio_restante = monto_solicitado    # Iguala var. Para hacer realizar verificación después

    for valor in sorted(inventario.keys(), reverse=True):    # Itera sobre inventario de forma descendente
        cantidad_disponible = inventario[valor]    # Define cuántos billetes por tipo hay en el cajero
        cantidad_necesaria = cambio_restante // valor    # Define billetes necesarios para cambio restante
        cantidad_a_entregar = min(cantidad_disponible, cantidad_necesaria)    # Define cantidad mínima posible

        if cantidad_a_entregar > 0:    # Verifica si se entregará el efectivo
            entrega[valor] = cantidad_a_entregar
            cambio_restante -= cantidad_a_entregar * valor

    if cambio_restante == 0:
        print("\nBilletes entregados:")
        for valor in sorted(entrega.keys(), reverse=True):    # Itera y otorga las denominaciones a dispensar
            cantidad = entrega[valor]
            mostrar_billete_s = "billete" if cantidad == 1 else "billetes"    # Define billete o billetes
            print(f"${valor}: {cantidad} {mostrar_billete_s}")    # Imprime denominación y num. De billetes
            inventario[valor] -= cantidad    # Actualiza el inventario

        verificar_fondos()

    else:
        print("No hay combinación suficiente para dispensar ese monto.")


print("\n--- Esta es una dispensadora de billetes ---")

while True:    # Se tratará de ejecutar hasta que el usuario ingrese '0'
    entrada = input("\nIngrese el monto a retirar (0 para salir): ")
    try:    # Define excepción en programa
        monto_solicitado = int(entrada)
        if monto_solicitado == 0:    
            print("Saliendo del programa. Gracias.")
            break    # Finaliza la función principal al leer '0'
        dispensar_billetes(monto_solicitado)    # Entrega efectivo en casos esperados
    except ValueError:    # Maneja error de unidad
        print("Por favor, ingrese un número válido.")

