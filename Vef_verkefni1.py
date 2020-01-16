from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello Heroku app</h1>\n <h5>It is currently a good day</h5>\n<a href="/sida1">Síða 1</a>\n<a href="/sida2">Síða 2</a>'
	

@app.route('/sida1')
def sida1():
	return '<h1>síða 1, nú er gaman...</h1>\n<a href="/">Heimasíða</a>'

@app.route('/sida2')
def sida2():
	return render_template("http.html")

if __name__ == "__main__":
	app.run(debug=True)
