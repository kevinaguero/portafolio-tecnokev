from django.shortcuts import render

def minijuegos_view(request):
    """Vista principal de minijuegos"""
    return render(request, 'minijuegos/minijuegos.html')
