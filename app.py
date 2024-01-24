from flask import Flask, render_template, request, redirect, jsonify, send_file
from flask_cors import CORS
import requests
import random

app = Flask(__name__, static_url_path='/static')
CORS(app)


@app.route('/')
def index():
    return "pare de mentir"

@app.route('/numero/<limite>')
def leatorio(limite):
    final = random.randint(int(limite)+1, 100)
    return str(final)


if __name__ == '__main__':
    app.run(debug=True)