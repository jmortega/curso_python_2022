import tkinter as tk

def archivo_nuevo_presionado(event=None):
    print("¡Has presionado para crear un nuevo archivo!")

def menu_iniciar_con_sistema_presionado():
    if iniciar_con_sistema.get():
        print("Opción establecida (iniciar con el sistema).")
    else:
        print("Opción deshabilitada (no iniciar con el sistema).")

def menu_tema_presionado():
    valor_tema = tema_elegido.get()
    if valor_tema == 1:
        print("Tema claro establecido.")
    elif valor_tema == 2:
        print("Tema oscuro establecido.")

ventana = tk.Tk()
ventana.title("Barra de menús en Tk")
ventana.config(width=400, height=300)
barra_menus = tk.Menu()
menu_archivo = tk.Menu(barra_menus, tearoff=False)
img_menu_nuevo = tk.PhotoImage(file="tkinter.png")
menu_archivo.add_command(
    label="Nuevo",
    accelerator="Ctrl+N",
    command=archivo_nuevo_presionado,
    image=img_menu_nuevo,
    compound=tk.LEFT
)
ventana.bind_all("<Control-n>", archivo_nuevo_presionado)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.destroy)
menu_opciones = tk.Menu(barra_menus, tearoff=False)
iniciar_con_sistema = tk.BooleanVar()
menu_opciones.add_checkbutton(
    label="Iniciar con sistema",
    command=menu_iniciar_con_sistema_presionado,
    variable=iniciar_con_sistema
)
menu_tema = tk.Menu(barra_menus, tearoff=False)
tema_elegido = tk.IntVar()
tema_elegido.set(1)  # Opción seleccionada por defecto ("Claro").
menu_tema.add_radiobutton(
    label="Claro",
    variable=tema_elegido,
    value=1,
    command=menu_tema_presionado
)
menu_tema.add_radiobutton(
    label="Oscuro",
    value=2,
    variable=tema_elegido,
    command=menu_tema_presionado
)
menu_opciones.add_cascade(menu=menu_tema, label="Tema")
barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
barra_menus.add_cascade(menu=menu_opciones, label="Opciones")
ventana.config(menu=barra_menus)
ventana.mainloop()
