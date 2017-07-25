# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio, GLib

from ventana_practica import MiVentana
from DragNDropImages import DragNDropImagesWindow


class CursoPythonApp(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super(CursoPythonApp, self).__init__(
            *args,
            application_id='of.cursopython.cursopythonapp',
            **kwargs
        )

        self.window = None

    def do_activate(self):

        if not self.window:
           self.window = MiVentana(application=self, title='Ventana Principal')
        self.window.show_all()
        self.window.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)
        accion_otra_ventana = Gio.SimpleAction.new('balance', None)
        accion_otra_ventana.connect('activate', self.crear_balance)
        self.add_action(accion_otra_ventana)

        accion_drag_n_drop = Gio.SimpleAction.new('drag_n_drop', None)
        accion_drag_n_drop.connect('activate', self.drag_n_drop)
        self.add_action(accion_drag_n_drop)

        builder = Gtk.Builder.new_from_file('menu.xml')
        self.set_app_menu(builder.get_object('app-menu'))

    def crear_balance(self, action, params):
        print 'Ejecutar una acción'

    def drag_n_drop(self, action, params):
        self.window_dos = DragNDropImagesWindow(
            application=self,
            title='Drag N Drop'
        )

        self.window_dos.show_all()
        self.window_dos.present()


if __name__ == '__main__':
    app = CursoPythonApp()
    app.run()

