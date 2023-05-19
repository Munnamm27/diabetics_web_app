import dash
from dash import html,dcc,Input,Output,State
import dash_bootstrap_components as dbc
import style

app = dash.Dash(
    __name__, use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)

server=app.server

page_list=[page['name'] for page in dash.page_registry.values()]
path_list=[page['path'] for page in dash.page_registry.values()]

# print(path_list)

header=dbc.Row( 
    [ 
        dbc.Col([
        html.H2("DIABETES",className='text-center'),
        html.H6("Know It to Fight It",className='text-center'),],md=12,style=style.dropdowns_style),

        html.Div([
            dcc.Link(page_list[0],href='/',style=style.hlink_home),
            dcc.Link("Test Your Risk",href='/test-your-risk',style=style.hlink),
            dcc.Link("Know Diabetes",href='/know',style=style.hlink),
            dcc.Link("Healthy Living",href='/healthy-living',style=style.hlink),
            dcc.Link("Tools & Support",href='/tools',style=style.hlink),
            dcc.Link("About",href='/about',style=style.hlink),

        ],className='text-center'),

        html.Br(),
        html.Br(),
        dcc.Markdown("-----------------"),
        dash.page_container
        
    ], align='center',justify='center'
)


app.layout=dbc.Container( 
    [ 
        header,
        
    ],
    fluid=True,
        style={'border': '1px solid black',    "border-radius": "10px", 'background': 'radial-gradient(circle, #FDF5E6, #E0FFFF)',
           "box-shadow": "0 2px 5px rgba(0, 0, 0, 0.3)",'height':'820px' }
)

if __name__ == "__main__":
    app.run_server(debug=True,host='0.0.0.0', port=9000)