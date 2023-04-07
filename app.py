from flask import Flask, render_template, send_file

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projets')
def projets():
    return render_template('projets.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

# Download route
@app.route('/download')
def download():
    path = 'static/files/CV-BDB.pdf'
    return send_file(path, as_attachment=True)