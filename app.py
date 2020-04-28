from flask import Flask

app = Flask(__name__)
app.secret_key = "secretkey"


@app.route("/")
def goto():
    return "hello world"
