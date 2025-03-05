from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/new-endpoint")
def new_endpoint():
    return jsonify({"message": "This is a properly formatted response"})


if __name__ == "__main__":
    app.run(debug=True)
