import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from create.models import Create


total = Create.objects.count()
date = Create.objects.filter('pub_date')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Total Favorite\'s Added',
        style={
            'textAlign': 'center',
            'color': colors['text'],

        }
    ),
dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [date], 'y': [total], 'type': 'bar', 'name': 'Total'},

            ],

'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }

            }
        }
    )
])