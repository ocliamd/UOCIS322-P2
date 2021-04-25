"""
Liam Dauphinee's Flask API.
"""

from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

@app.route("/trivia")
def send_file():
    #return redirect(url_for('forbidden'))
    return send_from_directory('pages', 'trivia.css'), 200
    return send_from_directory('pages', 'trivia.html'), 200
    '''if __name__ == '/trivia.html':
        print("True *****")
        return send_from_directory('pages', 'trivia.html'), 200
    else:
        print('False')
        return "No input file specified"'''


    '''if 'filename' in request.args:
        myfilename = request.args.get('filename')
        return send_from_directory('pages', name), 200
    else:
        print('')
        return "No input file specified"'''

    #if ('//' in parts[1]) or ('~' in parts[1]) or ('..' in parts[1]):
    # check for forbidden characters

    #return "UOCIS docker demo - test using PORT from app.ini!\n"
    #return send_from_directory(path, 'trivia.html'), 200

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
