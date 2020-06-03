import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Setup the app
# Make sure not to change this file name or the variable names below,
# the template is configured to execute 'server' on 'app.py'
server = flask.Flask("main")
app = dash.Dash("main", server=server)





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
app.server.run(debug=True, use_reloader=False)
