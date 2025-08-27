import tkinter as tk

# 1. Crear la ventana principal (a menudo llamada 'root' o 'ventana')
ventana = tk.Tk()

# 2. Personalizar la ventana
ventana.title("Mi Primera App")  # Establece el título
ventana.geometry("500x400")      # Define el tamaño inicial (Ancho x Alto)
ventana.resizable(False, False)  # Impide que se pueda cambiar el tamaño (Ancho, Alto)
ventana.config(bg="lightblue")   # Cambia el color de fondo

# 3. Iniciar el bucle de eventos
# Este método mantiene la ventana abierta y escucha las interacciones del usuario.
# Debe ser la última línea del script de la GUI.
ventana.mainloop()
