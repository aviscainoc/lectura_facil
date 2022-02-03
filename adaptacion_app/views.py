from django.shortcuts import render

# Create your views here.

def adaptador(request):
    texto_adaptado = ""
    if request.method == "POST":

        texto_orignal = request.POST['texto_orignal']


        texto_adaptado=texto_orignal 

    return render(request, "adaptacion_app/contact.html", {'texto_adaptado':texto_adaptado})

