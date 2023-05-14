import dash
from dash import dcc, html,callback,Input,Output,State
import plotly.express as px
import dash_bootstrap_components as dbc
import pickle
import style
import pandas as pd

with open('xgb_diabetics.best', 'rb') as file:
    model = pickle.load(file)

cols=['Age', 'Gender', 'Family_Diabetes', 'DelayedHealing',
       'PhysicallyActive', 'BMI', 'Smoking', 'Sleep', 'RegularMedicine',
       'JunkFood', 'Stress', 'BPLevel', 'UrinationFrequency']


physical_act=['one hr or more', 'less than half an hr', 'none', 'more than half an hr']
juck_food=['occasionally', 'very often', 'often', 'always']
stress=['sometimes', 'not at all', 'very often', 'always']
bp=['high','low','normal']
urin=['not much', 'quite often']


physical_act_v=['More Than 1 Hour', 'Less Than Half an Hour', 'none', 'More Than Half an Hour']
juck_food_v=['Occasionally', 'Very Often', 'Often', 'Always']
stress_v=['Sometimes', 'Not at All', 'Very Often', 'Always']
bp_v=['High','Low','Normal']
urin_v=['Not Much', 'Quite Often']

dash.register_page(__name__)






top_row=dbc.Row( 
    [ 
        html.H5("Please Provide Required Information",style={'textAlign':'center'}),
        html.Br(),
        html.Br()

    ]
)


personal_col=dbc.Col( 
    [ 
        html.H6("Personal Information",className='text-center'),
        html.Br(),

        html.Label("Enter Age"),
        dbc.Input(type='number',id='age',value=27),
        html.Label(),
        html.Label("Select Gender"),
        dcc.Dropdown(['Male','Female'],id='gender',value='Male'),
        html.Br(),
        html.Label("Enter Height (cm)"),
        dbc.Input(type='number',id='height',value=180),
        html.Br(),
        html.Label("Enter Weight (kg)"),
        dbc.Input(type='number',id='weight',value=70),
        html.Br(),
        html.Label("Family Diabetes"),
        dcc.Dropdown(options={'yes':'Yes','no':'No'},id='family',value='yes'),
        html.Br(),


    ],md=2,style=style.dropdowns_style
)


habitual_col=dbc.Col( 
    [ 
        html.H6("Habitual Information"),
        html.Br(),

        html.Label("Physical Activity"),
        dcc.Dropdown(options=dict(zip(physical_act,physical_act_v)),id='phy',value='none'),
        html.Br(),
        html.Label("Sleep Time (Hours)"),
        dbc.Input(type='number',id='sleep',value=8),
        html.Br(),
        html.Label("Junk Food Consumption"),
        dcc.Dropdown(options=dict(zip(juck_food,juck_food_v)),id='junk',value='occasionally'),
        html.Br(),
        html.Label("Smoking Habit"),
        dcc.Dropdown(options={'yes':'Yes','no':'No'},id='smoking',value='yes'),
        html.Br(),


    ],md=2,style=style.dropdowns_style
)

other_col=dbc.Col( 
    [ 
        html.H6("Other Informations"),
        html.Br(),

        html.Label("Stress"),
        dcc.Dropdown(options=dict(zip(stress,stress_v)),id='stress',value='always'),
        html.Br(),
        html.Label("Blood Pressure"),
        dcc.Dropdown(options=dict(zip(bp,bp_v)),id='bp',value='normal'),
        html.Br(),
        html.Label("Delayed Healing"),
        dcc.Dropdown(options={'yes':'Yes','no':'No'},id='heal',value='yes'),
        html.Br(),
        html.Label("Urine Frequency"),
        dcc.Dropdown(options=dict(zip(urin,urin_v)),id='urin',value='quite often'),
        html.Br(),
        html.Label("Regular Medicine"),
        dcc.Dropdown(options={'yes':'Yes','no':'No'},id='medicine',value='yes'),
        html.Br(),


    ],md=2,style=style.dropdowns_style
)


button_col=dbc.Col( 
    [   html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Button("Click to Predict",n_clicks=0,id='btn')
    ],md=1
)

result_col=dbc.Col( 
    [   html.H4("Risk Probability",className='text-center'),
        html.Br(),
        html.Div(id='out',className='text-center')
    ],md=3,style=style.dropdowns_style
)


drop_down_row=dbc.Row( 
    [ 
        personal_col,
        habitual_col,
        other_col,
        button_col,
        result_col
    ],justify='center',align='left'
)


layout = [top_row,drop_down_row]



@callback(
    Output('out','children'),
    Input('btn','n_clicks'),
    State('gender','value'),
    State('age','value'),
    State('height','value'),
    State('weight','value'),
    State('family','value'),
    State('phy','value'),
    State('sleep','value'),
    State('junk','value'),
    State('smoking','value'),
    State('stress','value'),
    State('bp','value'),
    State('heal','value'),
    State('urin','value'),
    State('medicine','value'),

)
def out(n,gender,ages,h,w,family,phy,sleep,junk,smoke,stress,bp,heal,urin,med):
    ages=45
    if (ages<40):
        age = 'less than 40'
    if (ages<=40) & (ages<50):
        age = '40-59'
    if (ages<=50) & (ages<60):
        age = '50-59'
    if (ages>=60):
        age = '60 or older'
    gender = gender
    family_diabetes = family
    delayed_healing = heal
    physical_activity = phy
    bmi = w/((h/100))**2
    smoking = smoke
    sleep = 4
    regular_medicine = med
    junk_food = smoke
    stress = stress
    bplevel = bp
    urin_freq = urin

    def prediction_ready_data():
        activity_f=['more than half an hr', 'none', 'one hr or more','x']

        stress_f=['not at all', 'sometimes','very often','x']

        bp_level_f=['low', 'normal','x']

        junk_food_f = ['occasionally', 'often', 'very often','x']

        age_f=['50-59','60 or older', 'less than 40','x']

        predict_df=pd.DataFrame([[age,gender,family_diabetes,delayed_healing,physical_activity,bmi,smoking,sleep,regular_medicine,junk_food,stress,bplevel,urin_freq]],columns=cols)
        def get_bin_encoder(d):
            if (d=='yes') or (d=='not much') or (d=='Male'):
                return 1
            if (d=='no') or (d=='quite often') or (d=='Female'):
                return 0

        fet=['Gender','Family_Diabetes','DelayedHealing','Smoking','RegularMedicine','UrinationFrequency']

        def prep_data(data):
            for feature in fet:
                data[feature]=data[feature].apply(get_bin_encoder)

            return data[fet]

        def get_predict_dummy(drop_down_cols,selected_fet):
            dummy_df=pd.DataFrame(columns=drop_down_cols[:-1])
            if selected_fet in drop_down_cols[:-1]:
                dummy_df[selected_fet]=[1]
                return dummy_df.fillna(0)
            else:
                dummy_df[drop_down_cols[0]]=[0]
                return dummy_df.fillna(0)
        bin_encoded=prep_data(predict_df)
        fet_2=[activity_f,stress_f,bp_level_f,junk_food_f,age_f]
        d_list=[]
        for f,select in zip(fet_2,[physical_activity,junk_food,stress,bplevel,age]):
            d_list.append(get_predict_dummy(f,select))

        prediction_ready_df=pd.concat([predict_df[['BMI','Sleep']],d_list[0],d_list[1],d_list[2],d_list[3],d_list[4],bin_encoded],axis=1)
        return prediction_ready_df
    val=model.predict_proba(prediction_ready_data().values)
    pred_val=model.predict(prediction_ready_data().values)[0]



    if pred_val==0:
        out_string=[ html.H6(f'You Have {round(val[0][1]*100,2)}% Diabetes Risk',style={'color':'green'}),
                    html.Br(),
                    html.P(f'Maintain Your Current Lifestyle to Avoid Risk'),
                    html.Img(src="assets/checked.png",style=style.icon_img)]
    if pred_val==1:
        out_string=[ html.H6(f'You Have {round(val[0][1]*100,2)}% Diabetes Risk',style={'color':'red'}),
                    html.Br(),
                    html.P(f'Click the Link Below To Know About Healthy Lifestyle'),
                    
                    
                    dcc.Link('Healthy Living','/healthy-living'),
                    html.Br(),
                    html.Img(src="assets/cancel.png",style=style.icon_img),
                    ]
    if n==0:
        return html.H4(f"")
    else:
        return out_string
