from flask import Flask, render_template

public = 'public'

app = Flask(__name__, template_folder=public, static_folder=public)


@app.route('/')
def index():
	return render_template('index.html')
