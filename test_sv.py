from flask import Flask, session, redirect, url_for, request
from playsound import playsound
app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def hello():
    if request.method == 'GET':
        print("You are Hitted")
        playsound("kyaaaa.mp3")
        return "aaaa"

if __name__ == '__main__':
    app.run()
