import plotly.graph_objects as go
import numpy as np
import pandas as pd
curtailment  = pd.read_csv('https://raw.githubusercontent.com/naohiro701/main/main/electricity/3D/TSO_elect_demand.csv')  
REGION_name = ["TSO_Hokkaido","TSO_Tohoku","TSO_Tokyo","TSO_Hokuriku","TSO_Chubu","TSO_Kansai","TSO_Chugoku","TSO_Shikoku","TSO_Kyushu","TSO_Okinawa"]

for reg in REGION_name:
    data = curtailment[["times", reg]]
    data[reg] = - data[reg]
    data['hours'] = data['times'].astype(str).str.replace(r'.* ',"",regex=True).astype(str).str.replace(r':.*',"",regex=True)
    data['month'] = data['times'].astype(str).str.replace(r' .*',"",regex=True).astype(str).str.replace(r'2019/',"",regex=True).str.zfill(2).str.replace(r'/.*',"",regex=True).str.zfill(2)
    data['day'] = data['times'].astype(str).str.replace(r'.*/',"",regex=True).str.replace(r'.*/',"",regex=True).astype(str).str.replace(r' .*',"",regex=True).str.zfill(2)
    #print(data['day'])
    data['month-day'] = data['month'] + data['day']
    data['hours'] = data['hours'].str.zfill(2)
    
    fig = go.Figure(data=[go.Scatter3d(
        x=data['hours'],
        y=data['month-day'],
        z=data[reg],
        mode='markers',
        
        marker = dict(
        sizeref=750,
        size= 3,
        color = data[reg],
        colorscale = 'Viridis',
        colorbar_title = 'Demand [GW]',
        line_color='rgb(140, 140, 170)'
    )
    )])

    fig.update_layout(
        #width=800, height=800, title = 'Planets!',
    scene = dict(
    xaxis=dict(title='Hour', titlefont_color='Black', backgroundcolor="#FFFFFF"),
    yaxis=dict(title='Day', titlefont_color='Black', backgroundcolor="#FFFFFF"),
    zaxis=dict(title='Demand [GW]', titlefont_color='Black', backgroundcolor="#FFFFFF"),
    # bgcolor = 'rgb(20, 24, 54)'
    ))

    # tight layout
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    # fig.show()
    fig.write_html("a/elect_demand_dust_%s.html"% reg)