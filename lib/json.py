import json
from urllib.parse import quote
from flask import jsonify

path = './data/data.json'

def getFileContent():
    with open(path,'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def getSchoolData(school):
    file = getFileContent()
    for skole in file["Skoler"]:
        if quote(school).lower() == quote(skole).lower():
            return jsonify(file["Skoler"][skole])
    return jsonify({"error": "Skolen finnes ikke i databasen."}), 404


# def getStudentOrTeacherData(role):
#     data = getFileContent()
#     for skole in data["Skoler"]:
#         for elev in skole[role]:
#             if 