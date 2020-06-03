import flask
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#
myServer = flask.Flask(__name__)
app = dash.Dash(__name__, server=myServer)

tips= px.data.tips().head(100)
fig = px.scatter(tips, x="total_bill", y="tip")

app.layout = html.Div([
  dcc.RadioItems(id="gender1", options=[{'label': 'Female', 'value': 'Female'},{'label': 'Male', 'value': 'Male'}], value='Female'),
  dcc.Graph(id="fig1", figure=fig)])

@app.callback(Output('fig1', 'figure'),[Input('gender1', 'value')])
def updateGender(g):
    return  px.scatter(tips.query("sex=='"+g+"'"), x="total_bill", y="tip")
app.run_server(debug=True, use_reloader=False)


# Run the Dash app
if __name__ == '__main__':
    app.myServer.run(debug=True, use_reloader=False)
