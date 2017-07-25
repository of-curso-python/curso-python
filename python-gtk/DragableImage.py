import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk, GdkPixbuf


class DragableImage(Gtk.Button):
    def __init__(self, nombre_archivo, width=150, height=150, *args, **kwargs):
        super(DragableImage, self).__init__(*args, **kwargs)

        # Cargar una imagen
        temp_image = Gtk.Image.new_from_file(nombre_archivo)
        # Obtener pixbuf:
        # Contiene info sobre datos de pixeles de la imagen,
        # su espacio de color, ancho y alto
        buf_image = temp_image.get_pixbuf()

        # Nuevo pixbuf de imagen redimensionada.
        resized_pixbuf = buf_image.scale_simple(
            width,
            height,
            GdkPixbuf.InterpType.BILINEAR
        )

        imagen= Gtk.Image()
        imagen.set_from_pixbuf(resized_pixbuf)

        self.set_image(imagen)

        # Establecer imagen como origin de DragNDrop.
        self.drag_source_set(
            Gdk.ModifierType.BUTTON1_MASK,
            [],
            Gdk.DragAction.COPY
        )

        self.drag_source_set_icon_pixbuf(resized_pixbuf)
