from inspect import getfile
import json
from urllib.parse import quote
from flask import jsonify

path = './data/data.json'

def getFileContent():
    with open(path,'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def url_format(str):
    return quote(str).lower()

def findKey(collection,key):
    for name, value in collection.items():
        if url_format(name) == url_format(key):
            return value
    return None

def lookup(*keys):
    node = getFileContent()['Skoler']
    for key in keys:
        node = findKey(node,key)
        if node is None:
            return None
    return node



def getSchoolData(school):
    file = getFileContent()
    for skole in file["Skoler"]:
        if quote(school).lower() == quote(skole).lower():
            return jsonify(file["Skoler"][skole])
    return jsonify({"error": "Skolen finnes ikke i databasen."}), 40