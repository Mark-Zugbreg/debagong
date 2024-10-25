from shutil import which
from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
	return "hallo kontol"


@app.route("/ngecek", methods=["GET"]):
def asyu():
	return f"ffmpeg <h1>{str(which('ffmpeg'))}</h1>"

if __name__ == "__main__":
	app.run(debug=True)
