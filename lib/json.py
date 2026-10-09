import json

path = './data/data.json'

def getFileContent():
    with open(path,'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
