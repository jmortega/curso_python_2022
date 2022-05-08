import tkinter as tk
from tkinter import ttk


def convertir_temp():
    temp_celsius = float(caja_temp_celsius.get())
    temp_kelvin = temp_celsius + 273.15
    temp_fahrenheit = temp_celsius*1.8 + 32
    etiqueta_temp_kelvin.config(text=f"Temperatura en K: {temp_kelvin}")
    etiqueta_temp_fahrenheit.config(
        text=f"Temperatura en ºF: {temp_fahrenheit}")


ventana = tk.Tk()
ventana.title("Conversor de temperatura")
ventana.config(width=400, height=300)

etiqueta_temp_celsius = ttk.Label(text="Temperatura en ºC:")
etiqueta_temp_celsius.place(x=20, y=20)

caja_temp_celsius = ttk.Entry()
caja_temp_celsius.place(x=140, y=20, width=60)

boton_convertir = ttk.Button(text="Convertir", command=convertir_temp)
boton_convertir.place(x=20, y=60)

etiqueta_temp_kelvin = ttk.Label(text="Temperatura en K: n/a")
etiqueta_temp_kelvin.place(x=20, y=120)

etiqueta_temp_fahrenheit = ttk.Label(text="Temperatura en ºF: n/a")
etiqueta_temp_fahrenheit.place(x=20, y=160)

ventana.mainloop()
