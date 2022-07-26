from flask import Flask

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    try:
        return "this is testing app.py"
    except Exception as e:
        raise e


if __name__== "__main__":
    app.run(debug=True)