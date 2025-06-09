import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime
import os

# Diccionario de respuestas
respuestas = {
    "feliz": "¡Qué bueno! Me alegro que te sientas así, disfruta tu día <3",
    "triste": "Lo siento, recuerda que después de la tormenta sale el sol.",
    "enojado": "Respira y relájate, todo estará bien. Es cosa de tiempo <3",
    "aburrido": "¡Vamos a hacer algo divertido el día de hoy!",
    "estresado": "Recuerda que la vida es corta y hay que disfrutarla.",
    "ansioso": "Todo estará bien, no te preocupes. Todo pasa por algo.",
}

# Nombre del archivo CSV
archivo_csv = "estados_de_animo.csv"

# Función para registrar estado en CSV
def registrar_estado(estado):
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archivo_existe = os.path.isfile(archivo_csv)

    with open(archivo_csv, mode='a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        # Escribir encabezado si el archivo es nuevo
        if not archivo_existe:
            writer.writerow(["Estado de Ánimo", "Fecha y Hora"])
        writer.writerow([estado, ahora])

# Función que se ejecuta al presionar un botón
def mostrar_respuesta(estado):
    mensaje = respuestas.get(estado, "No reconozco este tipo de ánimo, pero espero que te sientas mejor pronto.")
    messagebox.showinfo("Mensaje para ti", mensaje)
    registrar_estado(estado)  # Guardar en CSV

# Crear ventana principal
ventana = tk.Tk()
ventana.title("¿Cómo te sientes hoy?")
ventana.geometry("400x350")
ventana.resizable(False, False)

# Etiqueta de título
etiqueta = tk.Label(ventana, text="¿Cómo te sientes el día de hoy?", font=("Helvetica", 14))
etiqueta.pack(pady=20)

# Crear botones para cada estado de ánimo
for estado in respuestas.keys():
    boton = tk.Button(
        ventana,
        text=estado.capitalize(),
        width=20,
        command=lambda estado=estado: mostrar_respuesta(estado)
    )
    boton.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
