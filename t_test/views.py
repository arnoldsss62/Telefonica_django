from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from t_test.models import Cmts,Nodo,Troba, Usuario, TareaProgramada,InfoCore,InfoPlanta, TareaNoc
from .forms import nuevaTareaForm, calendarioForm, clienteForm
from bootstrap_datepicker_plus import DateTimePickerInput,TimePickerInput
from django.views import generic
from django.db.models import DurationField, ExpressionWrapper, F



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
    if 'date' in request.GET:
        date = request.GET['date']
        print('Esta es la fecha')
        print (date)
        listatareas=TareaNoc.objects.filter(fechaInicio=date).annotate(duration=ExpressionWrapper(
                                           F('horaFin') - F('horaInicio'),
                                           output_field=DurationField()))
        print(listatareas[0].duration)
    else:
        date = 'You submitted nothing!'
    form=calendarioForm
    my_dict={'tarealist':listatareas, 'form':form}
    return  render(request,'calendario2.html',context=my_dict)


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
    if request.method == "POST":
        uploaded_file = request.FILES['upload']
        fs= FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render (request,'upload.html')

