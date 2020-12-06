from django.shortcuts import render
import numpy as np
from plotly.offline import plot
from plotly.graph_objs import Scatter
from plotly.subplots import make_subplots
import plotly.graph_objects as go

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
        plot_div = '<div></div>'
        context['plot_div'] = plot_div
    else:
        context = {'params':[]}
        context['params'].append({
            'nome': 'Tensao',
            'valor': request.POST.get('tensao') + ' (V)',
            })
        context['params'].append({
            'nome': 'Resistores',
            'valor': request.POST.get('resistor') + ' (ohms)',
            })
        tensao = float(request.POST.get('tensao'))
        resistor = float(request.POST.get('resistor'))
        iab = tensao/resistor
        ibc = tensao/resistor
        ica = tensao/resistor

        xd = np.linspace(0,6,1000)
        xd_rad = np.linspace(0,6*np.pi*2,1000)
        yd = np.sin(xd_rad)*tensao

        x_iab = np.linspace(0,6,1000)
        x_iab_rad = np.linspace(0,6*np.pi*2,1000)
        y_iab = np.sin(x_iab_rad)*iab

        x_ibc = np.linspace(0,6,1000)
        x_ibc_rad = np.linspace(0,6*np.pi*2,1000)
        y_ibc = np.sin(x_ibc_rad+(2*np.pi/3))*ibc

        x_ica = np.linspace(0,6,1000)
        x_ica_rad = np.linspace(0,6*np.pi*2,1000)
        y_ica = np.sin(x_ica_rad+(4*np.pi/3))*ica

        # Create figure with secondary y-axis
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # Add traces
        fig.add_trace(
            go.Scatter(x=xd, y=yd, name="Tensao"),
            secondary_y=False,
        )

        fig.add_trace(
            go.Scatter(x=x_iab, y=y_iab, name="Iab"),
            secondary_y=True,
        )

        fig.add_trace(
            go.Scatter(x=x_ibc, y=y_ibc, name="Ibc"),
            secondary_y=True,
        )

        fig.add_trace(
            go.Scatter(x=x_ica, y=y_ica, name="Ica"),
            secondary_y=True,
        )

        # Add figure title
        fig.update_layout(
            title_text="Grafico do circuito trifásico ligação delta"
        )

        # Set x-axis title
        fig.update_xaxes(title_text="Periodo")

        plot_div = plot(fig,
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
