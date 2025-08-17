from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/agenda")
def agenda():
    return render_template("agenda.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/cello_classroom")
def cello_classroom():
    return render_template("cello_classroom.html")

if __name__ == '__main__':
    app.run(use_reloader=True)

