import dash
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
import style


paragraph='''Finding out your risk of type 2 diabetes only takes a few minutes. It could be the most important thing you do today.

'''

paragraph1='''To calculate your risk we will ask you for some personal data. These data in the context relates to your health. This information will be stored in such a way that it can not identify you. All information provided will only be used for testing diabetes.
'''

dash.register_page(__name__)

page_list=[page['name'] for page in dash.page_registry.values()]
path_list=[page['path'] for page in dash.page_registry.values()]

layout = dbc.Row(
    [

        dbc.Col(
            [ 
                html.H3("Test Your Risk",className='text-center'),
                html.Br(),

                html.P(paragraph),
                html.P(paragraph1),
                dcc.Link('Find Your Risk','/risk-calculation',style=style.hlink),
            ],md=4,style=style.para_style
        ),

    ],justify='center',
)
