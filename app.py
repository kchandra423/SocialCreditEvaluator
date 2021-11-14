from flask import Flask, render_template, request

import analyzer

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/request', methods=['POST'])
def my_form_post():
    username = request.form['username']
    credit = analyzer.analyze(username)

    if (credit >= 500):
        return f"Kumar approves the score {credit} for {username}.<img src='https://avatars.githubusercontent.com/{username}', width = '100px', height = 'auto'> \n <img src='https://cloud-ew8i9hhs9-hack-club-bot.vercel.app/0image_from_ios.jpg', width = '100px', height = 'auto'>"
    else:
        return f"Kumar does not approve the score {credit} for {username}.<img src='https://avatars.githubusercontent.com/{username}', width = '100px', height = 'auto'> \n <img src='https://cloud-6sg94z1h0-hack-club-bot.vercel.app/0image_from_ios.jpg', width = '100px', height = 'auto'>"


if __name__ == "__main__":
    app.run(debug=True)
