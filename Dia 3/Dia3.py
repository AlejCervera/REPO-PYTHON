#lista_edades = [15, 22, 17, 30, 65, 45, 70, 19]

#for edad in lista_edades:
#    if edad >= 65:
#        print(f'Tienes {edad} años, más viejo que la tos')
#        break
#    elif edad > 18:
#        print(f'Tienes {edad} años, eres mayor de edad, puedes beber alcohol e ir a la cárcel')
#    else:
#        print(f'Tienes {edad} años, eres menor de edad, no puedes beber alcohol ni ir a la cárcel, pringao')ç

i = 0
correcto = False
while i <= 5:
    cosa = input('Introduce un número: ')
    try:
        int(cosa)
        print(f'Has introducido {cosa}, es un entero')
        correcto = True
        break
    except:
        print(f'Has introducido {cosa}, no es un entero, vuelve a intentarlo')
        i += 1
    finally:
        if correcto:
            print('Programa finalizado correctamente')
        elif i > 5:
            print('Se acabaron los intentos, programa finalizado')
        elif i == 5:
            print('Último intento, si fallas se acabó')
        elif cosa == 'Hola Mundo':
            print('Has introducido la frase secreta, eres un tolai, programa finalizado')
            break
        else:
            print(f'Te quedan {5 - i} intentos')
