from tkinter import messagebox, ttk
import tkinter as tk


class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Combobox")
        self.combo = ttk.Combobox(
            self,
            state="readonly",
            values=["Python", "C", "C++", "Java"]
        )
        self.combo.place(x=50, y=50)
        self.button = ttk.Button(
            text="Mostrar selección",
            command=self.show_selection
        )
        self.button.place(x=50, y=100)
        main_window.config(width=300, height=200)
        self.place(width=300, height=200)

    def show_selection(self):
        # Obtener la opción seleccionada.
        selection = self.combo.get()
        messagebox.showinfo(
            message=f"La opción seleccionada es: {selection}",
            title="Selección"
        )


main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
