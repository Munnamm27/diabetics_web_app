import dash
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
import style



p1='''
### Healthy Living

- Recipes & Nutrition
- Diet Plans
- Fitness
- Mental Health
- Medication & Treatment'''


dash.register_page(__name__)

page_list=[page['name'] for page in dash.page_registry.values()]
path_list=[page['path'] for page in dash.page_registry.values()]

layout = dbc.Row(
    [

        dbc.Col(
            [ 
                # html.H3("Healthy Living",className='text-center'),
                # html.Br(),
                dcc.Markdown(p1),

                # dcc.Link('Find Your Risk',path_list[2],style=style.hlink),
            ],md=4,style=style.para_style
        ),

    ],justify='center',
)