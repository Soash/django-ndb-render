from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def custom_404_page(request, exception):
    return render(request, '404.html', status=404)
