import json
import os
import matplotlib.pyplot as plt

log_file = "mqtt_capture.log"
ALTURA_GRAFICA = 20


def leer_log_file():

    lineas = []

    try:
        with open(log_file, "r") as f:
            for linea in f:
                lineas.append(linea)

    except FileNotFoundError:
        print("Log file no encontrado")

    return lineas


def extraer_values(lineas):

    values = []

    for linea in lineas:

        if "Payload:" in linea:

            text_json = linea.split("Payload:", 1)[1].strip()

            try:
                data = json.loads(text_json)

                for value in data.values():

                    if isinstance(value, (int, float)):
                        values.append(value)

            except json.JSONDecodeError:
                pass

    return values


def crear_PNG(values):

    os.makedirs("plots", exist_ok=True)

    plt.plot(values)
    plt.grid()
    plt.title("datos del sensor")
    plt.xlabel("indice")
    plt.ylabel("Value")
    plt.savefig("plots/data.png")
    plt.close()

    print("PNG grafica guardada")


def grafica_ASCII(values):

    if len(values) == 0:
        print("no hay datos para monstrar")
        return

    max_value = int(max(values))
    ancho = len(values)

    scaled_values = []

    for v in values:

        level = int((v/max_value) * ALTURA_GRAFICA)
        scaled_values.append(level)

    print("\n Grafica ASCII \n")
    
    for y in range(ALTURA_GRAFICA, -1, -1):

        linea = ""
        if y == ALTURA_GRAFICA:
            linea += f"{max_value:>3} |"
        elif y == 0:
            linea += " 1 |"
        else:
            linea += "   |" 
         
        for x in range(ancho):
            if scaled_values[x] == y:
                linea += " * "
            else:
                linea += "   "
        
    print(linea)
    print("  +" + "---" * ancho)

    linea_form = "    "
    for i in range(ancho):
        linea_form += f"{i:>3}"
    print(linea_form)

    print("\n ultimos valores:", values)    


def main():

    lineas = leer_log_file()

    values = extraer_values(lineas)

    crear_PNG(values)

    grafica_ASCII(values)


if __name__ == "__main__":
    main()
