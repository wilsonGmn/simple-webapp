import os
from flask import Flask
app = Flask(__name__)


@app.route("/")
def main():
    return "Welcome! Update A"

@app.route("/howareyou")
def hello():
    return 'Aam good, how about you ?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8585)
