
from flask import Flask, render_template, request
from index import alphabet, alphabetlower

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def index_post():
    text = request.form.get("text")
    code = ""

    for e in text:
        if e in alphabet:
            i = alphabet.index(e)
            x = alphabet[i + 3]
            code += x
        elif e in alphabetlower:
            i = alphabetlower.index(e)
            x = alphabetlower[i + 3]
            code += x
        elif e == " ":
            x = " "
            code += x

    return render_template("index.html", text=text, code=code)


if __name__ == '__main__':
    app.run()