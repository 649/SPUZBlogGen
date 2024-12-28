#!/usr/bin/env python
import re
import random
import json
import sys, os
from datetime import datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

WORK_DIR = '../spuz.me/blog/zine/'

print(
    f"""
.▄▄ ·  ▄▄▄·▄• ▄▌·▄▄▄▄•    ▄▄▄▄· ▄▄▌         ▄▄ •      ▄▄ • ▄▄▄ . ▐ ▄ 
▐█ ▀. ▐█ ▄██▪██▌▪▀·.█▌    ▐█ ▀█▪██•  ▪     ▐█ ▀ ▪    ▐█ ▀ ▪▀▄.▀·•█▌▐█
▄▀▀▀█▄ ██▀·█▌▐█▌▄█▀▀▀•    ▐█▀▀█▄██▪   ▄█▀▄ ▄█ ▀█▄    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌
▐█▄▪▐█▐█▪·•▐█▄█▌█▌▪▄█▀    ██▄▪▐█▐█▌▐▌▐█▌.▐▌▐█▄▪▐█    ▐█▄▪▐█▐█▄▄▌██▐█▌
 ▀▀▀▀ .▀    ▀▀▀ ·▀▀▀ •    ·▀▀▀▀ .▀▀▀  ▀█▄▀▪·▀▀▀▀     ·▀▀▀▀  ▀▀▀ ▀▀ █▪
        [ Interactive Shell for Generating SPUZ Blog Content ]
        [ CURRENT WORK DIR: {WORK_DIR} ]
"""
)

class word:
    start = 0
    end = 0
    wrd = "null"

def bitwise(text):
    n = []
    result = re.finditer(r"\{(\b(?:[^}]+)\|?\b)+\}", text, re.MULTILINE)
    for xnum, x in enumerate(result, start=1):
        res = re.split("\|", x.group(1))
        obj = word()
        obj.start = x.start()
        obj.end = x.end()
        obj.wrd = random.choice(res)
        n.insert(xnum, obj)
    sum = 0
    insrt = 0
    for x in n:
        x.start = x.start - sum + insrt
        x.end = x.end - sum + insrt
        text = text[: x.start] + x.wrd + text[x.end :]
        sum += x.end - x.start
        insrt += len(x.wrd)
    return text

def save_draft(filename, data):
    draft_data.update(data)
    with open(WORK_DIR + filename, "w") as draft_file:
        json.dump(draft_data, draft_file)
    print(f"[*] Draft saved to {filename}")

def load_draft(filename):
    if Path(WORK_DIR + filename).is_file():
        with open(WORK_DIR + filename, "r") as draft_file:
            data = json.load(draft_file)
        print(f"[*] Draft loaded from {filename}")
        return data
    return {}

filename = input("[*] Enter blog post filename: ")
draft_filename = filename + ".json"
draft_data = load_draft(draft_filename)
filename += ".html"

if Path(WORK_DIR + filename).is_file():
    quit_now = input("[*] File already exists, quit? <Y/n>: ").lower()
    if quit_now != "n":
        exit()

stage = draft_data.get("stage", 0)
option = draft_data.get("option", 0)
content = draft_data.get("content", [])

# Prompt for title and description only if not loaded from draft
titlecard = draft_data.get("titlecard", 0)
if titlecard == 0:
    titlecard = input("[*] Enter blog post title: ")

desccard = draft_data.get("desccard", 0)
if desccard == 0:
    desccard = input("[*] Enter blog post description: ")

# Initialize variables for various stages
titlelvl = draft_data.get("titlelvl", 0)
headerlvl = draft_data.get("headerlvl", 0)
authorlvl = draft_data.get("authorlvl", 0)
primaryimglvl = draft_data.get("primaryimglvl", 0)
primaryimagecardlvl = draft_data.get("primaryimagecardlvl", 0)
primaryimagecard = draft_data.get("primaryimagecardlvl", 'null')

while primaryimagecardlvl == 0 and Path(WORK_DIR + f"img/nails/{primaryimagecard}").is_file() == False:
    primaryimagecard = input("[*] Enter blog post image (pix*.png): ")
    if Path(WORK_DIR + f"img/nails/{primaryimagecard}").is_file():
        primaryimagecardlvl = 1
    else:
        print("[*] WARNING: Image Filepath not Valid!")

print("")

current_state = {
                    'filename': filename,
                    'titlecard': titlecard,
                    'desccard': desccard,
                    'stage': stage,
                    'option': option,
                    'content': content,
                    'titlelvl': titlelvl,
                    'headerlvl': headerlvl,
                    'authorlvl': authorlvl,
                    'primaryimglvl': primaryimglvl,
                    'primaryimagecardlvl': primaryimagecardlvl,
                    'primaryimagecard': primaryimagecard
                }
save_draft(draft_filename, current_state)

while option != 5:
    if stage == 0:
        try:
            print("[*] ----- STAGE ONE -----")
            if titlelvl == 0:
                print("[1] Insert <TITLE> Info")
            else:
                print("[+] Insert <TITLE> Info")
            if headerlvl == 0:
                print("[2] Enter HEADER Title")
            else:
                print("[+] Enter HEADER Title")
            if authorlvl == 0:
                print("[3] Enter AUTHOR Info")
            else:
                print("[+] Enter AUTHOR Info")
            if primaryimglvl == 0:
                print("[4] Insert Primary Image")
            else:
                print("[+] Insert Primary Image")
            print("[5] Save and Quit Blog Generator")
            print("[*] ---------------------")
            print("")
            option = int(input("[*] Enter Selection #: "))
            save_draft(draft_filename, {'option': option})
            print("")
            if not (1 <= option <= 5):
                raise ValueError()
        except ValueError:
            print(f"[*] WARNING: Invalid Option {option}! (1-5)")
            print("")
        else:
            if option == 1:
                title = input("[*] Insert <TITLE> Info: ")
                print("")
                titlelvl = 1
                save_draft(draft_filename, {'title': title, 'titlelvl': titlelvl})
            elif option == 2:
                header = input("[*] Enter HEADER Title: ")
                print("")
                headerlvl = 1
                save_draft(draft_filename, {'header': header, 'headerlvl': headerlvl})
            elif option == 3:
                authorname = input("[*] Enter Author Name: ")
                authorlink = input("[*] Insert Author X Username: ")
                twitterusername = authorlink
                authorlink = "https://x.com/" + authorlink
                print("")
                authorlvl = 1
                save_draft(draft_filename, {'authorname': authorname, 'authorlink': authorlink, 'twitterusername': twitterusername, 'authorlvl': authorlvl})
            elif option == 4:
                while primaryimglvl == 0:
                    primaryimage = input("[*] Insert Primary Image FULL Filename: ")
                    print("")
                    if Path(WORK_DIR + f"img/{primaryimage}").is_file():
                        primaryimage = (
                            '<hr><img class="img-responsive" src="./img/'
                            + primaryimage
                            + '" alt=""><hr>'
                        )
                        primaryimglvl = 1
                    else:
                        print("[*] WARNING: Image Filepath not Valid!")
                        print("")
                save_draft(draft_filename, {'primaryimglvl': primaryimglvl, 'primaryimage': primaryimage})
            if (
                titlelvl == 1
                and headerlvl == 1
                and authorlvl == 1
                and primaryimglvl == 1
            ):
                stage += 1
                save_draft(draft_filename, {'stage': stage})
    elif stage == 1:
        try:
            print("[*] ----- STAGE TWO -----")
            print("[1] Insert SUB HEADER")
            print("[2] Insert PARAGRAPH")
            print("[3] Insert NEW IMAGE")
            print("[4] Insert NEW VIDEO")
            print("[5] Save and Quit Blog Generator")
            print("[6] Finalize Blog Post")
            print("[*] ---------------------")
            print("")
            option = int(input("[*] Enter Selection #: "))
            save_draft(draft_filename, {'option': option})
            print("")
            if not (1 <= option <= 6):
                raise ValueError()
        except ValueError:
            print(f"[*] WARNING: Invalid Option {option}! (1-6)")
            print("")
        else:
            if option == 1:
                tempsubheader = input("[*] Insert new SUB HEADER: ")
                print("")
                tempsubheader = '<p class="lead">' + tempsubheader + "</p>"
                content.append(tempsubheader)
            elif option == 2:
                tempparagraph = input("[*] Insert new PARAGRAPH: \n\n")
                print("")
                tempparagraph = "<p>" + bitwise(tempparagraph) + "</p>"
                content.append(tempparagraph)
            elif option == 3:
                imglvl = 0
                while imglvl == 0:
                    tempimage = input("[*] Insert Image FULL Filename: ")
                    print("")
                    if Path(WORK_DIR + f"img/{tempimage}").is_file():
                        imglvl = 1
                        tempimage = (
                            '<hr><img class="img-responsive" src="./img/'
                            + tempimage
                            + '" alt=""><hr>'
                        )
                        content.append(tempimage)
                    else:
                        print("[*] WARNING: Image Filepath not Valid!")
                        print("")
            elif option == 4:
                tempvideo = input("[*] Insert new Video YouTube ID: ")
                tempvideo = f"https://www.youtube.com/embed/{tempvideo}"
                print("")
                tempvideo = (
                    '<hr><iframe width="100%" height="422" src="'
                    + tempvideo
                    + '" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe><hr>'
                )
                content.append(tempvideo)
            elif option == 5:
                justincase = input("[*] Are you sure you want to save and quit? <y/N>: ").lower()
                if justincase == "y":
                    save_draft(draft_filename, draft_data)
                    break
                elif justincase == "n":
                    option = 0
            elif option == 6:
                # Define the folder where your template is located
                template_folder = './'  # Change this to the folder containing your template
                env = Environment(loader=FileSystemLoader(template_folder))

                # Load the template file
                template = env.get_template('template.html')

                # Define the variables to inject into the template
                now = datetime.now()
                formatted_date = now.strftime("%B %d, %Y at %I:%M %p")

                variables = {
                    'twitterusername': twitterusername,
                    'filename': filename,
                    'titlecard': titlecard,
                    'desccard': desccard,
                    'primaryimagecard': primaryimagecard,
                    'title': title,
                    'header' : header,
                    'authorlink': authorlink,
                    'authorname': authorname,
                    'formatted_date': formatted_date,
                    'primaryimage': primaryimage,
                    'all_content': all_content,
                    'content': content
                }
                save_draft(draft_filename, variables)

                # Render the template with the variables
                output_html = template.render(variables)
                with open(WORK_DIR + filename, "w") as file:  # will overwrite file
                    file.write(output_html)
                print("[*] Blog Post READY for Upload!")
                break
            all_content = ''
            i = 0
            while i < len(content):
                all_content += content[i]
                i += 1
            save_draft(draft_filename, {'all_content': all_content, 'content': content})
