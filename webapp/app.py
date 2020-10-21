from flask import Flask, jsonify
from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Environment, FileSystemLoader

import facerec

app = Flask(__name__)

@app.route('/')
def index():
    print("Face Recognition API")
    return render_template('index.html')

@app.route('/', methods=['POST'])
def validar():

    upload_path_foto = request.files['file_foto']
    upload_path_cod = request.files['file_cod']
    result = facerec.validar_aluno(upload_path_foto, upload_path_cod)
    return jsonify({'result': repr(result)})

def codificar():

    upload_path_foto = request.files['file_foto']
    result = facerec.codificar_foto(upload_path_foto)
    return jsonify({'result': repr(result)})
if __name__ == '__main__':
    app.run(host='0.0.0.0')