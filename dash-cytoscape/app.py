import pandas as pd

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import dash_cytoscape as cyto

app = dash.Dash(__name__)
server = app.server

# prepare data
edges = pd.DataFrame.from_dict({'from':['earthquake', 'earthquake', 'burglary', 'alarm', 'alarm'],
                               'to': ['report', 'alarm', 'alarm','John Calls', 'Mary Calls']})
nodes = set()

cy_edges = []
cy_nodes = []

for index, row in edges.iterrows():
    source, target = row['from'], row['to']

    if source not in nodes:
        nodes.add(source)
        cy_nodes.append({"data": {"id": source, "label": source}})
    if target not in nodes:
        nodes.add(target)
        cy_nodes.append({"data": {"id": target, "label": target}})

    cy_edges.append({
        'data': {
            'source': source,
            'target': target
        }
    })

# define stylesheet
stylesheet = [
    {
        "selector": 'node', # すべてのnodeに対して
        'style': {
            "opacity": 0.9,
            "label": "data(label)", # 表示させるnodeのラベル
            "background-color": "#07ABA0", # nodeの色
            "color": "#008B80" # nodeのラベルの色
        }
    },
    {
        "selector": 'edge', # すべてのedgeに対して
        "style": {
            "target-arrow-color": "#C5D3E2", # 矢印の色
            "target-arrow-shape": "triangle", # 矢印の形
            "line-color": "#C5D3E2", # edgeのcolor
            'arrow-scale': 2, # 矢印のサイズ
            'curve-style': 'bezier' # デフォルトのcurve-styleだと矢印が表示されないため指定する
    }
}]

# define layout
app.layout = html.Div([
    dcc.Dropdown(
            id='dropdown-layout',
            options=[
                {'label': 'random',
                 'value': 'random'},
                {'label': 'grid',
                 'value': 'grid'},
                {'label': 'circle',
                 'value': 'circle'},
                {'label': 'concentric',
                 'value': 'concentric'},
                {'label': 'breadthfirst',
                 'value': 'breadthfirst'},
                {'label': 'cose',
                 'value': 'cose'}
            ], value='grid'
        ),
    html.Div(children=[
        cyto.Cytoscape(
            id='cytoscape',
            elements=cy_edges + cy_nodes,
            style={
                'height': '95vh',
                'width': '100%'
            },
            stylesheet=stylesheet
        )
    ])
])

@app.callback(Output('cytoscape', 'layout'),
              [Input('dropdown-layout', 'value')])
def update_cytoscape_layout(layout):
    return {'name': layout}

if __name__ == '__main__':
    app.run_server(debug=False)

