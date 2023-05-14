import dash
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
import style



p1='''This application uses machine learning algorithms to predict the likelihood of diabetes in individuals. Our
mission is to help people take control of their health by providing them with information about their risk
of developing this chronic condition.'''
p2='''The algorithm used analyzes a range of factors, including age, weight, family history, and lifestyle habits,
to generate a personalized risk assessment for each user. This assessment can help individuals take
proactive steps to reduce their risk of developing diabetes, such as adopting a healthier diet or
increasing physical activity.'''
p3='''We believe that everyone deserves access to high-quality healthcare information, regardless of their
location or financial situation. That's why we've made this application completely free to use, with no
hidden fees or charges. Our goal is to empower individuals to take control of their health and make
informed decisions about their care.'''
p4='''Thank you for choosing this application, and we look forward to helping you on your journey towards a
healthier, happier life.'''
dash.register_page(__name__)

page_list=[page['name'] for page in dash.page_registry.values()]
path_list=[page['path'] for page in dash.page_registry.values()]

layout = dbc.Row(
    [

        dbc.Col(
            [ 
                html.H3("About",className='text-center'),
                html.Br(),
                html.P(p1),
                html.P(p2),
                html.P(p3),
                html.P(p4),

                # dcc.Link('Find Your Risk',path_list[2],style=style.hlink),
            ],md=6,style=style.para_style
        ),

    ],justify='center',
)