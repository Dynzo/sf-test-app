import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello World'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
])

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
