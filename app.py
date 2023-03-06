# app.py
from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
from module import check
# from module import imageQuality
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key = "secret key"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_link():
    res = check('link')
    return render_template('index.html', res)


if __name__ == "__main__":
    app.debug = True
    app.run()
