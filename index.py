from flask import Flask, request, redirect, url_for, send_from_directory, jsonify
from werkzeug import secure_filename
import os

app = Flask(__name__, static_folder='public', static_url_path='')

UPLOAD_FOLDER = 'public'

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return jsonify({'result': 'ok'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
