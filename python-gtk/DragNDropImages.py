import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk
from DragableImage import DragableImage


class DragNDropImagesWindow(Gtk.ApplicationWindow):

    def __init__(self, *args, **kwargs):
        super(DragNDropImagesWindow, self).__init__(*args, **kwargs)
        self.set_default_size(1024, 768)

        scrolled_window = Gtk.ScrolledWindow()
        self.grid = Gtk.Grid()
        scrolled_window.add(self.grid)
        self.add(scrolled_window)

        self.main()

    def main(self):
        """ Ejemplo simple de como agregar origen y destino
        para DnD con imagenes
        """

        # Crear targets de origen y destino.
        self.targets = Gtk.TargetList.new([])
        self.targets.add_image_targets(1, True)
        #####################################################
        # Crear el widget de origen
        #####################################################
        img_widget_origen = self.cargar_imagen('tijera.jpg')
        # Agregamos un nombre al widget para usarlo como identificador
        # en los callbacks conectados a los eventos de DnD cuando sea
        # necesario.
        img_widget_origen.set_name('Las tijeras')
        # Conecta evento drag-data-get a self.on_drag_data_get.
        img_widget_origen.connect('drag-data-get', self.on_drag_data_get)

        # Agregar img_widget_origen al Grid.
        self.grid.attach(img_widget_origen, 0, 0, 1, 1)

        ###################################################
        # Crear un widget que sirva de destino.
        ###################################################

        img_widget_destino = self.agregar_destino_de_imagen('img 1')
        self.grid.attach_next_to(img_widget_destino, img_widget_origen, Gtk.PositionType.RIGHT, 1, 1)

        ###################################################
        # Agregar target list comun a origen y destino.
        ###################################################
        # Agregar targets a img_widget_destino.
        img_widget_destino.drag_dest_set_target_list(self.targets)
        # Agregar targets a image_widget
        img_widget_origen.drag_source_set_target_list(self.targets)



    def cargar_imagen(self, nombre_archivo):
        """
        Carga imagen desde un archivo, redimensiona la imagen
        y retorna una instancia de DragableImage.

        """
        dragable_image = DragableImage(nombre_archivo)
        return dragable_image

    def on_drag_data_get(self, widget, drag_context, data, info, time):
        """ Callback ejecutado en evento 'drag-data-get'. Este se utiliza
        comunmente para obtener la info que se pasa desde el
        widget origen al widget destino.
        """
        print 'on drag data get'
        print widget.get_name()
        img = widget.get_image()
        data.set_pixbuf(img.get_pixbuf())
        data.set_text(widget.get_name(), -1)

    def agregar_destino_de_imagen(self,  nombre):
        """ Agrega un widget Gtk.Button como placeholder.
        Sirve como destino.
        """
        widget_destino = Gtk.Button()
        widget_destino.set_name(nombre)
        # Habilitar el Image vacio como destino
        widget_destino.drag_dest_set(
            Gtk.DestDefaults.ALL,
            [],
            Gdk.DragAction.COPY
        )
        # Conectar callback en evento 'drag-data-received'
        widget_destino.connect(
            "drag-data-received",
            self.on_drag_data_received
        )

        return widget_destino

    def on_drag_data_received(self, widget, drag_context, x, y, data, info, time):
        """ Callback ejecutado en evento 'drag-data-received'. Este se utiliza
        comunmente para terminar de transferir los datos de origin al widget destino.

        """
        print 'Datos recibidos', data
        new_img = Gtk.Image()
        new_img.set_from_pixbuf(data.get_pixbuf())
        widget.set_image(new_img)

        # Destruir origen.
        source_widget = Gtk.drag_get_source_widget(drag_context)
        if source_widget.get_name() == 'Las tijeras':
            source_widget.destroy()
