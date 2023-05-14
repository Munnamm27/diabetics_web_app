import dash
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
import style



p1='''Diabetes is a chronic condition that affects millions of people around the world. It is a disease that
affects how the body uses glucose, which is the main source of energy for our cells. There are two main
types of diabetes: type 1 diabetes and type 2 diabetes.'''
p2='''Type 1 diabetes is an autoimmune disease in which the immune system attacks and destroys the cells in
the pancreas that produce insulin, a hormone that helps regulate glucose levels in the blood. Type 2
diabetes, on the other hand, is a condition in which the body becomes resistant to insulin or doesn't
produce enough of it.'''
p3='''Managing diabetes requires a delicate balance of diet, exercise, and medication. But there is another
aspect of diabetes management that is often overlooked: the art of balance. Diabetes can be a
demanding disease that requires constant attention and monitoring, but it is also important to find a
balance between managing the disease and living a full and fulfilling life.'''
p4='''One way to achieve this balance is to focus on the things that bring joy and fulfillment, whether that&#39;s
spending time with loved ones, pursuing a hobby, or simply taking a break to relax and recharge. It's also
important to find ways to manage stress, which can have a negative impact on blood glucose levels.'''
p4='''Another aspect of balance is finding a way to enjoy food while still managing diabetes. This can involve
making healthy food choices, but it can also mean allowing yourself to indulge in a favorite treat every
once in a while. The key is to find a balance that works for you, and to make sure that you are still able
to manage your blood glucose levels.'''
p5='''Finally, it's important to remember that diabetes is a journey, and there will be ups and downs along the
way. The key is to stay positive and keep moving forward, even when the road ahead seems daunting.
By finding the art of balance in managing diabetes, it is possible to live a full and fulfilling life while still
keeping the disease under control.'''
dash.register_page(__name__)

page_list=[page['name'] for page in dash.page_registry.values()]
path_list=[page['path'] for page in dash.page_registry.values()]

layout = dbc.Row(
    [

        dbc.Col(
            [ 
                html.H3("Know Diabetes",className='text-center'),
                html.Br(),
                html.P(p1),
                html.P(p2),
                html.P(p3),
                html.P(p4),
                html.P(p5),

                # dcc.Link('Find Your Risk',path_list[2],style=style.hlink),
            ],md=8,style=style.para_style
        ),

    ],justify='center',
)