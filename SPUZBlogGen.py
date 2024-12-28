#!/usr/bin/env python
import re
import random
import json
import sys
import os
from datetime import datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

WORK_DIR = Path('../spuz.me/blog/zine/')

# If data.json lives elsewhere, adjust accordingly
DATA_JSON_PATH = WORK_DIR / '../../data.json'

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
    """
    Replaces tokens of the form {option1|option2|...} with
    a randomly chosen option. The text is processed so that
    multiple tokens can be replaced without messing up indexes.
    """
    found_tokens = re.finditer(r"\{(\b(?:[^}]+)\|?\b)+\}", text, re.MULTILINE)
    replacements = []

    # Gather all tokens and randomly choose a word from each
    for index, match in enumerate(found_tokens, start=1):
        choices = re.split(r"\|", match.group(1))
        obj = word()
        obj.start = match.start()
        obj.end = match.end()
        obj.wrd = random.choice(choices)
        replacements.insert(index, obj)

    total_removed = 0
    total_inserted = 0

    # Replace tokens in the original text
    for rep in replacements:
        # Adjust positions to account for the modifications
        rep_start = rep.start - total_removed + total_inserted
        rep_end   = rep.end - total_removed + total_inserted

        text = text[:rep_start] + rep.wrd + text[rep_end:]
        # Keep track of how many characters have been removed/inserted
        removed_len = rep_end - rep_start
        inserted_len = len(rep.wrd)
        total_removed += removed_len
        total_inserted += inserted_len

    return text

def save_draft(filename, data):
    """Updates draft_data with the given dictionary and saves to file."""
    draft_data.update(data)
    with open(WORK_DIR / filename, "w") as draft_file:
        json.dump(draft_data, draft_file)
    print(f"[*] Draft saved to {filename}")

def load_draft(filename):
    """Loads JSON draft data from file if it exists."""
    draft_path = WORK_DIR / filename
    if draft_path.is_file():
        with open(draft_path, "r") as draft_file:
            data = json.load(draft_file)
        print(f"[*] Draft loaded from {filename}")
        return data
    return {}

def file_exists(relative_path):
    """Convenience helper to check if a file exists under WORK_DIR."""
    return (WORK_DIR / relative_path).is_file()

# Main Script Flow
filename = input("[*] Enter blog post filename: ")
draft_filename = filename + ".json"
draft_data = load_draft(draft_filename)

# HTML output file
filename_html = filename + ".html"

# Prompt user if file exists
if file_exists(filename_html):
    quit_now = input("[*] File already exists, quit? <Y/n>: ").lower()
    if quit_now != "n":
        sys.exit()

# Start pulling data from draft or default
stage = draft_data.get("stage", 0)
option = 0
content = draft_data.get("content", [])

titlecard = draft_data.get("titlecard", 0)
if titlecard == 0:
    titlecard = input("[*] Enter blog post title: ")

desccard = draft_data.get("desccard", 0)
if desccard == 0:
    desccard = input("[*] Enter blog post description: ")

titlelvl = draft_data.get("titlelvl", 0)
headerlvl = draft_data.get("headerlvl", 0)
authorlvl = draft_data.get("authorlvl", 0)
primaryimglvl = draft_data.get("primaryimglvl", 0)

# This tracks the "card" image for the blog listing, separate from the post's main image
primaryimagecardlvl = draft_data.get("primaryimagecardlvl", 0)
primaryimagecard = draft_data.get("primaryimagecard", 'null')

# Prompt for a valid image file if the "card" image isn't set yet
while primaryimagecardlvl == 0 and not file_exists(f"img/nails/{primaryimagecard}"):
    primaryimagecard = input("[*] Enter blog post thumbnail image (pix*.png): ")
    if file_exists(f"img/nails/{primaryimagecard}"):
        primaryimagecardlvl = 1
    else:
        print("[*] WARNING: Image Filepath not Valid!")

print("")

# Update and save draft with current known data
current_state = {
    'filename': filename_html,
    'titlecard': titlecard,
    'desccard': desccard,
    'stage': stage,
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
            print("[1] Insert <TITLE> Info" + (" (pending)" if titlelvl == 0 else " (done)"))
            print("[2] Enter HEADER Title"  + (" (pending)" if headerlvl == 0 else " (done)"))
            print("[3] Enter AUTHOR Info"   + (" (pending)" if authorlvl == 0 else " (done)"))
            print("[4] Insert Primary Image" + (" (pending)" if primaryimglvl == 0 else " (done)"))
            print("[5] Save and Quit Blog Generator")
            print("[*] ---------------------\n")

            option = int(input("[*] Enter Selection #: "))
            print("")

            if not (1 <= option <= 5):
                raise ValueError()
        except ValueError:
            print(f"[*] WARNING: Invalid Option {option}! (1-5)\n")
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
                save_draft(draft_filename, {
                    'authorname': authorname,
                    'authorlink': authorlink,
                    'twitterusername': twitterusername,
                    'authorlvl': authorlvl
                })

            elif option == 4:
                while primaryimglvl == 0:
                    primaryimage = input("[*] Insert Primary Image FULL Filename: ")
                    print("")
                    if file_exists(f"img/{primaryimage}"):
                        primaryimage = (
                            '<hr><img class="img-responsive" src="./img/'
                            + primaryimage
                            + '" alt=""><hr>'
                        )
                        primaryimglvl = 1
                    else:
                        print("[*] WARNING: Image Filepath not Valid!\n")
                save_draft(draft_filename, {
                    'primaryimglvl': primaryimglvl,
                    'primaryimage': primaryimage
                })

            # If all required items are done, move to next stage
            if titlelvl == 1 and headerlvl == 1 and authorlvl == 1 and primaryimglvl == 1:
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
            print("[*] ---------------------\n")

            option = int(input("[*] Enter Selection #: "))
            print("")

            if not (1 <= option <= 6):
                raise ValueError()
        except ValueError:
            print(f"[*] WARNING: Invalid Option {option}! (1-6)\n")
        else:
            if option == 1:
                # Insert sub header
                tempsubheader = input("[*] Insert new SUB HEADER: ")
                print("")
                content.append('<p class="lead">' + tempsubheader + "</p>")

            elif option == 2:
                # Insert paragraph
                tempparagraph = input("[*] Insert new PARAGRAPH: \n\n")
                print("")
                content.append("<p>" + bitwise(tempparagraph) + "</p>")

            elif option == 3:
                # Insert new image
                imglvl = 0
                while imglvl == 0:
                    tempimage = input("[*] Insert Image FULL Filename: ")
                    print("")
                    if file_exists(f"img/{tempimage}"):
                        imglvl = 1
                        content.append(
                            '<hr><img class="img-responsive" src="./img/'
                            + tempimage
                            + '" alt=""><hr>'
                        )
                    else:
                        print("[*] WARNING: Image Filepath not Valid!\n")

            elif option == 4:
                # Insert new video
                tempvideo = input("[*] Insert new Video YouTube ID: ")
                tempvideo = f"https://www.youtube.com/embed/{tempvideo}"
                print("")
                content.append(
                    '<hr><iframe width="100%" height="422" src="'
                    + tempvideo
                    + '" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe><hr>'
                )

            elif option == 5:
                # Save and Quit
                justincase = input("[*] Are you sure you want to save and quit? <y/N>: ").lower()
                if justincase == "y":
                    save_draft(draft_filename, draft_data)
                    break
                elif justincase == "n":
                    option = 0  # reset so the loop continues

            elif option == 6:
                # Finalize Blog Post
                # 1) Ask for comma-delimited tags if not already saved
                tags_list = draft_data.get('tags', [])
                if not tags_list:
                    user_tags = input("[*] Enter comma-delimited tags: ")
                    tags_list = [tag.strip() for tag in user_tags.split(',') if tag.strip()]
                    # Save to draft, so we don't lose it if user restarts
                    save_draft(draft_filename, {'tags': tags_list})

                # 2) Load your template
                template_folder = './'
                env = Environment(loader=FileSystemLoader(template_folder))
                template = env.get_template('template.html')

                now = datetime.now()
                formatted_date = now.strftime("%B %d, %Y at %I:%M %p")

                # We assume these were stored in draft_data from earlier (stage 1)
                title       = draft_data.get('title', '')
                header      = draft_data.get('header', '')
                authorlink  = draft_data.get('authorlink', '')
                authorname  = draft_data.get('authorname', '')
                twitteruser = draft_data.get('twitterusername', '')
                primaryimg  = draft_data.get('primaryimage', '')

                # Convert list of tags into a single string for the blog, if needed
                all_content = ''.join(content)

                variables = {
                    'twitterusername': twitteruser,
                    'filename': filename_html,
                    'titlecard': titlecard,
                    'desccard': desccard,
                    'primaryimagecard': primaryimagecard,
                    'title': title,
                    'header': header,
                    'authorlink': authorlink,
                    'authorname': authorname,
                    'formatted_date': formatted_date,
                    'primaryimage': primaryimg,
                    'all_content': all_content,
                    'content': content
                }

                save_draft(draft_filename, variables)

                # 3) Insert a new item at the top of data.json
                #    ensuring we do not overwrite existing data, but prepend
                if DATA_JSON_PATH.is_file():
                    with open(DATA_JSON_PATH, 'r') as f:
                        data_json = json.load(f)
                else:
                    # In case data.json does not exist yet, create a skeleton
                    data_json = {"items": []}

                new_item = {
                    "imageSrc": f"/blog/zine/img/nails/{primaryimagecard}",
                    "altText": "",
                    "title": titlecard,
                    "description": desccard,
                    "link": f"/blog/zine/{filename_html}",
                    "tags": tags_list
                }
                data_json["items"].insert(0, new_item)

                # Write updated data.json
                with open(DATA_JSON_PATH, 'w') as f:
                    json.dump(data_json, f, indent=2)
                print(f"[*] data.json updated with new item at the top.")

                # 4) Render and write final HTML
                output_html = template.render(variables)
                with open(WORK_DIR / filename_html, "w") as file:
                    file.write(output_html)

                print("[*] Blog Post READY for Upload!")
                break

            # After each Stage 2 action (except finalize or forced quit), update & save
            all_content = ''.join(content)
            save_draft(draft_filename, {'all_content': all_content, 'content': content})
