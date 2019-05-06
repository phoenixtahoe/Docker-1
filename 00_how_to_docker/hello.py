from flask import Flask
app = Flask(_name_)

@app.route("/")
def hello():
	return "<h1>Hello World</h1>"
