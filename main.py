from datetime import datetime
import os

from flask import Flask, render_template, request, redirect, url_for, session
from passlib.hash import pbkdf2_sha256

from model import Task, User

app = Flask(__name__)


@app.route('/all')
def all_tasks():
 return render_template('all.jinja2', tasks=Task.select())

if __name__ == "__main__":
 port = int(os.environ.get("PORT", 5000))
 app.run(host='0.0.0.0', port=port)