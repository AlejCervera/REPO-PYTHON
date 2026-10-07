def descuento (precio, descuento):

    if descuento > 0 and descuento < 1:
        try:
            float(descuento)
            precio_final = f'precio*descuento'
        except:
            precio_final = f'Has introducido {descuento}, no es un valor entre 0 y 1'
    else:
        precio_final = f'Has introducido {descuento}, no es un valor entre 0 y 1'

    return precio_final