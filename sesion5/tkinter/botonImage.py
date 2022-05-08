import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.config(width=1000, height=500)
root.title("Botón en Tk")
img_boton = tk.PhotoImage(file="tkinter.png")
boton = ttk.Button(image=img_boton)
boton.place(x=50, y=50)
root.mainloop()  
