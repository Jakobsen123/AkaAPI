from flask import Flask, render_template, abort
from lib.json import getFileContent,lookup

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dokumentasjon')
def doc_page():
    return render_template('doc.html')

@app.route('/visualisering')
def visual_page():
    return render_template('visualisering.html')

@app.route('/api/')
def api_root():
    return getFileContent()

# skoler 

@app.route('/api/skole')
def api_school_all():
    return getFileContent()["Skoler"]
@app.route('/api/skole/<school>')
def api_school(school):
    return lookup(school) or abort(404)

# elever og ansatte

@app.route('/api/skole/<school>/ansatte')
def api_school_staff_all(school):
    return lookup(school,'Lærere') or abort(404)

@app.route('/api/skole/<school>/ansatte/<staff>')
def api_school_staff(school,staff):
    return lookup(school,"Lærere",staff) or abort(404)

@app.route('/api/skole/<school>/elever/')
def api_school_students_all(school):
    return lookup(school,"Elever") or abort(404)

@app.route('/api/skole/<school>/elever/<student>')
def api_school_students(school,student):
    return lookup(school,"Elever",student) or abort(404)

@app.errorhandler(404)
def error(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(debug=True)
