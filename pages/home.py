import dash
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
import style

dash.register_page(__name__, path='/')


img_row_1=dbc.Row( [
    dbc.Col(
        [ 
            html.H6("If you want to remain healthy & fit, avoid excess suger & sweet.",className='text-center'),
            html.Div(html.Img(src='assets/suger.jpg',style=style.home_img),className='text-center')
        ],md=4,style=style.img_section,
    ),
    dbc.Col(
        [ 
            html.H6("Diabetes won't wait, so loose your weight.",className='text-center'),
            html.Div(html.Img(src='assets/gym.jpg',style=style.home_img),className='text-center')
        ],md=4,style=style.img_section,
    ),
],align='center',justify='center'
)

img_row_2=dbc.Row( [
    dbc.Col(
        [ 
            html.H6("Diabetes is a deadly disease, not a bit less than your enemies.",className='text-center'),
            html.Div(html.Img(src='assets/deadly.jpg',style=style.home_img),className='text-center')
        ],md=4,style=style.img_section,
    ),
    dbc.Col(
        [ 
            html.H6("Increase Sweetness in your words, not in your blood.",className='text-center'),
            html.Div(html.Img(src='assets/happy.jpg',style=style.home_img),className='text-center')
        ],md=4,style=style.img_section,
    ),
],align='center',justify='center'
)


layout =[img_row_1,img_row_2]
