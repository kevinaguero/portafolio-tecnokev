from django.shortcuts import render

# Create your views here.
def proyectos_view(request):

    return render(request, 'proyectos/proyectos.html')