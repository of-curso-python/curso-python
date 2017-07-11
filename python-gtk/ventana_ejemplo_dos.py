import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


if __name__ == '__main__':

    ventana = Gtk.Window(title='Ejemplo 2')
    ventana.connect('delete-event', Gtk.main_quit)
    ventana.set_default_size(200, 200)

    boton = Gtk.Button('Btn 1')
    boton2 = Gtk.Button('Boton 2')

    contenedor = Gtk.Grid()
    contenedor.set_column_homogeneous(True)
    contenedor.set_row_homogeneous(True)

    contenedor.attach(
        boton, # Elemento
        0, # columna
        0, # fila
        3, # Nro Columnas a usar
        1, # Nro Filas a usar
    )

    contenedor.attach(boton2, 0, 1, 3, 1)
    ventana.add(contenedor)
    ventana.show_all()

    Gtk.main()
