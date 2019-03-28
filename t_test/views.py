from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from t_test.models import Cmts,Nodo,Troba, Usuario, TareaProgramada,InfoCore,InfoPlanta, TareaNoc
from .forms import nuevaTareaForm, calendarioForm, clienteForm, listarForm
from bootstrap_datepicker_plus import DateTimePickerInput,TimePickerInput
from django.views import generic
from django.db.models import DurationField, ExpressionWrapper, F
from django.core.files.storage import FileSystemStorage
import os
import datetime as d

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCEL_DIR= os.path.join(BASE_DIR,'media/backup/')


# Create your views here.

def index (request):

    class NameForm(forms.Form):

        your_name = forms.CharField(label='Your name', max_length=100)
        name = forms.CharField(max_length=30)
        email = forms.EmailField(max_length=254)
        message = forms.CharField(
            max_length=2000,
            widget=forms.Textarea(),
            help_text='Write here your message!'
        )
        source = forms.CharField(       # A hidden input for internal use
            max_length=50,              # tell from which page the user sent the message
            widget=forms.HiddenInput()
        )

        #template = "your_template.html"
    #context = { "form" : NameForm() }
    tarea=TareaProgramada.objects.all().annotate(duration=ExpressionWrapper(
                                   F('horaFin') - F('horaInicio'),
                                   output_field=DurationField()))

    my_dict={'tarealista':tarea}
    #return HttpResponse("<b><u>Hello World</u></b>")
    return render(request,'index.html',context=my_dict)


def usuarios(request,id):


    listausuarios=Usuario.objects.filter(troba__trobaId=id)
    my_dict={'usuarioslist':listausuarios}
    return  render(request,'usuarios.html',context=my_dict)


def tareasnoc(request):


    listaTareas=TareaNoc.objects.order_by('fechaInicio').annotate(duration=ExpressionWrapper(
                                       F('horaFin') - F('horaInicio'),
                                       output_field=DurationField()))
    my_dict={'tarealist':listaTareas}
    return  render(request,'tareasnoc.html',context=my_dict)

def calendario(request):


    #listaTareas=TareaNoc.objects.order_by('fechaHoraInicio')
    form=calendarioForm
    listaTareas= {}
    my_dict={'form':form}
    return  render(request,'calendario2.html',context=my_dict)

def calendario_hfc(request):


    #listaTareas=TareaNoc.objects.order_by('fechaHoraInicio')
    form=calendarioForm
    listaTareas= {}
    my_dict={'form':form}
    return  render(request,'calendario_hfc.html',context=my_dict)

def addTarea(request):

    form = nuevaTareaForm

    if request.method=='POST':
        print('entro tu post')
        form=nuevaTareaForm(request.POST)


        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Informacion invalida')

    return render(request,'form.html',{'form':form})

def showTable(request):
    listaTareas={}
    if 'date' in request.GET:
        date = request.GET['date']
        print('Esta es la fecha')
        print (date)
        listatareas=TareaNoc.objects.filter(fechaInicio=date)
        print('aun no entra')
        if listatareas:
            print('Hay tareas')
            listaTareas=listatareas.annotate(duration=ExpressionWrapper(
                                               F('horaFin') - F('horaInicio'),
                                            output_field=DurationField()))
            print(listaTareas[0].duration)

    else:
        date = 'You submitted nothing!'
    form=calendarioForm
    my_dict={'tarealist':listaTareas, 'form':form}
    return  render(request,'calendario2.html',context=my_dict)

def showTable_hfc(request):
    listaTareas={}
    if 'date' in request.GET:
        date = request.GET['date']
        print('Esta es la fecha')
        print (date)
        listatareas=TareaProgramada.objects.filter(fecha=date)
        print('aun no entra')
        if listatareas:
            print('Hay tareas')
            listaTareas=listatareas.annotate(duration=ExpressionWrapper(
                                               F('horaFin') - F('horaInicio'),
                                            output_field=DurationField()))
            print(listaTareas[0].duration)

    else:
        date = 'You submitted nothing!'
    form=calendarioForm
    my_dict={'tarealist':listaTareas, 'form':form}
    return  render(request,'calendario_hfc.html',context=my_dict)


#Vista de buscar cliente para encontrar si el cliente tiene trabajaos programados que afectaron su servicio

def buscarClientes(request):

    #listaTareas=TareaNoc.objects.order_by('fechaHoraInicio')
    form=clienteForm

    listaTareas= {}
    my_dict={'form':form}
    return  render(request,'buscaCliente.html',context=my_dict)


def muestraClientes(request):
    listatareas={}
    if 'codigo' in request.GET:
        codigo = request.GET['codigo']
        print('Esta es el codigo de cliente')
        print (codigo)
        #Se esta asumiendo que el trabajo es de planta , hacer despues logica para core
        cliente= Usuario.objects.filter(codigoCliente=codigo)
        if cliente:

            listatareas=TareaProgramada.objects.filter(infoPlanta__troba=cliente[0].troba).annotate(duration=ExpressionWrapper(
                                           F('horaFin') - F('horaInicio'),
                                           output_field=DurationField()))


    else:
        date = 'You submitted nothing!'
    form=clienteForm
    my_dict={'tarealist':listatareas, 'form':form, 'cliente': cliente}

    return  render(request,'buscaCliente.html',context=my_dict)



def upload_file(request):
    if request.method == "POST" and ('upload' in request.FILES):
        uploaded_file = request.FILES['upload']
        fs= FileSystemStorage()
        print(EXCEL_DIR)
        if fs.exists('ExcelMovistar1.xlsx'):
                    fs.delete('ExcelMovistar1.xlsx')
        fs.save(EXCEL_DIR+uploaded_file.name,uploaded_file)
        fs.save('ExcelMovistar1.xlsx',uploaded_file)
        os.system('dataPLANTA.py')

    elif request.method == "POST" and ('upload_remd' in request.FILES):
        uploaded_file = request.FILES['upload_remd']
        fs= FileSystemStorage()
        print(EXCEL_DIR)
        if fs.exists('Remedy.xlsx'):
                    fs.delete('Remedy.xlsx')
        fs.save(EXCEL_DIR+uploaded_file.name,uploaded_file)
        fs.save('Remedy.xlsx',uploaded_file)
        os.system('dataCORE.py')
        ###EJECUTAR TU FUNCION ADRIAN
    return render (request,'upload.html')


#Listar usuarios afectados por trabajos programados en un lapso de tiempo

def listar_usuarios(request):


    #listaTareas=TareaNoc.objects.order_by('fechaHoraInicio')
    form=listarForm
    listaTareas= {}
    my_dict={'form':form}
    return  render(request,'lista_usuarios.html',context=my_dict)

##Tabla para mostrar usuarios

def showUsuarios(request):
    listaTareas={}
    if 'fechaInicio' and 'fechaFin'  in request.GET:
        fechaInicio = request.GET['fechaInicio']
        f1,f2,f3=fechaInicio.split('-')
        fechaFin=request.GET['fechaFin']
        fa,fb,fc=fechaFin.split('-')
        print(fechaInicio)
        if fechaFin > fechaInicio:
            listatareas=TareaProgramada.objects.filter(fecha__gte=d.date(int(f1),int(f2),int(f3)),fecha__lte=d.date(int(fa),int(fb),int(fc))).filter(area='Planta')
            if listatareas:
                print('Aqui estoy :)')
                print(listatareas)
                listaT=[]
                for u in listatareas:
                    print(u.infoPlanta.troba)
                    listaT=listaT+[u.infoPlanta.troba]
                querySet=Usuario.objects.filter(troba=listaT[0])
                for t in listaT[1:]:
                    querySet=querySet | Usuario.objects.filter(troba=t)

    else:
        fechaInicio = 'You submitted nothing!'
    form=listarForm
    my_dict={'listaUsuarios':querySet, 'form':form}
    return  render(request,'lista_usuarios.html',context=my_dict)




def report(request):
    return render(request,'reporte.html')



