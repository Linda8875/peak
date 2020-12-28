'''imports'''
from flask import Flask, redirect, url_for, render_template, request, session
from werkzeug.datastructures import ImmutableMultiDict
from dotenv import load_dotenv
import os
load_dotenv()


'''instance flask web application'''
app = Flask(__name__)
app.secret_key = "qsdfghjklm"

'''define pages on app'''


@app.route("/", methods=["POST","GET"])
def index():
    return render_template("index.html")


'''run app'''
if __name__ == "__main__":
    app.run(debug=False)

