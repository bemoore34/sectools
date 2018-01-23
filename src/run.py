from src.app import app

__author__ = 'bmoore'

app.run(debug=app.config['DEBUG'], port=5000)
