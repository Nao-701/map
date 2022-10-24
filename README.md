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

