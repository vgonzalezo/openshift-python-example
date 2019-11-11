from flask import Flask, render_template, request, redirect, Response, send_from_directory
from test_tsoft import main_tsoft_1, main_tsoft_2
import os
import json
app = Flask(__name__)
path = os.getcwd()

paginas = ["Bienvenido","a","descargar"]
@app.route("/", methods=['POST', 'GET'])
@app.route("/home", methods=['POST', 'GET'])
def home():  
    if request.method == "POST":
        data = request.form.getlist("data[]")
        if data[0] == '1':
            main_tsoft_1(path,data[1])
        else:
            pass
            main_tsoft_2(path,data[2])
    return render_template("home.html", filiales=paginas)

@app.route('/uploads/<path:filename>')
def download(filename):
    return send_from_directory(directory='output', filename=filename,as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)