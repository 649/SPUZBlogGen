#!/usr/bin/env python
import sys, os, datetime
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
                init = """
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
                file.write(init)
                file.write(title)
                init = """
</title>

    <!-- Bootstrap Core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/blog-post.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>

    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="./../../index.html">SPUZ</a>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li>
                        <a href="./../index.html">Blog</a>
                    </li>
                    <li>
                        <a href="./../../archive/index.html">Archive</a>
                    </li>
					<li>
						<a href="./../../paper/index.html">White Papers</a>
					</li>
					<li>
						<a href="./../../video/index.html">Video Portal</a>
					</li>
                    <li>
                        <a href="./../../about/index.html">About</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

    <!-- Page Content -->
    <div class="container">

        <div class="row">

            <!-- Blog Post Content Column -->
            <div class="col-lg-8">

                <!-- Blog Post -->

                <!-- Title -->
                <h1><b>
                """
                file.write(init)
                file.write(header)
                init = """
</b></h1>

                <!-- Author -->
                <p class="lead">
                    by <a href="
                """
                file.write(init)
                file.write(authorlink)
                file.write('">')
                file.write(authorname)
                init = """
</a>
                </p>

                <hr>

                <!-- Date/Time -->
                <p><span class="glyphicon glyphicon-time"></span> Posted on 
                """
                file.write(init)
                now = datetime.datetime.now()
                if(now.hour >= 12):
                    period = 'PM'
                    hour = now.hour - 12
                else:
                    period = 'AM'
                    hour = now.hour
                if(now.month == 1):
                    month = 'January'
                elif(now.month == 2):
                    month = 'February'
                elif(now.month == 3):
                    month = 'March'
                elif(now.month == 4):
                    month = 'April'
                elif(now.month == 5):
                    month = 'May'
                elif(now.month == 6):
                    month = 'June'
                elif(now.month == 7):
                    month = 'July'
                elif(now.month == 8):
                    month = 'August'
                elif(now.month == 9):
                    month = 'September'
                elif(now.month == 10):
                    month = 'October'
                elif(now.month == 11):
                    month = 'November'
                elif(now.month == 12):
                    month = 'December'
                now = month + " " + str(now.day) + ", " + str(now.year) + " at " + str(hour) + ":" + str(now.minute) + " " + period
                file.write(now)
                init = """
</p>

                <hr>

                <!-- Preview Image -->
                <img class="img-responsive" src="./img/
                """
                file.write(init)
                file.write(primaryimage)
                init = """
" alt="">

                <hr>
                """
                file.write(init)

                i = 0
                while(i < len(content)):
                    file.write(content[i])

                init = """
<hr>
				
			<!-- Comments Section -->
			<a class="twitter-timeline" data-dnt="true" show-replies="true" width="850" height="600" tweet-limit="10" href="https://twitter.com/hashtag/SPUZ" data-widget-id="985893656476266497">#SPUZ Tweets</a>
            <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
          
            </div>

            <!-- Blog Sidebar Widgets Column -->
            <div class="col-md-4">

                <!-- Blog Search Well -->
				<script>
					(function() {
						var cx = 'partner-pub-8088146909281544:9176712447';
						var gcse = document.createElement('script');
						gcse.type = 'text/javascript';
						gcse.async = true;
						gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
						var s = document.getElementsByTagName('script')[0];
						s.parentNode.insertBefore(gcse, s);
					})();
				</script>
                <div class="well">
                    <h4>Blog Search</h4>
					<gcse:searchbox-only></gcse:searchbox-only>
                    <!-- /.input-group -->
                </div>

                <!-- Blog Categories Well -->
                <div class="well">
                    <h4>Blog Categories</h4>
                    <div class="row">
                        <div class="col-lg-6">
                            <ul class="list-unstyled">
                                <li><a href="#">Malware</a>
                                </li>
                                <li><a href="#">Privacy</a>
                                </li>
                                <li><a href="#">Vulnerability</a>
                                </li>
                                <li><a href="#">Tools</a>
                                </li>
                            </ul>
                        </div>
                        <div class="col-lg-6">
                            <ul class="list-unstyled">
                                <li><a href="#">COMING</a>
                                </li>
                                <li><a href="#">SOON</a>
                                </li>
                                <li><a href="#">JUST</a>
                                </li>
                                <li><a href="#">WAIT</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <!-- /.row -->
                </div>

                <!-- Side Widget Well -->
                <div class="well">
			<a class="twitter-timeline" href="https://twitter.com/SPUZNIQ">Tweets by SPUZNIQ</a> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
                </div>

            </div>

        </div>
        <!-- /.row -->

        <hr>

        <!-- Footer -->
        <footer>
            <div class="row">
                <div class="col-lg-12">
                    <p>Copyright &copy; SPUZ 2016 - 2018</p>
                </div>
            </div>
            <!-- /.row -->
        </footer>

    </div>
    <!-- /.container -->

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

</body>

</html>
                """
                file.write(init)