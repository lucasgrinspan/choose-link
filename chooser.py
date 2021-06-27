#!/usr/bin/env python3
from subprocess import check_output
import webbrowser
import json
import os

def formatList(links):
    return "\n".join(links)

def openLink(url):
    webbrowser.open(url)

def getSelection(links):
    try:
        output = check_output(f'echo "{links}" | choose -c 000088', shell=True)
        return output.decode('utf-8')
    except Exception:
        return None

def showMenu(links):
    label = getSelection(formatList(links))
    if (label is None):
        return
        
    selection = links[label]

    if type(selection) == str:
        openLink(selection)
        return
    
    # recursion :O
    return showMenu(selection)

path = os.getenv('HOME') + '/.choose-link/links.json'
links_file = open(path)
links = json.load(links_file)

showMenu(links)