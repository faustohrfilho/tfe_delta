from django.shortcuts import render
import numpy as np
from plotly.offline import plot
from plotly.graph_objs import Scatter

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
    if request.method == 'GET':
        context = {'params':[]}
        xd = np.linspace(0,6*np.pi,1000)
        yd = np.sin(xd)*220
        plot_div = plot([Scatter(x=xd, y=yd,
                    mode='lines', name='test',
                    opacity=0.8, marker_color='green')],
               output_type='div',
               include_plotlyjs=False)
        context['plot_div'] = plot_div
    else:
        context = {'params':[]}
#        context['params'].append({
#            'nome': 'Resistencia 1',
#            'valor': request.POST.get('resistor1'),
#            })
#        context['params'].append({
#            'nome': 'Resistencia 2',
#            'valor': request.POST.get('resistor2'),
#            })
#        context['params'].append({
#            'nome': 'Resistencia 3',
#            'valor': request.POST.get('resistor3'),
#            })
        context['params'].append({
            'nome': 'Tensao',
            'valor': request.POST.get('tensao'),
            })
#        context['params'].append({
#            'nome': 'Resistencia Total',
#            'valor': float(request.POST.get('resistor1')) + float(request.POST.get('resistor2')) + float(request.POST.get('resistor3')),
#            })

        tensao = float(request.POST.get('tensao'))
        xd = np.linspace(0,6*np.pi,1000)
        yd = np.sin(xd)*tensao
        plot_div = plot([Scatter(x=xd, y=yd,
                    mode='lines', name='test',
                    opacity=0.8, marker_color='green')],
               output_type='div',
               include_plotlyjs=False)
        context['plot_div'] = plot_div

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
