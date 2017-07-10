# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect

# Importar clase base para Vistas.
# Las vistas manejan la logica del sitio web.
from django.views.generic import View

# Metodo render retorna una respuesta
# Combina una plantilla con un diccionario de contexto
# y retorna un objeto HttpResponse.
from django.shortcuts import render
from documentos.models import Documento


class Documentos(View):
    def get(self, request, *args, **kwargs):

        docs  = Documento.objects.all()
        context = {
            'docs': docs,
            'encabezado': 'Mis Documentos'
        }

        return render(
            request,
            'documentos.html',
            context
        )

