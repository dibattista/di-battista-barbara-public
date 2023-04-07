this_file = "venv/bin/activate_this.py"
exec(open(this_file).read(), {'__file__': this_file})

from flask import Flask, render_template, send_file

application = Flask(__name__, static_url_path='/static')

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/projets')
def projets():
    return render_template('projets.html')

@application.route('/privacy')
def privacy():
    return render_template('privacy.html')

# Download route
@application.route('/download')
def download():
    path = 'static/files/CV-BDB.pdf'
    return send_file(path, as_attachment=True)