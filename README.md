## はじめに

[こちら](https://naohiro701.github.io/main/electricity/main.html)をご覧ください．


### 電力会社の当日実績のスクレイピング

```

function my_function(){
  let date = Utilities.formatDate(new Date(), "JST","yyyyMMdd");
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var REMOTE_SOURCES = [
    {
      'url': 'https://denkiyoho.hepco.co.jp/area/data/juyo_01_'+date+'.csv',
      'sheetname': 'hokkaido',
    },
    {
      'url': 'https://setsuden.nw.tohoku-epco.co.jp/common/demand/juyo_02_'+date+'.csv',
      'sheetname': 'tohoku',
    },
    {
      'url':'https://www.tepco.co.jp/forecast/html/images/juyo-d1-j.csv',
      'sheetname': 'tokyo',
    },
    {
      'url':'https://www.rikuden.co.jp/nw/denki-yoho/csv/juyo_05_'+date+'.csv',
      'sheetname': 'hokuriku',
    },
        {
      'url':'https://powergrid.chuden.co.jp/denki_yoho_content_data/juyo_cepco003.csv',
      'sheetname': 'chubu',
    },
    {
      'url': 'https://www.kansai-td.co.jp/yamasou/juyo1_kansai.csv',
      'sheetname': 'kansai',
    },
    {
      'url': 'https://www.energia.co.jp/nw/jukyuu/sys/juyo_07_'+date+'.csv',
      'sheetname': 'chugoku',
    },
    {
      'url':'https://www.yonden.co.jp/nw/denkiyoho/juyo_shikoku.csv',
      'sheetname': 'shikoku',
    },
    {
      'url':'https://www.kyuden.co.jp/td_power_usages/csv/juyo-hourly-'+date+'.csv',
      'sheetname': 'kyushu',
    },
        {
      'url':'https://www.okiden.co.jp/denki2/juyo_10_'+date+'.csv',
      'sheetname': 'okinawa',
    },
  ];
  var REMOTE_SOURCES_OPTIONS = {
    method : "get"
  };

  for(var i =0; i<REMOTE_SOURCES.length; i++){    
    response = UrlFetchApp.fetch(REMOTE_SOURCES[i].url, REMOTE_SOURCES_OPTIONS);
    var sheetName = REMOTE_SOURCES[i].sheetname;
    var sh = ss.getSheetByName(sheetName);
    if(sh == null)
    {
      ss.insertSheet(sheetName);
      sh = ss.getSheetByName(sheetName);
    } 
    var data = response.getContentText("Shift_JIS"); 
    var csv = Utilities.parseCsv(data);
    sh.getRange(1,1,csv.length,csv[0].length).setValues(csv);
  }
}

```

この結果より得られるスプレッドシートより，グラフを作成し，ページに貼り付け．

30分毎に１回程度実行すればよい．

### 需要実績を3Dで可視化する

```

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
        colorbar_title = 'Value',
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

```
