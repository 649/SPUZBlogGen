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
file = open(filename, 'w')

option = True
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
        print("[*] Error: Invalid Option %d! (1-5)" % option)
    else:
        print("[*] Processing. . .")