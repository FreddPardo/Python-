print("BIENVENIDO A LA CALCULADORA")
print("Las operaciones son suma, resta, multi, div")
print("para salir escribe salir")
res = int(input("Ingresa el primer numero: "))

for numero in range(10):
    oper = (input("ingresa el operador:"))
    if oper == "suma":
        n2 = int(input("ingresa el siguiente numero: "))
        res = res + n2
        print("El resultado de la operacion es: ", res)

    elif oper == "resta":
        n2 = int(input("ingresa el siguiente numero: "))
        res = res - n2
        print("El resultado de la operacion es: ", res)

    elif oper == "multi":
        n2 = int(input("ingresa el siguiente numero: "))
        res = res * n2
        print("El resultado de la operacion es: ", res)

    elif oper == "div":
        n2 = int(input("ingresa el siguiente numero: "))
        res = res / n2
        print("El resultado de la operacion es: ", res)
