from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "secretkey"


@app.route("/")
def goto():
    return render_template("index.html")
