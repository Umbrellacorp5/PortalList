from django.shortcuts import render, redirect
from django.db import connection
from django.db import connections
from profesores.forms import IngresarProfesor
from profesores.models import Materia, Lista, Profesor
from administracion.models import Usuario, Grupo, Pasan
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from json import dumps
import json

'''
ingresa profesor:
    -envia codigo
    seleccionLista:
        -muestra los grupos
            -grupos del profesor:
            -pasan saca codGrupo usando codProfesor
            -enviar json con grupos
            -ve la lista

Funcionalidades: 

    -LogIn, nombreUsuario + contraseña
    -LogOut

    -Elegir Grupo
        -nombre Grupo + Materia

    -Ver Lista
        -Lista de alumnos
'''

#copy and delete
def send_dictionary(request):
    # create data dictionary
    dataDictionary = {
        'hello': 'World',
        'geeks': 'forgeeks',
        'ABC': 123,
        456: 'abc',
        14000605: 1,
        'list': ['geeks', 4, 'geeks'],
        'dictionary': {'you': 'can', 'send': 'anything', 3: 1}
    }
    # dump data
    dataJSON = dumps(dataDictionary)
    return render(request, 'landing.html', {'data': dataJSON})




def ingresarProfesor(request):
   IP = IngresarProfesor(request.POST)
   if request.method == "POST":
        IP.inputUsuarioIP = request.POST.get('inputUsuarioIP')
        IP.inputContraseñaIP = request.POST.get('inputContraseñaIP')
        for u in Usuario.objects.raw('SELECT usuario, cedula, contraseña FROM administracion_usuario WHERE usuario = %s and contraseña = %s',[IP.inputUsuarioIP, IP.inputContraseñaIP]):
            global profesorCI
            profesorCI= u.cedula
        if IP.inputUsuarioIP == u.usuario and  IP.inputContraseñaIP == u.contraseña:
                return redirect('../seleccionLista/')
   return render(request,'ingresarProfesor.html')





def seleccionLista(request):
    if request.method == 'GET':
        
        for p in Profesor.objects.raw('Select codProfesor FROM profesores_profesor WHERE usuarioci_id=%s', [profesorCI]):
            codProfesor = p.codProfesor
        for m in Materia.objects.raw('Select codMateria, nombre FROM profesores_materia WHERE cod_profesor_id = %s',[codProfesor]):
            nombreMateria = m.nombre
        for g in Pasan.objects.raw('SELECT codGrupo_id, id FROM administracion_pasan WHERE codProfesor_id = %s',[codProfesor]):
            grupo = g.codGrupo_id
        for ng in Grupo.objects.raw('SELECT nombre, codGrupo FROM administracion_grupo WHERE codGrupo = %s',[grupo]):
            gruposProfesor = ng.nombre
    
        
        dataDictionary = {
            'NombreMateria': nombreMateria,
            'NombreGrupo': gruposProfesor,
        }
        dataGrupoJSON = dumps(dataDictionary) 
        print(dataGrupoJSON)
        
        return render(request, 'seleccionLista.html',{'datajs': dataGrupoJSON})

'''
def listaElegida(request):
    if request.method == 'POST':
        return render(request, 'seleccionLista.html',{'datajs': dataGrupoJSON})
'''




def lista(request):
    if request.method == 'GET':
        '''
        Checkboxes work a little bit different from other form inputs, so if you examine a post 
        sent from a form that includes a checkbox, there are two possibilities...

        <input type="checkbox" name="cb1"/>
        if the checlbox is checked, your queryset will look like:
            queryset = {'cb1' : 'on'}
        if it is not checked:
            queryset = {}
        So, you have to check the existence of the related form element name:
        if 'cb1' in queryset:
            "item is selected"
        else:
            "item is not selected"
        '''
        #if 'cedula' in queryset:
        #
        return render(request, 'lista.html')