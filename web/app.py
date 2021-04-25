"""
Liam Dauphinee's Flask API.
"""

from flask import Flask, render_template, send_from_directory, request, abort

app = Flask(__name__)

@app.route("/<path:f_name>")
def send_file(f_name):
    symbols_403 = ['~', '..', '//']
    if (symbols_403[0] in f_name) or (symbols_403[1] in f_name) or (symbols_403[2] in f_name):
        abort(403)
    else:
       try:
           return send_from_directory('pages', f_name), 200
       except:
           abort(404)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
