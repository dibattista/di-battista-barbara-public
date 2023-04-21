from flask import Flask, render_template, send_file, request, send_from_directory

application = Flask(__name__, static_folder='static', static_url_path='')

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
    path = 'static/files/CV.pdf'
    return send_file(path, as_attachment=True)

#SEO
@application.route('/robots.txt')
def static_from_root():
    return send_from_directory(application.static_folder, request.path[1:])
