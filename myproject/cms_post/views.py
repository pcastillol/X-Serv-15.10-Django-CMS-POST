from django.shortcuts import render
from .models import Pages
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context

# Create your views here.




FORMULARIO = """
    <form action="" method="POST">
        ANIMATE A CREAR UNA NUEVA PAGINA:<br>
        Nombre: <input type="text" name="nombre" value="Real Madrid"><br>
        Pagina: <input type="text" name="pagina" value="12 Champions"><br>
        <input type="submit" value="Enviar">
    </form>
"""

def barra(request):
    if request.user.is_authenticated():
        logged = "Logged in as " + request.user.username + ". <a href='/logout'>Logout</a>"
    else:
        logged = "Not logged in. <a href='/login'>Login</a>"

    pages = Pages.objects.all()
    respuesta = "<br><br><h1>Bienvenido a tu CMS.</h1>"

    if len(pages)==0:
        respuesta += "Aún no hay contenidos almacenados.<br>"
    else:
        respuesta += "Estos son los contenidos almacenados:<br>"

    respuesta += "<ul>"
    for page in pages:
        respuesta += "<li><a href='/content/" + str(page.id) + "'>" + page.name + "</a>"
    respuesta += "</ul>"

    return HttpResponse(logged + respuesta)

@csrf_exempt
def content(request, num):
    if request.method == "POST":
        pagina = Pages(name = request.POST['nombre'], page = request.POST['pagina'])
        pagina.save()
        return HttpResponseRedirect("/content/" + str(pagina.id))
    try:
        pagina = Pages.objects.get(id=int(num))
    except Pages.DoesNotExist:
        respuesta = "No existe"
        if request.user.is_authenticated():
            respuesta += "<br><br>" + FORMULARIO
        return HttpResponseNotFound(respuesta)

    respuesta = "Id: " + str(pagina.id) + "<br>"
    respuesta += "Nombre: " + pagina.name + "<br>"
    respuesta += "Pagina: " + pagina.page + "<br>"

    if request.user.is_authenticated():
        respuesta += "<br><br>" + FORMULARIO
    return HttpResponse(respuesta)

def annotated_barra(request):
    if request.user.is_authenticated():
        logged = "Logged in as " + request.user.username + ". <a href='/logout'>Logout</a>"
    else:
        logged = "Not logged in. <a href='/login'>Login</a>"

    pages = Pages.objects.all()
    respuesta = "<br><br><h1>Bienvenido al CMS mas futbolero.</h1>"

    if len(pages)==0:
        respuesta += "Aún no hay contenidos almacenados.<br>"
    else:
        respuesta += "Estos son los contenidos almacenados:<br>"

    respuesta += "<ul>"
    for page in pages:
        respuesta += "<li><a href='/annotated/content/" + str(page.id) + "'>" + page.name + "</a>"
    respuesta += "</ul>"

    template = get_template('Summer_Breeze/index.html')
    c = Context({
        'title': "FutCMS",
        'cabecera':"DJANGO FutCMS",
        'content': respuesta + logged,
    })

    return HttpResponse(template.render(c))

@csrf_exempt
def annotated_content(request, num):
    if request.method == "POST":
        pagina = Pages(name = request.POST['nombre'], page = request.POST['pagina'])
        pagina.save()
        return HttpResponseRedirect("/annotated/content/" + str(pagina.id))
    try:
        pagina = Pages.objects.get(id=int(num))
    except Pages.DoesNotExist:
        respuesta = "No existe"
        if request.user.is_authenticated():
            respuesta += "<br><br>" + FORMULARIO
        return HttpResponseNotFound(respuesta)

    respuesta = "Id: " + str(pagina.id) + "<br>"
    respuesta += "Nombre: " + pagina.name + "<br>"
    respuesta += "Pagina: " + pagina.page + "<br>"

    if request.user.is_authenticated():
        respuesta += "<br><br>" + FORMULARIO

    template = get_template('Summer_Breeze/index.html')
    c = Context({
        'title': "FutCMS",
        'cabecera':"DJANGO FutCM",
        'content': respuesta,
    })

    return HttpResponse(template.render(c))

def edit(contenido_pag):
    form_edit = '<form action="" method="POST">'
    form_edit += 'EDITA ESTA PAGINA:<br>'
    form_edit += 'Pagina: <input type="text" name="pagina_editada" value="' + str(contenido_pag) + '"<br>'
    form_edit += '<input type="submit" value="Enviar">'
    form_edit += '</form>'

    return form_edit


@csrf_exempt
def edit_content(request, num):
    if request.method == "GET":
        if request.user.is_authenticated():
            logged = "Logged in as " + request.user.username + ". <a href='/logout'>Logout</a>"

            try:
                pagina = Pages.objects.get(id=int(num))
            except Pages.DoesNotExist:
                respuesta = "No existe"
                respuesta += "<br><br>" + FORMULARIO
                return HttpResponseNotFound(respuesta)

            respuesta = logged + "<br><br>"
            respuesta += "Id: " + str(pagina.id) + "<br>"
            respuesta += "Nombre: " + pagina.name + "<br>"
            respuesta += "Pagina: " + pagina.page + "<br>"
            respuesta += "<br><br>" + FORMULARIO

            formulario_editar = edit(pagina.page)

            respuesta += "<br><br>" + formulario_editar

            return HttpResponse(respuesta)

        else:
            logged = "Not logged in. <a href='/login'>Login</a>"
            respuesta = "Lo siento, no estas logueado, asi que no puedes editar."
            respuesta += "<br><br>" + logged

            return HttpResponse(respuesta)

    elif request.method == "POST":
        if request.user.is_authenticated():

            try:
                pagina = Pages.objects.get(id=int(num))
            except Pages.DoesNotExist:
                respuesta = "No existe"
                respuesta += "<br><br>" + FORMULARIO
                return HttpResponseNotFound(respuesta)

            pagina.page = request.POST['pagina_editada']
            # pagina = Pages(name = , page = request.POST['pagina_editada'])
            pagina.save()

            return HttpResponseRedirect("/edit/content/" + str(num))

        else:
            logged = "Not logged in. <a href='/login'>Login</a>"
            respuesta = "Lo siento, no estas logueado, asi que no puedes editar."
            respuesta += "<br><br>" + logged

            return HttpResponse(respuesta)


@csrf_exempt
def edit_annotated_content(request, num):
    if request.method == "GET":
        if request.user.is_authenticated():
            logged = "Logged in as " + request.user.username + ". <a href='/logout'>Logout</a>"

            try:
                pagina = Pages.objects.get(id=int(num))
            except Pages.DoesNotExist:
                respuesta = "No existe"
                respuesta += "<br><br>" + FORMULARIO
                return HttpResponseNotFound(respuesta)

            respuesta = logged + "<br><br>"
            respuesta += "Id: " + str(pagina.id) + "<br>"
            respuesta += "Nombre: " + pagina.name + "<br>"
            respuesta += "Pagina: " + pagina.page + "<br>"
            respuesta += "<br><br>" + FORMULARIO

            formulario_editar = edit(pagina.page)

            respuesta += "<br><br>" + formulario_editar

            template = get_template('Summer_Breeze/index.html')
            c = Context({
                'title': "FutCMS",
                'cabecera':"DJANGO FutCMS",
                'content': respuesta,
            })

            return HttpResponse(template.render(c))

        else:
            logged = "Not logged in. <a href='/login'>Login</a>"
            respuesta = "Lo siento, no estas logueado, asi que no puedes editar."
            respuesta += "<br><br>" + logged

            return HttpResponse(respuesta)

    elif request.method == "POST":
        if request.user.is_authenticated():

            try:
                pagina = Pages.objects.get(id=int(num))
            except Pages.DoesNotExist:
                respuesta = "No existe"
                respuesta += "<br><br>" + FORMULARIO
                return HttpResponseNotFound(respuesta)

            pagina.page = request.POST['pagina_editada']
            # pagina = Pages(name = , page = request.POST['pagina_editada'])
            pagina.save()

            return HttpResponseRedirect("/edit/annotated/content/" + str(num))

        else:
            logged = "Not logged in. <a href='/login'>Login</a>"
            respuesta = "Lo siento, no estas logueado, asi que no puedes editar."
            respuesta += "<br><br>" + logged

            return HttpResponse(respuesta)
