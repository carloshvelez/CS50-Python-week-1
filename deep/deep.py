def main():
    respuesta = input("¿Cuál es la respuesta a la gran pregunta de la vida? ")
    print(confirmar_respuesta(respuesta))

def confirmar_respuesta(respuesta):
    match respuesta.lower().strip():
        case "forty-two" | "42" | "forty two":
            return "Yes"
        case _:
            return "No"

main()

