"""
Liam Dauphinee's Flask API.
"""

from flask import Flask, render_template, send_from_directory, abort
import config    # Configure from .ini files and command line

app = Flask(__name__)

@app.route("/<path:f_name>")
def send_file(f_name):
    symbols_403 = ['~', '..', '//']
    options = config.configuration()
    path = options.DOCROOT  # path points to DOCROOT in credential.ini
    for s in symbols_403:
        if s in f_name:
            abort(403)
    return send_from_directory(path, f_name)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
