## Google FormをベースにURLをまとめるサイトを作る

[こちら](https://naohiro701.github.io/main/electricity/main.html)をご覧ください．

""
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

""

""

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

""

""

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


""

""

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



""