def main():
    nombre_archivo = input("Ingrese el nombre de archivo: ").lower().strip()
    print(tipo_archivo(nombre_archivo))

def tipo_archivo(nombre_archivo):
    if nombre_archivo.endswith((".gif", ".png",)):
        nombre, punto, extension = nombre_archivo.rpartition(".")
        return "image/" + extension

    elif nombre_archivo.endswith((".pdf", ".zip")):
        nombre, punto, extension = nombre_archivo.rpartition(".")
        return "application/" + extension

    elif nombre_archivo.endswith((".txt")):
        return "text/plain"

    elif nombre_archivo.endswith((".jpg", ".jpeg")):
        return "image/jpeg"

    else:
        return "application/octet-stream"


main()

