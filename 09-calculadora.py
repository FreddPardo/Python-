print("Bienvenido a la Calculadora")
print("La operaciones son suma, multi, div y resta")
print("Para salir escribe Salir ")

res = ""
while True:
    if not res:
        res = input("Ingrese un numero: ")
        if res.lower() == "salir":
            break
        res = int(res)
    op = input("Ingresa Operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa el siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        res += n2
    elif op.lower() == "resta":
        res -= n2
    elif op.lower() == "multi":
        res *= n2
    elif op.lower() == "div":
        res /= n2
    else:
        print("operacion no valida")

    print(f"El resultado es  {res}")
