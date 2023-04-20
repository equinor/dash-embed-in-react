from dash import Dash, dcc, html, Input, Output
import webviz_core_components as wcc

app = Dash(__name__)

app.layout = html.Div(style={"backgroundColor": "rgb(200, 200, 200)"}, children=[
    wcc.WebvizEmbedDash(id="hei", eventName="webvizGlobalState"),
    html.Div(id="placeholder-global-state")
])


@app.callback(
    Output(component_id='placeholder-global-state', component_property='children'),
    Input(component_id='hei', component_property='value')
)
def update_output_div(input_value):
    return f'Hello from Dash and standard dash.html.Div: {input_value}'


if __name__ == '__main__':
    app.run_server(port=5000)
