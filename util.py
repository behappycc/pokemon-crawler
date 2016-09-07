import os
import json

def load_json(path):
    jsonFile = open(path, encoding='utf8')
    data = json.load(jsonFile)
    jsonFile.close()
    return data

def write_json(data,path):
    with open(path, "w", encoding='utf8') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)