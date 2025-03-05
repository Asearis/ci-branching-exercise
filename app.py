from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/new-endpoint')
def bad_endpoint():
    value = "This is bad code"
    for i in range(10):  # Unused loop variable
        x = i * 2  # Unused variable
    return value  # No proper JSON response

if __name__ == "__main__":
    app.run(debug=True)
