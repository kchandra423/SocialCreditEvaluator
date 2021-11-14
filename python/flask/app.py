from flask import Flask, render_template, url_for, request
import os
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    username = request.form['username']
    print(username)
    return username
if __name__ == "__main__":
    app.run(debug=True)
