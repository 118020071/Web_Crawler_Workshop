Outline 服务器+requests+前端html/css/js+bs4+__ __ __+selenium

Outline js/php+服务器后端+php_html+数据库sql/json/txt/excel/csv+API+threading并发并行

Outline 全栈框架/爬虫框架+逆向/混淆代码+session+Ethics

Tut 1

Part 0

show result: request, selenium, api

Part 1 - 30 min

a-What is server

b--Linux log-in

c--Just a computer/BaoTa Panel



xxSkipxx a-What is back-end

b--What is PHP

b--How to do Data Storage

c---What is SQL + Json + Dashboard



a-What is front-end

b--HTML Hyper text Markup Language- show data stored in the server

b--CSS Cascating Style Sheet

b--JavaScript



a-What is middle-end and how from and back connect

b--JS

b--AJAX

b--JQuery



a-What is the framework

b--Angular

b--Vue

b--React



Part 2 - 30 min

1. HTML basics: F12 browser, element - write+show, id/class
2. CSS basics: canvas
3. JS basics: DOM  *Document Object Model*, element and parents and descendants



```html
<!-- Raw HTML -->
<!Doctype html>
<html>

<head>

</head>

<body>
<button>nothing</button>
</body>
</html>



<!-- With style -->
<!Doctype html>
<html>

<head>
<link rel=stylesheet type=text/css href=style.css>
<style>
.bt {background-color: red;}
#bt1 {font-size: xx-large;}
</style>
</head>
<body>
<button class="bt" id="bt1">nothing</button>
</body>
</html>



<!-- With script -->
<!Doctype html>
<html>

<head>

<style>
.bt {background-color: red;}
#bt1 {font-size: xx-large;}

</style>
<script src=script.js></script>
<script>
function change2() {
    //add confirmation box
    //diff than alert box, it has concel button
    var btn = document.getElementById("bt1");
    document.write("click btn");
    document.write(btn);
    alert("emm?");
}
</script>

</head>
<body>
<button class="bt" id="bt1" onclick="change2()">nothing</button>
</body>
</html>
```



5min break



Part 3 - 50min

1. Requests lib - basic notation
2. Element - HTML
3. Path - HTML, CSS, XPath
4. Selenium lib - basic notation



**Tut 2**

Part 0

http://ip.memories1999.com/index.html

show API crawler

show server and how JS get HTML message and pass it to backend and how server send message to front end - http://www.cuhkszofficialaccountapi.top



Part 1 40min

1. Data storage: SQL dashboard, SQL language in python, SQL language in PHP (local)
2. How PHP process SQL, HTML, JS with no output to user.
3. How JS works in between
4. Compare speed
5. Why Json(Dictionary) is used, how is the data open access to front-end



Part 2 30min

1. How to get API- charles proxy debugging (PC+Phone)
2. How to get api data with requests
3. User agent pool and ip pool
4. Threading



Part 3 10min

1. Data storage with sql, excel, json



Part 4 20min

1. session and cookie
2. scrapy framework



Part 5 20min

1. Anti-scrapper

   anti requests on ip, on UA, on cookie

   Anti selenium: image cover (JD), login-taobao

   Separate data storage, generate tempo access with cookie (Wechat official account-Charles, TikTok)

2. Reverse engineering (爬虫学的好，监狱进得早)

   How does the server store data, what is the file on the server. Denied path/robots.txt

3. Ethics and tradeoff:

   -Scraper speed and anti-scraper strength: more slower, more like human, no need to defend

   -Why expose data in Json not SQL: speed for user

   -误伤user/scraper

   -携程

4. Project introduction and take-home work