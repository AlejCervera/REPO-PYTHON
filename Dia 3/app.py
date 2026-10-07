import saludos

nombre = input("¿Cómo te llamas máquina? ")

if nombre == "Alejandro":
    print(saludos.insultar(nombre))
else:
    print(saludos.saludar(nombre))