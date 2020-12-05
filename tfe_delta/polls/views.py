from django.shortcuts import render
import numpy as np

# Create your views here.

def index(request):
    text = 'Pagina Inicial'
    a = np.linspace(5,15,3)
    context = {
        'text': text,
        'a':a,
    }
    return render(request,'polls/index.html',context)

def teoria_circuito(request):
    return render(request,'polls/teoria_circuito.html',{})

def simulacoes(request):
    #rodar o codigo do plotly
    context = {}
    return render(request,'polls/simulacoes.html',context)

def aplicacoes(request):
    return render(request,'polls/aplicacoes.html',{})

def sobre(request):
    faustim = {
        'nome': 'Fausto Humberto dos Reis Filho',
        'matricula': '11521EAU004',
    }
    gustavo = {
        'nome': 'Gustavo Pereira Marcos',
        'matricula': '11521EAU012',
    }
    valdemir = {
        'nome': 'Valdemir José de Queiroz Junior',
        'matricula': '11621EAU002',
    }
    lista_integrantes = [faustim,gustavo,valdemir]
    return render(request,'polls/sobre.html',{'lista_integrantes':lista_integrantes})
