def main():
    solicitud = input("Por favor ingrese la operación que quiere realizar: ")
    print(calcular(solicitud))

def calcular(solicitud):
     n1, operador, n2= solicitud.split()
     if operador == "+":
         return float(n1) + float(n2)
     elif operador == "/":
         return float(n1) / float(n2)
     elif operador == "-":
         return float(n1) - float(n2)
     elif operador == "*":
         return float(n1) * float(n2)

main()