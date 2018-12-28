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

titlelvl = 0
headerlvl = 0
authorlvl = 0
primaryimglvl = 0
content = []
while(Path(filename).is_file() and option != 5):
    if(stage == 0):
        try:
            print("[*] ----- STAGE ONE -----")
            print("[1] Insert <TITLE> Info")
            print("[2] Enter HEADER Title")
            print("[3] Enter AUTHOR Info")
            print("[4] Insert Primary Image")
            print("[5] Quit Blog Generator")
            print("[*] ---------------------")
            print("")
            option = int(input("[*] Enter Selection #: "))
            print("")
            if not (1 <= option <= 5):
                raise ValueError()
        except ValueError:
            print("[*] WARNING: Invalid Option %d! (1-5)" % option)
            print("")
        else:
            if(option == 1):
                title = input("[*] Insert <TITLE> Info: ")
                print("")
                titlelvl = 1
            elif(option == 2):
                header = input("[*] Enter HEADER Title: ")
                print("")
                headerlvl = 1
            elif(option == 3):
                authorname = input("[*] Enter Author Name: ")
                authorlink = input("[*] Insert Author URL: ")
                print("")
                authorlvl = 1
            elif(option == 4):
                while(primaryimglvl == 0):
                    primaryimage = input("[*] Insert Primary Image FULL Filename: ")
                    print("")
                    if (Path("./img/%s" % primaryimage).is_file()):
                        primaryimglvl = 1
                    else:
                        print("[*] WARNING: Image Filepath not Valid!")
                        print("")
            if(titlelvl == 1 and headerlvl == 1 and authorlvl == 1 and primarylvl == 1):
                stage+=1
    elif(stage == 1):
        try:
            print("[*] ----- STAGE TWO -----")
            print("[1] Insert SUB HEADER")
            print("[2] Insert PARAGRAPH")
            print("[3] Insert NEW IMAGE")
            print("[4] Insert NEW VIDEO")
            print("[5] Quit Blog Generator")
            print("[6] Finalize Blog Post")
            print("[*] ---------------------")
            print("")
            option = int(input("[*] Enter Selection #: "))
            print("")
            if not (1 <= option <= 6):
               raise ValueError()
        except ValueError:
            print("[*] WARNING: Invalid Option %d! (1-6)" % option)
            print("")
        else:
            if(option == 1):
                tempsubheader = input("[*] Insert new SUB HEADER: ")
                print("")
                tempsubheader = '<p class="lead">' + tempsubheader + '</p>'
                content.append(tempsubheader)
            elif(option == 2):
                tempparagraph = input("[*] Insert new PARAGRAPH: \n\n")
                print("")
                tempparagraph = '<p>' + tempparagraph + '</p>'
                content.append(tempparagraph)
            elif(option == 3):
                imglvl = 0
                while(imglvl == 0):
                    tempimage = input("[*] Insert Image FULL Filename: ")
                    print("")
                    if (Path("./img/%s" % tempimage).is_file()):
                        imglvl = 1
                        tempimage = '<hr><img class="img-responsive" src="./img/'+ tempimage + '" alt=""><hr>'
                        content.append(tempimage)
                    else:
                        print("[*] WARNING: Image Filepath not Valid!")
                        print("")
            elif(option == 4):
                tempvideo = input("[*] Insert new Video YouTube Full URL: ")
                print("")
                tempvideo = '<hr><iframe width="100%" height="422" src="' + tempvideo + '" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe><hr>'
                content.append(tempvideo)
            elif(option == 6):


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