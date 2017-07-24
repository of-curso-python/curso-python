import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MiVentana(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):

        super(MiVentana, self).__init__(*args, **kwargs)
        self.set_default_size(500, 300)

        self.agregar_contenedor()
        self.agregar_entrada()
        self.agregar_boton()
        self.agregar_lista()

    def agregar_contenedor(self):
        self.contenedor = Gtk.Grid()
        self.contenedor.set_column_homogeneous(True)
        self.add(self.contenedor)

    def agregar_entrada(self):
        self.entrada = Gtk.Entry()
        self.entrada_monto = Gtk.Entry()
        self.entrada_monto.connect('activate', self.agregar_fila)

        self.contenedor.attach(self.entrada, 0, 0, 2, 1)

        self.contenedor.attach_next_to(
            self.entrada_monto,
            self.entrada,
            Gtk.PositionType.RIGHT,
            1,
            1
        )

    def agregar_boton(self):
        self.boton = Gtk.Button('Agregar')
        self.contenedor.attach_next_to(
            self.boton,
            self.entrada,
            Gtk.PositionType.BOTTOM,
            3,
            1
        )
        # conecta el metodo self.agregar_fila al evento "clicked"
        # de self.boton
        self.boton.connect('clicked', self.agregar_fila)

    def agregar_lista(self):
        """ Crea un TreeView:

        1 - Crear el model de datos Gtk.ListStore(type, type, ..., type)
        2 - Crear el Widget que contiene o muestra los datos de modelo.
        TreeView(<model>)
        3 - Definir Las columnas y su contenido.

        3.1 - Crear Celda para cada columna de la fila.
        Los CellRenderer son widgets que sirven para mostrar contenido dentro de
        otros widgets dependiendo de su tipo.
        3.2 - Crear Columnas(TreeViewColumn) del TreeView que mostraran los datos
        usando CellRenderer widgets como elementos hijos.
        args: (Titulo, cellRenderer, posicion en el modelo de la info a mostrar.)
        3.3 - Agregar cada TreeViewColumn al TreeView widget.

        """
        self.modelo =  Gtk.ListStore(str, float)

        self.lista_activos = Gtk.TreeView(self.modelo)

        descripcion = Gtk.CellRendererText()
        columna_descripcion = Gtk.TreeViewColumn(
            'Descripcion',
            descripcion,
            text=0
        )

        monto = Gtk.CellRendererText()
        columna_monto = Gtk.TreeViewColumn('Monto', monto, text=1)

        self.lista_activos.append_column(columna_descripcion)
        self.lista_activos.append_column(columna_monto)

        self.contenedor.attach_next_to(
            self.lista_activos,
            self.boton,
            Gtk.PositionType.BOTTOM,
            3,
            1
        )

    def agregar_fila(self, btn):
        texto = self.entrada.get_text()
        monto = self.entrada_monto.get_text()
        self.modelo.append([texto, float(monto)])


if __name__ == '__main__':
    ventana = MiVentana()
    ventana.show_all()

    Gtk.main()
