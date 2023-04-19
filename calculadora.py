print("Bienvenido a la Calculadora")
print("La operaciones son suma, multi, div y resta")
print("Para salir escribe Salir ")
res = int(input("Ingresa primer numero: "))

for numero in range(10):
    oper = input("Ingresa el operador: ")
    if oper == "suma":
        n2 = int(input("Ingresa siguiente numero: "))
        res = (res + n2)
        print("el resultado de la suma es: ", res)

    elif oper == "resta":
        n2 = int(input("Ingresa siguiente numero: "))
        res = (res - n2)
        print("el resultado de la resta es: ", res)

    elif oper == "multi":
        n2 = int(input("Ingresa siguiente numero: "))
        res = (res * n2)
        print("el resultado de la resta es: ", res)

    elif oper == "div":
        n2 = int(input("Ingresa siguiente numero: "))
        res = (res / n2)
        print("el resultado de la resta es: ", res)
    elif oper == "salir":
        break
