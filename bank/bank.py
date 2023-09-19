def main():
    saludo = input("Saludo: ")
    print(pago(saludo))

def pago(saludo):
    if saludo.lower().strip().startswith("hello"):
        return "$0"
    elif saludo.lower().strip().startswith("h"):
        return "$20"
    else:
        return "$100"

main()
