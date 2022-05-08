import tkinter as tk

def prueba_radio():
	print("Opcion seleccionada:" + variable.get())

def prueba_check():
	print("Check value:" + str(bool_var.get()))
	
root = tk.Tk()
variable = tk.StringVar()

bool_var = tk.BooleanVar()
check = tk.Checkbutton(root, text="Probando", variable=bool_var, command=prueba_check)
check.pack()

radiobutton1 = tk.Radiobutton(text="Opcion 1", variable=variable, value=1, command=prueba_radio)
radiobutton2 = tk.Radiobutton(text="Opcion 2", variable=variable, value=2, command=prueba_radio)
radiobutton3 = tk.Radiobutton(text="Opcion 3", variable=variable, value=3, command=prueba_radio)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

root.mainloop()
