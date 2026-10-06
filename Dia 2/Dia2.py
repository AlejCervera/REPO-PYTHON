from py_compile import main


contraseña = 'mimamamemima'
longitud_minima = 8
longitud_maxima = 20

#if len(contraseña) <= longitud_minima:
#    print(f'La longitud de la contraseña es muy corta, debe ser de al menos {longitud_minima}')     
#elif len(contraseña) <= longitud_maxima:
#    print('La longitud de la contraseña es válida, contraseña aceptada')
#else:
#    print(f'La longitud de la contraseña es muy larga, debe ser de menos de {longitud_maxima}')

#colores = ['rojo', 'verde', 'azul', 'amarillo']

#for i in colores:
#    print(i)

numero = 7

#while numero < 12:
#    print(numero)
#    numero += 1

#def saludar(nombre):
#
#    return f'Hola {nombre}'
#print(saludar('Sofia'))

#def cuentaCaracteres(cadena):
#    if isinstance(cadena, str):
#        contador = 0
#        for i in cadena:
#            contador += 1
#        return contador
#    else:
#        return "Debo ser ejecutada con un string"
#
#print(cuentaCaracteres('Mucho Elche'))

#letra = lambda palabra: palabra[-1]

#print(letra('Hola'))

def obtener_nombre_completo(nombre, apellido):
    return nombre + " " + apellido
    def main():
        usuarios = [
         {"nombre": "Sofía"},
         {"nombre": "Luis", "apellido": "Martínez"},
         ]

    for usuario in usuarios:
        completo = obtener_nombre_completo(usuario["nombre"], usuario["apellido"])
    print(completo)
main()
