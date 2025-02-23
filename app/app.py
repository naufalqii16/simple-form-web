from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/presensi", methods=["POST"])
def presensi():
    return render_template("after-submit.html")


if __name__ == "__main__":
    app.run(debug=True)
