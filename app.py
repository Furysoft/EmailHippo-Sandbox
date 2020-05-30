from flask import Flask
import json;

app = Flask(__name__)


if __name__ == '__main__':
    app.run()


@app.route('/')
def index():
    return app.send_static_file("index.html")


@app.route("/test")
def test():
    return {"key": "value"}, 200


@app.route("/v3/more/json/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ok.email@test.com")
def ok():
    with open('data/ok.json') as json_data:
        data = json.load(json_data)
        return data


@app.route("/v3/more/json/baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/<path:path>")
def bad_key(path):
    return "Invalid license key. Reason:Invalid key", 401


@app.route("/v3/more/json/caaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/<path:path>")
def insufficient_quota(path):
    return "Invalid license key. Reason:Insufficient quota", 401
