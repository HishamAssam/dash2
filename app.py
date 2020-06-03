import os
from random import randint

import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#
myServer = flask.Flask(__name__)
myServer.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = dash.Dash(__name__, server=myServer)


app.layout = html.Div([
    dcc.Input(id='num1', value='0', type='number'),
    html.Div(id='out1'),    
])

@app.callback(
    Output(component_id='out1', component_property='children'),
    [Input(component_id='num1', component_property='value')]
)
def calc(val):
    if (val==None):
        return 0
    else:
        return int(val)*int(val)


# Run the Dash app
if __name__ == '__main__':
    app.myServer.run(debug=True, use_reloader=False)
