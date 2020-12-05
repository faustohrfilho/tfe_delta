from django.shortcuts import render

# Create your views here.

def index(request):
    text = 'Pagina Inicial'
    context = {
        'text': text,
    }
    return render(request,'polls/index.html',context)
