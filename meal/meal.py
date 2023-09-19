def main ():
    consulta = input("¿Qué hora es? ")

    #Función para convertir en la hora en un decimal:
    h_convert = convert(consulta)

    if 7 <= h_convert <=8:
        print("breakfast time")
    elif 12 <= h_convert <=13:
        print("lunch time")
    elif 18 <= h_convert <=19:
        print("dinner time")

def convert(consulta):

    #Verifica si termina en am y lo quita.
    if consulta.endswith(("am", "Am", "AM", "a.m.", "A.m.", "A.M.")):
        consulta = consulta.strip(("aApPmM. "))
        hora, minutos = consulta.split(":")

    #Verifica si termina en pm, lo quita y le suma 12 a la hora.
    elif consulta.endswith(("pm", "Pm", "PM", "p.m.", "P.m.", "P.M.")):
        consulta = consulta.strip(("aApPmM. "))
        hora, minutos = consulta.split(":")
        hora = int(hora) + 12

    else:
        hora, minutos = consulta.split(":")

    h_convert = float(int(hora) + int (minutos)/60)

    return h_convert





if __name__ == "__main__":
    main()

