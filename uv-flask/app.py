from flask import Flask, jsonify, request
from utils import add, subtract, to_celsius, to_fahrenheit

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"status": "ok"})


@app.route("/add")
def add_route():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    return jsonify({"result": add(a, b)})


@app.route("/subtract")
def subtract_route():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    return jsonify({"result": subtract(a, b)})


@app.route("/to_celsius")
def celsius_route():
    f = request.args.get("f", type=float)
    return jsonify({"result": to_celsius(f)})


@app.route("/to_fahrenheit")
def fahrenheit_route():
    c = request.args.get("c", type=float)
    return jsonify({"result": to_fahrenheit(c)})


if __name__ == "__main__":
    app.run(debug=True)
