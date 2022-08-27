from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<name>")
def home(name):
    return render_template("index.html", content=name, r=2, contents=["tim", "joe", "bill"])


if __name__ == "__main__":
    app.run()
