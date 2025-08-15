# Captura dos números
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

print("captura de nuemros :", numero1, "y", numero2)

# Compara los números y muestra el mayor
if numero1 > numero2:
    print("El número mayor es:", numero1)
elif numero2 > numero1:
    print("El número mayor es:", numero2)
else:
    print("Ambos números son iguales.")

