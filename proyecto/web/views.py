from django.shortcuts import render, redirect, get_object_or_404
from .models import Auto, Cliente, Producto, ImagenAuto
from django.shortcuts import render
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm, AutoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
#para proteger urls
from django.contrib.auth.decorators import login_required, permission_required

def inicio(request):
    return render(request, 'web/index.html')
def Catalogo(request):
    autos = Auto.objects.order_by('marca')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(autos, 6)
        autos = paginator.page(page)
    except:
        raise Http404


    data = {
        'entity': autos,
        'paginator': paginator
    }
    
    return render(request, 'web/Catalogo.html', data)
def Noticias(request):
    return render(request, 'web/Noticias.html')
def car_detail(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    return render(request, 'web/car_detail.html', {'auto': auto})

@login_required
def Registro(request):
    data = {
        # creo una isntancia 
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Registro Enviado"
        else:
            data["form"] = formulario 
    return render(request, 'web/formulario.html', data)

@permission_required('web.add_auto')
def agregar_auto(request):

    data = {
        'form' : AutoForm()
    }

    if request.method == 'POST':
        formulario = AutoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Correctamente")
        else:
            data["form"] = formulario

    return render(request, 'web/Auto/agregar.html', data)

def listar_autos(request):
    auto = Auto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(auto, 8)
        auto = paginator.page(page)
    except:
        raise Http404


    data = {
        'entity': auto,
        'paginator': paginator
    }
    
    return render(request, 'web/Auto/listar.html', data)

def modificar_auto(request, id):

    auto = get_object_or_404(Auto, id=id)   

    data = {
        'form': AutoForm(instance=auto)
    }
    if request.method == 'POST':
        formulario = AutoForm(data=request.POST, instance=auto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar_autos")
        data['form'] = formulario


    return render(request, 'web/Auto/modificar.html', data)


def eliminar_auto(request, id):

    auto = get_object_or_404(Auto, id=id) 
    auto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_autos")

@permission_required('web.add_producto')
def agregar_producto(request):

    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Correctamente")
        else:
            data["form"] = formulario

    return render(request, 'web/Producto/agregar.html', data)



def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 8)
        productos = paginator.page(page)
    except:
        raise Http404


    data = {
        'entity': productos,
        'paginator': paginator
    }
    
    return render(request, 'web/Producto/listar.html', data)


def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)   

    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar_productos")
        data['form'] = formulario


    return render(request, 'web/Producto/modificar.html', data)


def eliminar_producto(request, id):

    producto = get_object_or_404(Producto, id=id) 
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_productos")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registrado con Exito!")
            return redirect(to="index")
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)


def Accesorios(request):
    productos = Producto.objects.all()
    return render(request, 'web/Accesorios.html', {'productos':productos})

def detalle_auto(request, auto_id):
    auto = get_object_or_404(Auto, id=auto_id)
    imagenes_auto = ImagenAuto.objects.filter(auto=auto)
    
    
    # Resto de la lógica para obtener los datos del auto y renderizar la plantilla de detalle del auto
    return render(request, 'web/detalle_auto.html', {'auto': auto, 'imagenes_auto': imagenes_auto})