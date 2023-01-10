#!/usr/bin/python3

def write_file(filename="", text=""):
    numofch = 0
    with open(filename, 'r+', encoding='utf-8') as f:
        numofch = f.write(str(text))
    return numofch
