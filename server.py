<<<<<<< HEAD
#/usr/bin/python

=======
#server kalkuka

from flask import flask
app=Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")
>>>>>>> 8f0a6dc3af0486d5308e69dc2f49a5f260c3e7da
