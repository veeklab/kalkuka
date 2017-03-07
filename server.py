#/usr/bin/python
# server kalkuka

from flask import (
	Flask,
	request,
	render_template,
	redirect
	)


# include library

from lib.coulumb import fc
from lib.kapasitansi import c


app = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/coulumb', methods=['POST'])
def handle_post():
	if request.method == 'POST':
		q1 = int(request.form['q1'])
		q2 = int(request.form['q2'])
		r = int(request.form['r'])

		if q1 is not None and q2 is not None and r is not None:
			res = fc(q1, q2, r)
			return render_template("index.html", res=res)
	return redirect(url_for('index', 302))


