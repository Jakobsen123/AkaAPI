from flask import Flask, render_template
from lib.json import getFileContent,getSchoolData

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dokumentasjon')
def doc_page():
    return render_template('doc.html')

@app.route('/api/')
def api_root():
    return getFileContent()

# skoler 

@app.route('/api/skole/')
def api_school_all():
    return getFileContent()["Skoler"]
@app.route('/api/skole/<school>')
def api_school(school):
    return getSchoolData(school)

# elever og ansatte




if __name__ == '__main__':
    app.run(debug=True)
