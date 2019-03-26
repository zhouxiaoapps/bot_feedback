from flask import render_template

from bot_feedback import app


@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('index.html')
