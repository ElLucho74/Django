from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("Hola Mundo Luis Castro en Django")