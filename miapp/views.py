import json
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import View
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Hito, tipohito, tiposegmento
from .serializer import HitoSerialiazer
from rest_framework import viewsets, permissions
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import EsDeveloper
from django.utils import timezone
from datetime import datetime


def index(request):
    hitosvigente = Hito.objects.filter(fecha_termino__gt=datetime.now())
    user = request.user
    hitosuser = Hito.objects.filter(segmento=user.userrol.rol)[:3]
    context = {
        'hitosvigentes':hitosvigente,
        'tipohitos':tipohito,
        'tiposegmento':tiposegmento,
        'hitosuser':hitosuser
    }

    return render(request, 'miapp/index.html', context)

def SegmentoHitoView(request, segmentobuscado):
    este = ''
    for x in tiposegmento:
        if segmentobuscado == x[1]:
            este = x[0]
    hitosvigentes = Hito.objects.filter(segmento=este).filter(fecha_termino__gt=datetime.now())
    user = request.user
    hitosuser = Hito.objects.filter(segmento=user.userrol.rol)[:3]
    context = {
        'hitosvigentes':hitosvigentes,
        'tipohitos':tipohito,
        'tiposegmento':tiposegmento,
        'hitosuser':hitosuser
    }

    return render(request, 'miapp/index.html', context)


def TipoHitoView(request, tipobuscado):
    buscado = ''
    for x in tipohito:
        if tipobuscado == x[1]:
            buscado = x[0]
    hitosvigentes = Hito.objects.filter(tipo=buscado).filter(fecha_termino__gt=datetime.now())
    user = request.user
    hitosuser = Hito.objects.filter(fecha_termino__gt=datetime.now()).filter(segmento=user.userrol.rol)[:3]
    context = {
        'hitosvigentes':hitosvigentes,
        'tipohitos':tipohito,
        'tiposegmento':tiposegmento,
        'hitosuser':hitosuser
    }

    return render(request, 'miapp/index.html', context)

class HitoView(View):
    queryset = Hito.objects.all()
    serializer_class = HitoSerialiazer
    permission_classes = [IsAuthenticatedOrReadOnly]
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id >0):
            hitos =list (Hito.objects.filter(id=id).values())
            if len(hitos) > 0:
                hitos=hitos[0]
                datos = {'message': "Realizado", 'hitos': hitos}
            else:
                datos =  {'message': "Hito no encontrado"}  
            return JsonResponse(datos)
        else:
            hitos = list(Hito.objects.values())
            if len(hitos) > 0:
                datos = {'message': "Realizado", 'hitos': hitos}
            else:
                datos= {'message': "Hito no encontrado"}
            return JsonResponse(datos)
    def post(self, request):
        self.check_permissions(request, EsDeveloper)
        jd = json.loads(request.body)
        hito = Hito.objects.create(fecha_inicio= jd['fecha_inicio'],fecha_termino= jd['fecha_termino'],
                            todo_el_dia= jd['todo_el_dia'],descripcion= jd['descripcion'],tipo= jd['tipo'],
                            segmento= jd['segmento'],titulo= jd['titulo'])
        if hito.todo_el_dia:
            hito.fecha_termino = None
            hito.save()
        datos = {'message': "Realizado",'hito': model_to_dict(hito)}
        return JsonResponse(datos)
    
    def put(self, request, id):
        self.check_permissions(request, EsDeveloper)
        jd =json.loads(request.body)
        hitos =list (Hito.objects.filter(id=id).values())
        if len(hitos) > 0:
            hito = Hito.objects.get(id=id)
            hito.fecha_inicio=jd['fecha_inicio']
            hito.fecha_termino= jd['fecha_termino']
            hito.todo_el_dia= jd['todo_el_dia']
            hito.descripcion= jd['descripcion']
            hito.tipo= jd['tipo']
            hito.segmento= jd['segmento']
            hito.titulo= jd['titulo']
            hito.save()
            datos = {'message': "Realizado"}
        else:
            datos= {'message': "Hito no encontrado"}
        return JsonResponse(datos)
    
    def delete(self,request,id):
        self.check_permissions(request, EsDeveloper)
        hitos =list (Hito.objects.filter(id=id).values())
        if len(hitos) > 0:
            Hito.objects.filter(id=id).delete()
            datos = {'message': "Realizado"}
        else:
            datos= {'message': "Hito no encontrado"}
        return JsonResponse(datos)



class HitoAPI(generics.ListAPIView):
    queryset = Hito.objects.all()
    serializer_class = HitoSerialiazer

    def get_queryset(self):
        queryset = super().get_queryset()
        año = self.request.query_params.get('año', None)
        segmento = self.request.query_params.get('segmento', None)
        tipo = self.request.query_params.get('tipo', None)
        if año is not None:
            queryset = queryset.filter(fecha_inicio__year=año)
        if segmento is not None:
            queryset = queryset.filter(segmento=segmento)
        if tipo is not None:
            queryset = queryset.filter(tipo=tipo)
        return queryset

#http://localhost:8000/api/hitos/?año=2023&tipo=V&segmento=Co forma de filtrar por año,tipo y segmento
#Class que funciona con /docs/, sirve para ver como se implementan los elementos en la API, permite las acciones de GET,POST,PUT y DELETE, es mucho más
#arcaico que el sistema de thunder Client, los comandos de arriba fueron implementandos con ThunderClient en su totalidad
class HitoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Hito.objects.all()
    serializer_class = HitoSerialiazer