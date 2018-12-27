#!/usr/bin/env python
import sys, os, time
from pathlib import Path

print("""
.▄▄ ·  ▄▄▄·▄• ▄▌·▄▄▄▄•    ▄▄▄▄· ▄▄▌         ▄▄ •      ▄▄ • ▄▄▄ . ▐ ▄ 
▐█ ▀. ▐█ ▄██▪██▌▪▀·.█▌    ▐█ ▀█▪██•  ▪     ▐█ ▀ ▪    ▐█ ▀ ▪▀▄.▀·•█▌▐█
▄▀▀▀█▄ ██▀·█▌▐█▌▄█▀▀▀•    ▐█▀▀█▄██▪   ▄█▀▄ ▄█ ▀█▄    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌
▐█▄▪▐█▐█▪·•▐█▄█▌█▌▪▄█▀    ██▄▪▐█▐█▌▐▌▐█▌.▐▌▐█▄▪▐█    ▐█▄▪▐█▐█▄▄▌██▐█▌
 ▀▀▀▀ .▀    ▀▀▀ ·▀▀▀ •    ·▀▀▀▀ .▀▀▀  ▀█▄▀▪·▀▀▀▀     ·▀▀▀▀  ▀▀▀ ▀▀ █▪
        [ Interactive Shell for Generating SPUZ Blog Content ]
""")

filename = input("[*] Enter blog post filename: ") + '.html'
if (Path(filename).is_file()):
    print("[*] ERROR: File already exists!")
    option = 5
else:
    file = open(filename, 'a')
    stage = 0
    option = 0
while(Path(filename).is_file() and option != 5):
    try:
        print("[*] ----- STAGE ONE -----")
        print("[1] Insert <TITLE> Info")
        print("[2] Enter HEADER Title")
        print("[3] Enter AUTHOR Info")
        print("[4] Insert Primary Image")
        print("[5] Quit Blog Generator")
        print("[*] ---------------------")
        option = int(input("[*] Enter Selection #: "))
        if not (1 <= option <= 5):
            raise ValueError()
    except ValueError:
        print("[*] WARNING: Invalid Option %d! (1-5)" % option)
    else:
        


        if(stage == 5):
            init1 = """
<!DOCTYPE html>
<html lang="en">

<head>
<!----Google Analytics---->	
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-115535331-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-115535331-1');
</script>

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({
          google_ad_client: "ca-pub-8088146909281544",
          enable_page_level_ads: true
     });
</script>
<!------------------------>

	<link rel="icon" type="image/png" href="./img/main/favicon-32x32.png" sizes="32x32" />
	<link rel="icon" type="image/png" href="./img/main/favicon-16x16.png" sizes="16x16" />
	
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>SPUZ : 
        """
            file.write(init1)