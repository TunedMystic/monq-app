#!/usr/bin/env python
import os
import sys
import uuid
import datetime
import random
import arrow
import django

# Clear the database.
def endall():
  # Delete Snippets.
  for obj in Snippet.objects.all():
    obj.delete()
  # Delete Users.
  for obj in get_user_model().objects.all():
    obj.delete()

# Make User object.
def makeUser(n, e, p):
  try:
    usr = get_user_model().objects.get(username = n)
    return usr
  except get_user_model().DoesNotExist:
    return get_user_model().objects.create_user(username = n, email = e, password = p)

# Make a Snippet
def makeSnippet(author = None, title = None, language = None, visibility = None, url_code = None, content = None, date = None, tags = None):
    s = Snippet.objects.create(author = author, title = title, language = language, visibility = visibility, \
                url_code = url_code, content = content, date_added_raw = date)
    for t in tags:
      s.tags.add(t)
    s.save()

# Make a random date.
def randomDate():
  """
  This function will return a random datetime between two datetime objects.
  """
  start = arrow.get(datetime.datetime(2014, 7, 1, 12, 0, 0))
  end = arrow.get(datetime.datetime(2014, 12, 30, 12, 0, 0))
  delta = end - start
  int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
  random_second = random.randrange(int_delta)
  d = start + datetime.timedelta(seconds=random_second)
  return arrow.get(d).datetime

# Return a random User.s
randomUser = lambda: get_user_model().objects.all()[random.randrange(0, get_user_model().objects.count())]

# Make a random Url.
randomUrl = lambda: str(uuid.uuid4())[:6]

def main():
  
  # Make Users.
  makeUser("Harry", "harry@gmail.com", "harry101")
  makeUser("Natalie", "natalie@gmail.com", "natalie101")
  makeUser("Ramin", "ramin@gmail.com", "ramin101")
  makeUser("Tyler", "tyler@gmail.com", "tyler101")
  makeUser("Bella", "bella@gmail.com", "bella101")
  makeUser("Blossom", "blossom@gmail.com", "blossom101")
  makeUser("Starbuck", "starbuck@gmail.com", "starbuck101")
  makeUser("Chewbacca", "chewbacca@gmail.com", "chewbacca101")
  makeUser("Vader", "vader@gmail.com", "vader101")
  makeUser("Obi-wan", "obiwan@gmail.com", "obiwan101")
  Drogo = get_user_model().objects.create_superuser(username = "drogo", email = "drogo@gmail.com", password = "drogo101")
  Anakin = get_user_model().objects.create_superuser(username = "anakin", email = "anakin@gmail.com", password = "anakin101")
  
  # Make some Snippets!
  
  makeSnippet(
    author = randomUser(), 
    title = "Generate a random date", 
    language = "python", 
    content = "from random import randrange\r\nfrom datetime import timedelta\r\n\r\ndef random_date(start, end):\r\n    \"\"\"\r\n    This function will return a random datetime between two datetime \r\n    objects.\r\n    \"\"\"\r\n    delta = end - start\r\n    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds\r\n    random_second = randrange(int_delta)\r\n    return start + timedelta(seconds=random_second)", 
    visibility = "public",
    url_code = randomUrl(), 
    tags = ["js", "web", "dev", "date", "program"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Send mail with Gmail in Python",
    language = "python",
    content = "import smtplib\r\n \r\ndef sendemail(from_addr, to_addr_list, cc_addr_list,\r\n              subject, message,\r\n              login, password,\r\n              smtpserver='smtp.gmail.com:587'):\r\n    \r\n    header  = 'From: %s\\n' % from_addr\r\n    header += 'To: %s\\n' % ','.join(to_addr_list)\r\n    header += 'Cc: %s\\n' % ','.join(cc_addr_list)\r\n    header += 'Subject: %s\\n\\n' % subject\r\n    message = header + message\r\n    \r\n    server = smtplib.SMTP(smtpserver)\r\n    server.starttls()\r\n    server.login(login,password)\r\n    problems = server.sendmail(from_addr, to_addr_list, message)\r\n    server.quit()",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["gmail", "python", "dev", "Python-program"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Get Username from a prompt",
    language = "python",
    content =  "#!/usr/bin/env python\r\n\r\n#get the username from a prompt\r\nusername = raw_input(\"Login: >> \")\r\n\r\n#list of allowed users\r\nuser1 = \"Jack\"\r\nuser2 = \"Jill\"\r\n\r\n#control that the user belongs to the list of allowed users\r\nif username == user1:\r\n    print \"Access granted\"\r\nelif username == user2:\r\n    print \"Welcome to the system\"\r\nelse:\r\n    print \"Access denied\"",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["user", "username", "python", "prompt"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Expanding Boxes Navigation",
    language = "css",
    content =  "nav {\r\n    background: #444;\r\n    border-bottom: 8px solid #E6E2DF;\r\n    overflow: hidden;\r\n    position: relative;\r\n    width: 100%;\r\n}\r\nnav:after {\r\n    content: \"\";\r\n    position: absolute;\r\n    left: 0;\r\n    bottom: 0;\r\n    width: 100%;\r\n    height: 2px;\r\n    background: white; \r\n}\r\nnav ul {\r\n    background: -moz-linear-gradient(left,\r\n                #444 0%,\r\n                #444 50%,\r\n                #41d05f 100%);\r\n    background: -webkit-gradient(linear, left top, right top,\r\n                color-stop(0%,#444),\r\n                color-stop(50%,#444),\r\n                color-stop(50%,#41d05f),\r\n                color-stop(100%,#41d05f));\r\n    list-style: none;\r\n    overflow: hidden;\r\n    padding: 0 0 0 20px;\r\n    width: 810px;\r\n}\r\nnav li {\r\n    display: inline;\r\n}\r\nnav a {\r\n    color: white;\r\n    display: block;\r\n    float: left;\r\n    font-family: \"myriad-pro-1\",\"myriad-pro-2\", HelveticaNeue, Helvetica, Arial, Sans-Serif;\r\n    font-size: 22px;\r\n    padding: 12px 0;\r\n    text-decoration: none;\r\n    text-align: center;\r\n    width: 19%;\r\n    -webkit-transition: width 0.12s ease;\r\n       -moz-transition: width 0.12s ease;\r\n         -o-transition: width 0.12s ease;\r\n            transition: width 0.12s ease;\r\n}\r\nnav a:hover {\r\n    color: white;\r\n}\r\nnav a:hover span {\r\n    border-bottom: 2px solid white;\r\n}\r\nnav .a-home {\r\n    background: #ff8400;\r\n    z-index: 100;\r\n    position: relative;\r\n}    \r\nnav .a-forums {\r\n    background: #e42b2b;\r\n}    \r\nnav .a-videos {\r\n    background: #a800ff;\r\n}    \r\nnav .a-downloads {\r\n    background: #49a7f3;\r\n}   \r\nnav .a-snippets {\r\n    background: #41d05f;\r\n}\r\n.home nav {\r\n    border-bottom-color: #ff8400;\r\n}\r\n.forums nav {\r\n    border-bottom-color: #e42b2b;\r\n}\r\n.videos nav {\r\n    border-bottom-color: #a800ff;\r\n}\r\n.downloads nav {\r\n    border-bottom-color: #49a7f3;\r\n}\r\n.snippets nav {\r\n    border-bottom-color: #41d05f;\r\n}\r\nnav li:hover a {\r\n    width: 24%;\r\n}\r\nnav ul:hover .active {\r\n    width: 19%;\r\n}\r\nnav ul:hover .active:hover {\r\n    width: 24%;\r\n}\r\nnav li a.active {\r\n    width: 24%;\r\n}",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["css", "html", "js", "boxes", "expand", "navigatio"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Standard Social Media Template Tags",
    language = "html",
    content =  "<!-- Place this data between the <head> tags of your website -->\r\n<title>Page Title. Maximum length 60-70 characters</title>\r\n<meta name=\"description\" content=\"Page description. No longer than 155 characters.\" />\r\n\r\n<!-- Twitter Card data -->\r\n<meta name=\"twitter:card\" content=\"summary\">\r\n<meta name=\"twitter:site\" content=\"@publisher_handle\">\r\n<meta name=\"twitter:title\" content=\"Page Title\">\r\n<meta name=\"twitter:description\" content=\"Page description less than 200 characters\">\r\n<meta name=\"twitter:creator\" content=\"@author_handle\">\r\n<!-- Twitter Summary card images must be at least 120x120px -->\r\n<meta name=\"twitter:image\" content=\"http://www.example.com/image.jpg\">\r\n\r\n<!-- Open Graph data -->\r\n<meta property=\"og:title\" content=\"Title Here\" />\r\n<meta property=\"og:type\" content=\"article\" />\r\n<meta property=\"og:url\" content=\"http://www.example.com/\" />\r\n<meta property=\"og:image\" content=\"http://example.com/image.jpg\" />\r\n<meta property=\"og:description\" content=\"Description Here\" /> \r\n<meta property=\"og:site_name\" content=\"Site Name, i.e. Moz\" />\r\n<meta property=\"fb:admins\" content=\"Facebook numeric ID\" />",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["html", "social", "css", "facebook", "twitter"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Random readable password",
    language = "php",
    content = "<?php\n\nfunction random_readable_pwd($length=10){\n \n    // the wordlist from which the password gets generated \n    // (change them as you like)\n    $words = 'dog,cat,sheep,sun,sky,red,ball,happy,ice,';\n    $words .= 'green,blue,music,movies,radio,green,turbo,';\n    $words .= 'mouse,computer,paper,water,fire,storm,chicken,';\n    $words .= 'boot,freedom,white,nice,player,small,eyes,';\n    $words .= 'path,kid,box,black,flower,ping,pong,smile,';\n    $words .= 'coffee,colors,rainbow,plus,king,tv,ring';\n \n    // Split by \",\":\n    $words = explode(',', $words);\n    if (count($words) == 0){ die('Wordlist is empty!'); }\n \n    // Add words while password is smaller than the given length\n    $pwd = '';\n    while (strlen($pwd) < $length){\n        $r = mt_rand(0, count($words)-1);\n        $pwd .= $words[$r];\n    }\n \n    // append a number at the end if length > 2 and\n    // reduce the password size to $length\n    $num = mt_rand(1, 99);\n    if ($length > 2){\n        $pwd = substr($pwd,0,$length-strlen($num)).$num;\n    } else { \n        $pwd = substr($pwd, 0, $length);\n    }\n \n    return $pwd;\n \n}\n\n?>",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["php", "password", "web", "webdev", "php-code"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Simple cURL example",
    language = "php",
    content = "<?php\n\nfunction curl_download($Url){\n \n    // is cURL installed yet?\n    if (!function_exists('curl_init')){\n        die('Sorry cURL is not installed!');\n    }\n \n    // OK cool - then let's create a new cURL resource handle\n    $ch = curl_init();\n \n    // Now set some options (most are optional)\n \n    // Set URL to download\n    curl_setopt($ch, CURLOPT_URL, $Url);\n \n    // Set a referer\n    curl_setopt($ch, CURLOPT_REFERER, \"http://www.example.org/yay.htm\");\n \n    // User agent\n    curl_setopt($ch, CURLOPT_USERAGENT, \"MozillaXYZ/1.0\");\n \n    // Include header in result? (0 = yes, 1 = no)\n    curl_setopt($ch, CURLOPT_HEADER, 0);\n \n    // Should cURL return or print out the data? (true = return, false = print)\n    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);\n \n    // Timeout in seconds\n    curl_setopt($ch, CURLOPT_TIMEOUT, 10);\n \n    // Download the given URL, and return output\n    $output = curl_exec($ch);\n \n    // Close the cURL resource, and free system resources\n    curl_close($ch);\n \n    return $output;\n\n?>",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["curl", "php", "programming", "php-curl"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Simple HTML5 Starter template",
    language = "html",
    content = "<!doctype html>\r\n<html lang=\"en\">\r\n<head>\r\n  <meta charset=\"utf-8\">\r\n  <title>The Brand New Web Site</title>\r\n  <meta name=\"description\" content=\"The Brand New Web Site\">\r\n  <meta name=\"author\" content=\"Barattalo.it\">\r\n  <link rel=\"stylesheet\" href=\"css/styles.css?v=1.0\">\r\n  <!--[if lt IE 9]>\r\n  <script src=\"http://html5shiv.googlecode.com/svn/trunk/html5.js\"></script>\r\n  <![endif]-->\r\n</head>\r\n<body>\r\n \r\n \r\n \r\n\t<!-- run javascript at the end -->\r\n  <script src=\"js/scripts.js\"></script>\r\n</body>\r\n</html>",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["html", "html5", "template", "css", "web"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Find all the links in a page",
    language = "php",
    content = "<?php\n\n  $html = file_get_contents('http://www.example.com');\n     \n  $dom = new DOMDocument();\n  @$dom->loadHTML($html);\n\n  // grab all the on the page\n  $xpath = new DOMXPath($dom);\n  $hrefs = $xpath->evaluate(\"/html/body//a\");\n\n  for ($i = 0; $i < $hrefs->length; $i++) {\n    $href = $hrefs->item($i);\n    $url = $href->getAttribute('href');\n    echo $url.'<br />';\n  }\n\n?>",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["php", "html", "script", "web", "links"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Big curly blockquotes",
    language = "css",
    content =  "blockquote {\r\n\tposition: relative;\r\n\ttext-indent: 2em;\r\n}\r\n \r\n.bqstart,\r\n.bqend { font-size: 300%; }\r\n \r\n/* apply IE specific rules first */\r\n.bqstart {\r\n\ttext-indent: 0;\r\n\tmargin: -0.6em 0 -2em 0;\r\n\tfloat: left;\r\n}\r\n \r\nblockquote > .bqstart {\r\n\t/* add extra non-ie rules */\r\n\tposition: absolute;\r\n\ttop: -0.2em;\r\n\tleft: 0;\r\n\t/* remove IE specific rules */\r\n\tfloat: none;\r\n\tmargin: 0;\r\n}\r\n \r\n.bqend {\r\n\tposition: absolute;\r\n\tmargin-top: -0.6em;\r\n\tright: 0;\r\n\ttext-indent: 0;\r\n}\r\n \r\nblockquote > .bqend {\r\n\tmargin-top: -0.2em;\r\n}",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["css", "html", "css3", "style", "block"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Master Stylesheet",
    language = "css",
    content = "/***** Global Settings *****/\r\n \r\nhtml, body {\r\nborder:0;\r\nmargin:0;\r\npadding:0;\r\n}\r\n \r\nbody {\r\nfont:100%/1.25 Arial, Helvetica, sans-serif;\r\n}\r\n \r\n/***** Headings *****/\r\n \r\nh1, h2, h3, h4, h5, h6 {\r\nmargin:0;\r\npadding:0;\r\nfont-weight:normal;\r\n}\r\n \r\nh1 {\r\npadding:30px 0 25px 0;\r\nletter-spacing:-1px;\r\nfont-size:2em;\r\n}\r\n \r\nh2 {\r\npadding:20px 0;\r\nletter-spacing:-1px;\r\nfont-size:1.5em;\r\n}\r\n \r\nh3 {\r\nfont-size:1em;\r\nfont-weight:bold;\r\n}\r\n \r\n/***** Common Formatting *****/\r\n \r\np, ul, ol {\r\nmargin:0;\r\npadding:0 0 1.25em 0;\r\n}\r\n \r\nul, ol {\r\npadding:0 0 1.25em 2.5em;\r\n}\r\n \r\nblockquote {\r\nmargin:1.25em;\r\npadding:1.25em 1.25em 0 1.25em;\r\n}\r\n \r\nsmall {\r\nfont-size:0.85em;\r\n}\r\n \r\nimg {\r\nborder:0;\r\n}\r\n \r\nsup {\r\nposition:relative;\r\nbottom:0.3em;\r\nvertical-align:baseline;\r\n}\r\n \r\nsub {\r\nposition:relative;\r\nbottom:-0.2em;\r\nvertical-align:baseline;\r\n}\r\n \r\nacronym, abbr {\r\ncursor:help;\r\nletter-spacing:1px;\r\nborder-bottom:1px dashed;\r\n}\r\n \r\n/***** Links *****/\r\n \r\na,\r\na:link,\r\na:visited,\r\na:hover {\r\ntext-decoration:underline;\r\n}\r\n \r\n/***** Forms *****/\r\n \r\nform {\r\nmargin:0;\r\npadding:0;\r\ndisplay:inline;\r\n}\r\n \r\ninput, select, textarea {\r\nfont:1em Arial, Helvetica, sans-serif;\r\n}\r\n \r\ntextarea {\r\nwidth:100%;\r\nline-height:1.25;\r\n}\r\n \r\nlabel {\r\ncursor:pointer;\r\n}\r\n \r\n/***** Tables *****/\r\n \r\ntable {\r\nborder:0;\r\nmargin:0 0 1.25em 0;\r\npadding:0;\r\n}\r\n \r\ntable tr td {\r\npadding:2px;\r\n}\r\n \r\n/***** Wrapper *****/\r\n \r\n#wrap {\r\nwidth:960px;\r\nmargin:0 auto;\r\n}\r\n \r\n/***** Global Classes *****/\r\n \r\n.clear         { clear:both; }\r\n.float-left    { float:left; }\r\n.float-right   { float:right; }\r\n \r\n.text-left     { text-align:left; }\r\n.text-right    { text-align:right; }\r\n.text-center   { text-align:center; }\r\n.text-justify  { text-align:justify; }\r\n \r\n.bold          { font-weight:bold; }\r\n.italic        { font-style:italic; }\r\n.underline     { border-bottom:1px solid; }\r\n.highlight     { background:#ffc; }\r\n \r\n.wrap          { width:960px;margin:0 auto; }\r\n \r\n.img-left      { float:left;margin:4px 10px 4px 0; }\r\n.img-right     { float:right;margin:4px 0 4px 10px; }\r\n \r\n.nopadding     { padding:0; }\r\n.noindent      { margin-left:0;padding-left:0; }\r\n.nobullet      { list-style:none;list-style-image:none; }",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["css", "stylesheet", "html", "template", "code"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Convert IPv6 Address to IP numbers",
    language = "csharp",
    content = "/// <summary>\r\n/// Convert IPV6 Address to IP Number\r\n/// Free geolocation database can be downloaded at:\r\n/// http://lite.ip2location.com/\r\n/// </summary>\r\n \r\nstring strIP = \"2404:6800:4001:805::1006\";\r\nSystem.Net.IPAddress address;\r\nSystem.Numerics.BigInteger ipnum;\r\n \r\nif (System.Net.IPAddress.TryParse(strIP, out address)) {\r\nbyte[] addrBytes = address.GetAddressBytes();\r\n \r\nif (System.BitConverter.IsLittleEndian) {\r\nSystem.Collections.Generic.List<byte> byteList = new System.Collections.Generic.List<byte>(addrBytes);\r\nbyteList.Reverse();\r\naddrBytes = byteList.ToArray();\r\n}\r\n \r\nif (addrBytes.Length > 8) {\r\n//IPv6\r\nipnum = System.BitConverter.ToUInt64(addrBytes, 8);\r\nipnum <<= 64;\r\nipnum += System.BitConverter.ToUInt64(addrBytes, 0);\r\n} else {\r\n//IPv4\r\nipnum = System.BitConverter.ToUInt32(addrBytes, 0);\r\n}\r\n}",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["csharp", "ipv6", "ip numbers", "address", "web"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Smooth scrolling for internal links",
    language = "javascript",
    content = "\r\n\r\n$('a[href^=\"#\"]').bind('click.smoothscroll',function (e) {\r\n    e.preventDefault();\r\n \r\n    var anchor = this.hash,\r\n        $target = $(target);\r\n \r\n    $('html, body').stop().animate({\r\n        'scrollTop': $target.offset().top\r\n    }, 500, 'swing', function () {\r\n        window.location.hash = anchor;\r\n    });\r\n \r\n});",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["javascript", "jquery", "scrolling", "link", "js"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Getting random objects from a queryset in Django",
    language = "python",
    content = "\r\n\"\"\"\r\nWhen providing related or suggested info to the user in a website, it's a common\r\npractice to obtain a random set of items. To do this in django the \"usual\" way is:\r\n\"\"\"\r\n \r\nBook.objects.all().order_by('?')[:10]\r\n\r\n\"\"\"\r\nThe above code, sorts all books in a random order and then picks the first 10 objects. \r\nThis approach is not really efficient en MySQL. Since the \"ORDER BY ?\" clause is really expensive. \r\nSo, a good way to obtain random elements (actually a random slice) is the following:\r\n\"\"\"\r\n\r\nimport random\r\ncount = Book.objects.all().count()\r\nslice = random.random() * (count - 10)\r\nBook.objects.all()[slice: slice+10]",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["python", "django", "query", "db", "database"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Splitting up Models in Django",
    language = "python",
    content = "# 1. Create a models folder under myApp.\r\n \r\n# 2. Delete models.py and add a model_name.py file in the models folder for each model model_name.\r\n \r\n# 3. Add the following to each model file :\r\n \r\nclass Meta: \r\n    app_label = 'myApp'    \r\n \r\n# 4. Add a line in models/_init__.py_ for each model file :\r\n \r\nfrom myModelFile import myModel",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["python", "django", "py", "db", "web", "dev", "programming"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Singleton pattern for C#",
    language = "csharp",
    content = "// Singleton pattern for C# 4.0 or above.\r\n\r\npublic sealed class Singleton\r\n {\r\n     private static readonly Lazy<Singleton> lazy =\r\n         new Lazy<Singleton>(() => new Singleton());\r\n \r\n     public static Singleton Instance { get { return lazy.Value; } }\r\n \r\n     private Singleton()\r\n     {\r\n     }\r\n }",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["csharp", "web", "windows", "microsoft", "js"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Make Table from Json Data",
    language = "html",
    content = "<!DOCTYPE html>\r\n<html ng-app=\"tableJson\">\r\n<head >\r\n<link href=\"//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css\" rel=\"stylesheet\">\r\n<!--<script src=\"../angular.1.2.14.min.js\"></script>-->\r\n<script src=\"//ajax.googleapis.com/ajax/libs/angularjs/1.2.19/angular.min.js\"></script>\r\n  <title>Angular Framework</title>\r\n \r\n</head>\r\n<body>\r\n<div ng-controller=\"tableJsonCtrl\">\r\n<table border=\"1\" cellpadding=\"10\">\r\n<tr ng-repeat=\"items in phones\">\r\n  <td>{{items.name}}</td>\r\n  <td>{{items.snippet}}</td>\r\n  <td>{{items.age}}</td>\r\n</tr>\r\n</table>\r\n</div>\r\n<script>\r\nvar tableJson =  angular.module('tableJson', []);\r\n    tableJson.controller('tableJsonCtrl', function($scope){\r\n    $scope.phones = [\r\n    {   \"name\": \"Nexus S\",\r\n        \"snippet\": \"Fast just got faster with Nexus S.\",\r\n        \"age\": 0\r\n    },\r\n    {   \"name\": \"Apple iPhone 4S (White) (8 GB)\",\r\n        \"snippet\": \"3.5 Inch Widescreen Diagonal\",\r\n        \"age\": 1\r\n    },\r\n    {   \"name\": \"Samsung Galaxy Core 2 (White)\",\r\n        \"snippet\": \"powerful 1.2 GHz Quad Core processor and Android 4.4 Kitkat Operating System\",\r\n        \"age\": 2\r\n    },\r\n    {\r\n        \"name\": \"Micromax Canvas HD Plus A190, white gold\",\r\n        \"snippet\": \"4.76 GB for mass storage\",\r\n        \"age\": 2\r\n    }\r\n    ];\r\n \r\n    })\r\n</script>\r\n<script src=\"//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js\"></script>\r\n</body>\r\n \r\n</html>",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["angular", "angularjs", "js", "javascript", "html", "json"],
    date = randomDate()
  )
  
  makeSnippet(
    author = randomUser(),
    title = "Last.fm Simple API Example",
    language = "python",
    content = "import urllib, urllib2\r\ntry:\r\n    import json\r\nexcept ImportError:\r\n    import simplejson as json\r\n \r\nclass LastFM:\r\n    def __init__(self ):\r\n        self.API_URL = \"http://ws.audioscrobbler.com/2.0/\"\r\n        self.API_KEY = \"API_KEY_FROM_LAST_FM\"\r\n \r\n    def get_genre(self, genre, **kwargs):\r\n        kwargs.update({\r\n            \"method\":\t\"tag.gettopartists\",\r\n            \"tag\":\t\tgenre,\r\n            \"api_key\":\tself.API_KEY,\r\n            \"limit\":\t3,\r\n            \"format\":\t\"json\"\r\n        })\r\n        try:\r\n            # Create an API Request\r\n            url = self.API_URL + \"?\" + urllib.urlencode(kwargs)\r\n            # Send Request and Collect it\r\n            data = urllib2.urlopen( url )\r\n            # Print it\r\n            response_data = json.load( data )\r\n            print response_data['topartists']['artist'][0]['name']\r\n            # Close connection\r\n            data.close()\r\n        except urllib2.HTTPError, e:\r\n            print \"HTTP error: %d\" % e.code\r\n        except urllib2.URLError, e:\r\n            print \"Network error: %s\" % e.reason.args[1]\r\n \r\ndef main():\r\n    last_request = LastFM()\r\n    last_request.get_genre( \"rock\" )\r\n \r\nif __name__ == \"__main__\":\r\n    main()\r\n",
    visibility = "public",
    url_code = randomUrl(),
    tags = ["python", "api", "last", "key", "py", "web", "dev"],
    date = randomDate()
  )

if __name__ == "__main__":
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
  django.setup()
  from snippet.models import Snippet, SnippetExtras
  from django.contrib.auth import get_user_model
  
  if 'x' in sys.argv[1:]:
    print "Clearing database...\n"
    endall()
  
  main()

