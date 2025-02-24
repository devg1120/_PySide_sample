import pandas as pd

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

import dash_cytoscape as cyto
import json

## https://github.com/cytoscape/cytoscape.js-cose-bilkent
cose_bilkent_defaultOptions = {
  # Called on `layoutready`
  "ready":  "function () {console(\"rady!!!\"}",
  # Called on `layoutstop`
  "stop": None,
  # 'draft', 'default' or 'proof" 
  # - 'draft' fast cooling rate 
  # - 'default' moderate cooling rate 
  # - "proof" slow cooling rate
  "quality": 'default',
  # Whether to include labels in node dimensions. Useful for avoiding label overlap
  "nodeDimensionsIncludeLabels": False,
  # number of ticks per frame; higher is faster but more jerky
  "refresh": 30,
  # Whether to fit the network view after when done
  "fit": True,
  # Padding on fit
  "padding": 10,
  # Whether to enable incremental mode
  "randomize": True,
  # Node repulsion (non overlapping) multiplier
  "nodeRepulsion": 4500,
  # Ideal (intra-graph) edge length
  "idealEdgeLength": 50,
  # Divisor to compute edge forces
  "edgeElasticity": 0.45,
  # Nesting factor (multiplier) to compute ideal edge length for inter-graph edges
  "nestingFactor": 0.1,
  # Gravity force (constant)
  "gravity": 0.25,
  # Maximum number of iterations to perform
  "numIter": 2500,
  # Whether to tile disconnected nodes
  "tile": True,
  # Type of layout animation. The option set is {'during', 'end', false}
  "animate": 'end',
  # Duration for animate:end
  "animationDuration": 500,
  # Amount of vertical space to put between degree zero nodes during tiling (can also be a function)
  "tilingPaddingVertical": 10,
  # Amount of horizontal space to put between degree zero nodes during tiling (can also be a function)
  "tilingPaddingHorizontal": 10,
  # Gravity range (constant) for compounds
  "gravityRangeCompound": 1.5,
  # Gravity force (constant) for compounds
  "gravityCompound": 1.0,
  # Gravity range (constant)
  "gravityRange": 3.8,
  # Initial cooling factor for incremental layout
  "initialEnergyOnIncremental": 0.5
}

cyto.load_extra_layouts()

app = dash.Dash(__name__)
server = app.server

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}
# prepare data
"""
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
"""

## Elements JSON
## https://js.cytoscape.org/#selectors/group-class-amp-id
_elements = [{ 'group':'nodes','data':{ 'id': 'n0' ,'label' :'n0'  }},
            { 'group':'nodes', 'data':{ 'id': 'n1' ,'label': 'n1'  }},
            { 'group':'nodes', 'data':{ 'id': 'n2' ,'label': 'n2'  }},
            { 'group':'nodes', 'data':{ 'id': 'n3' ,'label': 'n3'  }},
            { 'group':'nodes', 'data':{ 'id': 'n4' ,'label': 'n4'  , 'parent': 'n37'}},
            { 'group':'nodes', 'data':{ 'id': 'n5' ,'label': 'n5'  }},
            { 'group':'nodes', 'data':{ 'id': 'n6' ,'label': 'n6'  }},
            { 'group':'nodes', 'data':{ 'id': 'n7' ,'label': 'n7'  , 'parent': 'n37'}},
            { 'group':'nodes', 'data':{ 'id': 'n8' ,'label': 'n8'  , 'parent': 'n37'}},
            { 'group':'nodes', 'data':{ 'id': 'n9' ,'label': 'n9'  , 'parent': 'n37'}},
            { 'group':'nodes', 'data':{ 'id': 'n10','label': 'n10' , 'parent': 'n38'}},
            { 'group':'nodes', 'data':{ 'id': 'n12','label': 'n12' }},
            { 'group':'nodes', 'data':{ 'id': 'n13','label': 'n13' }},
            { 'group':'nodes', 'data':{ 'id': 'n14','label': 'n14' }},
            { 'group':'nodes', 'data':{ 'id': 'n15','label': 'n15' }},
            { 'group':'nodes', 'data':{ 'id': 'n16','label': 'n16' }},
            { 'group':'nodes', 'data':{ 'id': 'n17','label': 'n17' }},
            { 'group':'nodes', 'data':{ 'id': 'n18','label': 'n18' }},
            { 'group':'nodes', 'data':{ 'id': 'n19','label': 'n19' }},
            { 'group':'nodes', 'data':{ 'id': 'n20','label': 'n20' }},
            { 'group':'nodes', 'data':{ 'id': 'n21','label': 'n21' }},
            { 'group':'nodes', 'data':{ 'id': 'n22','label': 'n22' }},
            { 'group':'nodes', 'data':{ 'id': 'n23','label': 'n23' }},
            { 'group':'nodes', 'data':{ 'id': 'n24','label': 'n24' , 'parent': 'n39'}},
            { 'group':'nodes', 'data':{ 'id': 'n25','label': 'n25' , 'parent': 'n39'}},
            { 'group':'nodes', 'data':{ 'id': 'n26','label': 'n26' , 'parent': 'n42'}},
            { 'group':'nodes', 'data':{ 'id': 'n27','label': 'n27' , 'parent': 'n42'}},
            { 'group':'nodes', 'data':{ 'id': 'n28','label': 'n28' , 'parent': 'n42'}},
            { 'group':'nodes', 'data':{ 'id': 'n29','label': 'n29' , 'parent': 'n40'}},
            { 'group':'nodes', 'data':{ 'id': 'n31','label': 'n31' , 'parent': 'n41'}},
            { 'group':'nodes', 'data':{ 'id': 'n32','label': 'n32' , 'parent': 'n41'}},
            { 'group':'nodes', 'data':{ 'id': 'n33','label': 'n33' , 'parent': 'n41'}},
            { 'group':'nodes', 'data':{ 'id': 'n34','label': 'n34' , 'parent': 'n41'}},
            { 'group':'nodes', 'data':{ 'id': 'n35','label': 'n35' , 'parent': 'n41'}},
            { 'group':'nodes', 'data':{ 'id': 'n36','label': 'n36' , 'parent': 'n41'}},
            { 'group':'nodes', 'data':{ 'id': 'n37','label': 'n37' }},
            { 'group':'nodes', 'data':{ 'id': 'n38','label': 'n38' }},
            { 'group':'nodes', 'data':{ 'id': 'n39','label': 'n39' , 'parent': 'n43'}},
            { 'group':'nodes', 'data':{ 'id': 'n40','label': 'n40' , 'parent': 'n42'}},
            { 'group':'nodes', 'data':{ 'id': 'n41','label': 'n41' , 'parent': 'n42'}},
            { 'group':'nodes', 'data':{ 'id': 'n42','label': 'n42' , 'parent': 'n43'}},
            { 'group':'nodes', 'data':{ 'id': 'n43','label': 'n43' },'classes': ['classtest']},
            { 'group':'edges', 'data':{ 'id': 'e0', 'source': 'n0', 'target': 'n1'} },
            { 'group':'edges', 'data':{ 'id': 'e1', 'source': 'n1', 'target': 'n2'} },
            { 'group':'edges', 'data':{ 'id': 'e2', 'source': 'n2', 'target': 'n3'} },
            { 'group':'edges', 'data':{ 'id': 'e3', 'source': 'n0', 'target': 'n3'} },
            { 'group':'edges', 'data':{ 'id': 'e4', 'source': 'n1', 'target': 'n4'} },
            { 'group':'edges', 'data':{ 'id': 'e5', 'source': 'n2', 'target': 'n4'} },
            { 'group':'edges', 'data':{ 'id': 'e6', 'source': 'n4', 'target': 'n5'} },
            { 'group':'edges', 'data':{ 'id': 'e7', 'source': 'n5', 'target': 'n6'} },
            { 'group':'edges', 'data':{ 'id': 'e8', 'source': 'n4', 'target': 'n6'} },
            { 'group':'edges', 'data':{ 'id': 'e9', 'source': 'n4', 'target': 'n7'} },
            { 'group':'edges', 'data':{ 'id': 'e10', 'source': 'n7', 'target': 'n8'} },
            { 'group':'edges', 'data':{ 'id': 'e11', 'source': 'n8', 'target': 'n9'} },
            { 'group':'edges', 'data':{ 'id': 'e12', 'source': 'n7', 'target': 'n9'} },
            { 'group':'edges', 'data':{ 'id': 'e13', 'source': 'n13', 'target': 'n14'} },
            { 'group':'edges', 'data':{ 'id': 'e14', 'source': 'n12', 'target': 'n14'} },
            { 'group':'edges', 'data':{ 'id': 'e15', 'source': 'n14', 'target': 'n15'} },
            { 'group':'edges', 'data':{ 'id': 'e16', 'source': 'n14', 'target': 'n16'} },
            { 'group':'edges', 'data':{ 'id': 'e17', 'source': 'n15', 'target': 'n17'} },
            { 'group':'edges', 'data':{ 'id': 'e18', 'source': 'n17', 'target': 'n18'} },
            { 'group':'edges', 'data':{ 'id': 'e19', 'source': 'n18', 'target': 'n19'} },
            { 'group':'edges', 'data':{ 'id': 'e20', 'source': 'n17', 'target': 'n20'} },
            { 'group':'edges', 'data':{ 'id': 'e21', 'source': 'n19', 'target': 'n20'} },
            { 'group':'edges', 'data':{ 'id': 'e22', 'source': 'n16', 'target': 'n20'} },
            { 'group':'edges', 'data':{ 'id': 'e23', 'source': 'n20', 'target': 'n21'} },
            { 'group':'edges', 'data':{ 'id': 'e25', 'source': 'n23', 'target': 'n24'} },
            { 'group':'edges', 'data':{ 'id': 'e26', 'source': 'n24', 'target': 'n25'} },
            { 'group':'edges', 'data':{ 'id': 'e27', 'source': 'n26', 'target': 'n38'} },
            { 'group':'edges', 'data':{ 'id': 'e29', 'source': 'n26', 'target': 'n39'} },
            { 'group':'edges', 'data':{ 'id': 'e30', 'source': 'n26', 'target': 'n27'} },
            { 'group':'edges', 'data':{ 'id': 'e31', 'source': 'n26', 'target': 'n28'} },
            { 'group':'edges', 'data':{ 'id': 'e33', 'source': 'n21', 'target': 'n31'} },
            { 'group':'edges', 'data':{ 'id': 'e35', 'source': 'n31', 'target': 'n33'} },
            { 'group':'edges', 'data':{ 'id': 'e36', 'source': 'n31', 'target': 'n34'} },
            { 'group':'edges', 'data':{ 'id': 'e37', 'source': 'n33', 'target': 'n34'} },
            { 'group':'edges', 'data':{ 'id': 'e38', 'source': 'n32', 'target': 'n35'} },
            { 'group':'edges', 'data':{ 'id': 'e39', 'source': 'n32', 'target': 'n36'} },
            { 'group':'edges', 'data':{ 'id': 'e40', 'source': 'n16', 'target': 'n40'} }
           ]


# define stylesheet
stylesheet = [
    {
        "selector": 'node', # すべてのnodeに対して
        'style': {
            "opacity": 0.9,
            "label": "data(label)", # 表示させるnodeのラベル
            "background-opacity": 0.333,
            "background-color": "#07ABA0", # nodeの色
            #"background-color": "red", # nodeの色
            "color": "#008B80" # nodeのラベルの色
        }
    },
    {
        "selector": '#n1', # すべてのnodeに対して
        'style': {
            "opacity": 0.9,
            "label": "data(label)", # 表示させるnodeのラベル
            #"background-color": "#07ABA0", # nodeの色
            "background-color": "red", # nodeの色
            "color": "#008B80" # nodeのラベルの色
        }
    },
    
    {
        "selector": '.classtest', # 
        'style': {
            "background-opacity": 0.333,
            #"background-color": "#07ABA0", # nodeの色
            "background-color": "yellow", # nodeの色
        }
    },
   
    {
        "selector": 'edge', # すべてのedgeに対して
        "style": {
            "target-arrow-color": "#C5D3E2", # 矢印の色
            "target-arrow-shape": "triangle", # 矢印の形
            "line-color": "#C5D3E2", # edgeのcolor
            #"line-color": "#000000", # edgeのcolor
            'arrow-scale': 2, # 矢印のサイズ
            'curve-style': 'bezier' # デフォルトのcurve-styleだと矢印が表示されないため指定する
    }
}]

# define layout
"""
https://dash.plotly.com/cytoscape/layout
 cose-bilkent
 cola
 euler
 spread
 dagre
 klay
"""
cyt_data = cyto.Cytoscape(
            id='cytoscape',
            #elements=cy_edges + cy_nodes,
            elements=_elements,
            #layout={'name': 'cose-bilkent'},
            layout={'name': 'cose-bilkent', 'options': cose_bilkent_defaultOptions},
            style={
                'height': '95vh',
                'width': '100%'
            },
            stylesheet=stylesheet
        )

#c = cyto.utils.Tree.get_nodes(_elements)

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
                 'value': 'cose'},
                {'label': 'cose-bilkent',
                 'value': 'cose-bilkent'},
                {'label': 'cola',
                 'value': 'cola'},
                {'label': 'euler',
                 'value': 'euler'},
                {'label': 'spread',
                 'value': 'spread'},
                {'label': 'dagre',
                 'value': 'dagre'},
                {'label': 'klay',
                 'value': 'klay'}
            ], value='cose-bilkent'
        ),
    ## https://dash.plotly.com/cytoscape/elements
    ##
    html.Div(children=[
        cyt_data
        #cyto.Cytoscape(
        #    id='cytoscape',
        #    #elements=cy_edges + cy_nodes,
        #    elements=_elements,
        #    #layout={'name': 'cose-bilkent'},
        #    layout={'name': 'cose-bilkent', 'options': cose_bilkent_defaultOptions},
        #    style={
        #        'height': '95vh',
        #        'width': '100%'
        #    },
        #    stylesheet=stylesheet
        #)
        ,
     html.Pre(id='cytoscape-tapNodeData-json', style=styles['pre']),
     html.Button("Print elements JSONified", id="button-cytoscape"),
     html.Div(id="html-cytoscape"),
     #html.P(id='cytoscape-tapNodeData-output'),
     #html.P(id='cytoscape-tapEdgeData-output'),
     #html.P(id='cytoscape-mouseoverNodeData-output'),
     #html.P(id='cytoscape-mouseoverEdgeData-output')
    ])
])


@app.callback(Output('cytoscape', 'layout'),
              [Input('dropdown-layout', 'value')])
def update_cytoscape_layout(layout):
    return {'name': layout}


@app.callback(Output('cytoscape-tapNodeData-json', 'children'),
              Input('cytoscape', 'tapNodeData'))
def displayTapNodeData(data):
    print("displayTapNodeData...")
    print(json.dumps(data, indent=2))

    return json.dumps(data, indent=2)

@app.callback(
    Output("html-cytoscape", "children"),
    [Input("button-cytoscape", "n_clicks")],
    [State("cytoscape", "elements")],
)
def testCytoscape(n_clicks, elements):
    if n_clicks:
        return json.dumps(elements)

"""
@app.callback(Output('cytoscape-tapNodeData-output', 'children'),
              Input('cytoscape', 'tapNodeData'))
def displayTapNodeData(data):
    if data:
        return "You recently clicked/tapped the city: " + data['label']


@app.callback(Output('cytoscape-tapEdgeData-output', 'children'),
              Input('cytoscape', 'tapEdgeData'))
def displayTapEdgeData(data):
    if data:
        return "You recently clicked/tapped the edge between " + \
               data['source'].upper() + " and " + data['target'].upper()


@app.callback(Output('cytoscape-mouseoverNodeData-output', 'children'),
              Input('cytoscape', 'mouseoverNodeData'))
def displayTapNodeData(data):
    if data:
        return "You recently hovered over the city: " + data['label']


@app.callback(Output('cytoscape-mouseoverEdgeData-output', 'children'),
              Input('cytoscape', 'mouseoverEdgeData'))
def displayTapEdgeData(data):
    if data:
        return "You recently hovered over the edge between " + \
               data['source'].upper() + " and " + data['target'].upper()

"""

if __name__ == '__main__':
    app.run_server(debug=False)

