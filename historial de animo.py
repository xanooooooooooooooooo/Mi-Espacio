import tkinter as tk 
from tkinter import ttk
# datos de ejemplo 
historial = [
{"fecha": "2025-09-06", "estado": "feliz", "nota": "que bueno me alegro que te sientas asi, disfruta tu dia"},
{"fecha": "2025-10-06", "estado": "triste", "nota": "lamento que te sientas asi, aqui estoy para lo que necesites"},
{"fecha": "2025-11-06", "estado": "enojado", "nota": "respira y relajate todo estara bien es cosa de tiempo"},
{"fecha": "2025-13-06", "estado": "aburrido", "nota": "vamos a hacer algo divertido el dia de hoy"},
{"fecha": "2025-14-06", "estado": "estresado", "nota": "recuerda que la vida es corta y hay que disfrutrala"},
{"fecha": "2025-15-06", "estado": "ansioso", "nota": "todo estara bien no te preocupes, todo pasa por algo"},
]
# crear ventana principal
ventana = tk.Tk()
ventana.title("historial de animo")
ventana.geometry("600x400")
#titulo 
titulo=tk.Label(ventana, text="historial de animo", font=("helvetica",16))
titulo.pack(pady=10)
#crear tabla 
tabla=ttk.Treeview(ventana, columns=("fecha", "estado", "nota"), show="headings")
tabla.heading("fecha", text="fecha")
tabla.heading("estado", text="estado")
tabla.heading("nota", text="nota")
#insertar datos en la tabla 
for entrada in historial: 
    tabla.insert("","end", values=(entrada["fecha"], entrada["estado"], entrada["nota"]))
    tabla.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    #ejecutar
ventana.mainloop()