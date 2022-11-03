## Google FormをベースにURLをまとめるサイトを作る

[こちら](https://script.google.com/macros/s/AKfycbyCSELylp2itm2oRrfi84WOv12c0c2PgzflOHQdWQo/exec)をご覧ください．

### main.gs
スプレッドシートからGASへの接続を行います．
```
function doGet() {
  Logger.log(Session.getActiveUser());
  const htmlOutput = HtmlService.createTemplateFromFile("index").evaluate();
  htmlOutput.setTitle('講義資料');
  return htmlOutput;
}

function getSheet(name){
  // SSIDはスプレッドシートID
  var ssId = '';
  var ss = SpreadsheetApp.openById(ssId);
  // 指定されたシート名からシートを取得
  var sheet = ss.getSheetByName(name);
  return sheet;
}

function getData() {
  // 指定したシートからデータを取得
  var values = getSheet('フォームの回答 1').getDataRange().getValues();
  return values;
}

```

### index.html

```

<!DOCTYPE html>
<html>
<head>
<base target="_top">
<meta name="viewport" content="width=device-width, maximum-scale=1.0, minimum-scale=0.5,user-scalable=yes,initial-scale=0.5" />
<title>まとめ</title>
<?!= HtmlService.createHtmlOutputFromFile('stylesheet').getContent(); ?>
<?!= HtmlService.createHtmlOutputFromFile('script').getContent(); ?>
<?// スプレッドシートからデータを取得
var data = getData();
?>
</head>
<body>

<header>
<nav class="navbar navbar-dark fixed-top bg-dark">
<a class="navbar-brand" href="url of google form" onclick="navigateTargetUrl(); return false;">投稿</a>
<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
<span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse" id="navbarCollapse">
<ul class="navbar-nav mr-auto">
<li class="nav-item active">
<a class="nav-link" href="url of this site">更新 <span class="sr-only">(current)</span></a>
</li>
<li class="nav-item">
<a class="nav-link" href="url of scripts" onclick="navigateTargetUrl(); return false;">GAS</a>
</li>
<li class="nav-item">
<a class="nav-link" href="url of spreadsheet" onclick="navigateTargetUrl(); return false;">スプレッドシート</a>
</li>
</ul>
</div>
</nav>
</header>

<nav class="navbar navbar-light bg-light">
<a class="navbar-brand" href="url of form" onclick="navigateTargetUrl(); return false;">投稿はここをクリック！</a>
</nav>
<div class="jumbotron">
<h1>こちらのサイトについて</h1>
このサイトでは、ネットに転がっている講義資料を整理できます。
</div>

<div class="container">
<?
for(var j=1; j<3; j++)
{
output.append('<h2>' + data[1][j] + '</h2><p>' + data[3][j] + '</p><ol>');

for(var value=data.length-1; value>=1; value--)
{
if(data[value][3].indexOf(data[2][j]) != -1)
output.append('<li><a href="' + data[value][2] + '" onclick="navigateTargetUrl(); return false;">' + data[value][1] +'</a></li>');
}

output.append('</ol><hr>');
}

?>

</div>
</div>
<footer id="red">
  <h1 class="text"></h1>
  <h2 class="text2">&copy;  Naoi Hiroki </h2>
</footer>
</body>
</html>

```
### fotter.html

```

//以下フッター

@import url(https://fonts.googleapis.com/css?family=Lato:900);
#red{ 
  border-top: solid #A44B4B;
  border-width: 15px;
  background: #2E2E2E; 
  bottom:0; 
  height:100%;
  width:100%; 
  height:50px; 
  margin-top:20%;
}

.text {
  color: #424242;
  font-family: Lato;
  font-size: 60px;
  text-align: center;
  margin-top: 50px;
}

.text2 {
  color: #424242;
  font-family: Lato;
  font-size: 20px;
  text-align: center;
  margin-top: -50px;
}

.text3 {
  color: #424242;
  font-family: Lato;
  font-size: 20px;
  text-align: center;
  margin-top: -20px;
  float: center;
}

#page-footer {
  display: none !important;
}


```

### script.html
数式に対応させる予定でした.

```

<script>
  // a タグの href 属性に記述された URL を、新規ウィンドウで開く関数
  function navigateTargetUrl() {
    window.open(this.event.target.href, null, "noopener");
  }
  
  var params = (new URL(document.location)).searchParams;
  var value= params.get("value")
</script>
<script type="text/javascript"
src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_HTML" defer>
</script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
tex2jax: { inlineMath: [['$','$'], ["</br>(","</br>)"]] } });
</script>
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>

```


## GASをベースに論文のRSSを用いて公式LINEより送信する

### 
スプレッドシートからGASへの接続を行い，公式LINEでBroadcastします．

```
//TOKENS
CHANNEL_ACCESS_TOKEN = ""
let sheetId = ''
let sheet = SpreadsheetApp.openById(sheetId).getActiveSheet()
var API_URL = "https://api.line.me/v2/bot/message/reply"
var REPLY_TOKEN
var STAT_ID
```
```
//トリガーで実行する，RSSを取得してくる関数
function GET_RSS() {
  var Rsheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("urls");
  var Rrow = Rsheet.getLastRow();

  if (Rrow) {
    var rssLists = Rsheet.getRange(1, 1, Rrow, 3).getValues();
    // フィードURL

    // ジャーナルごとでループさせる
    for (var jurnal_number = 0 ; jurnal_number < rssLists.length; jurnal_number++) {

      paper_name = rssLists[jurnal_number][0]
      my_rss = rssLists[jurnal_number][1]
      
      // フィードを取得
      var rss_data = UrlFetchApp.fetch(my_rss);
      // XMLをパース
      var rss_xml = XmlService.parse(rss_data.getContentText());
      // 各データの要素を取得
      var rss_entries = rss_xml.getRootElement().getChildren('channel')[0].getChildren('item');
      
      var title = []
      var link = []

      for(var paper_number = 0; paper_number < rss_entries.length; paper_number++){
        title[paper_number] = rss_entries[paper_number].getChildText('title')
        link[paper_number] = rss_entries[paper_number].getChildText('link')
        // description = rss_entries[paper_number].getChildText('description')
      }
      
      // CHECK してから SEND する関数へ送る．ジャーナルごとにLISTを送る．
      
      // Logger.log(title);
      check(paper_name, title, link)
    }
  }
}

```

```
// キーワード検索
function check(paper_name,title, link){

  let sheet_keywords = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("keyword");
  let keywords = sheet_keywords.getDataRange().getValues();

  var count = 0
  var interesting_title = []
  var interesting_link = []

  for(var num = 0; num < title.length; num++){

    // Logger.log(title[num])

    if (keywords.some(function(word){return (title[num].indexOf(word) !== -1);})) {

      // interesting_title[count] = title[num]
      // interesting_link[count] = link[num]

      var array = [title[num],link[num]]
      interesting_link[count] = array.join("\n ");
      
      count = count + 1; 
    }
    // 送信！！
  }
    // Logger.log(interesting_title);
    // send(paper_name, interesting_title,interesting_link); 
    send(paper_name, interesting_link); 
}
```

```
// 送信する文章を一括で作成する．
function send(paper_name,interesting_link) {
  let message_texts = interesting_link.join("\n \n  ー－－－－－－－－－－－－－－ \n\n");
  Logger.log(message_texts.length);

  let message = {
      "messages": [
        {
        'type': 'text',
        'text': "⚡" + paper_name+"⚡\n"
      }]
    }
  if (message_texts.length == 0){
    message = {
      "messages": [
        {
        'type': 'text',
        'text': paper_name+"には入力されたキーワードを含む論文がありませんでした．"
      }]
    }
  }
  else if (message_texts.length<5000){
    message = {
      "messages": [
        {
        'type': 'text',
        'text': "⚡" + paper_name+"⚡\n \nー－－－－－－－－－－－－－－\n\n" + message_texts
      }]
    }
  } else{
    message = {
      "messages": [
        {
        'type': 'text',
        'text':  paper_name+"には対象の論文がありすぎて，送れませんでした．" 
      }]
    }
  }

  UrlFetchApp.fetch('https://api.line.me/v2/bot/message/broadcast', {
    method: 'post',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + CHANNEL_ACCESS_TOKEN,
    },
    payload: JSON.stringify(message),
  });
}
```
