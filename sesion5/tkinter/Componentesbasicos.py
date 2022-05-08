import tkinter as tk

def funcion():
    print("Se ha llamado a la función del Boton")

root = tk.Tk()

etiqueta = tk.Label(root, text="Etiqueta")
boton = tk.Button(root, text="Pulsa aqui", command=funcion)

etiqueta.pack()
boton.pack()

root.mainloop()
