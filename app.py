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
        return f"Kumar approves the social credit score {credit} for {username}<br> Bing Chilling!!!<br>" \
               f"<img src = 'https://c.tenor.com/4m1F3mnrVNEAAAAM/social-credit-social-credit-score.gif'><br>" \
               f"<img src='https://avatars.githubusercontent.com/{username}', width = '100px', height = 'auto'> " \
               f"<img src='https://cloud-ew8i9hhs9-hack-club-bot.vercel.app/0image_from_ios.jpg', width = '100px', height = 'auto'>"
    else:
        return f"Kumar does not approve the social credit score {credit} for {username}<br>" \
               f" Taiwain is not a country >:( <br>" \
               f"<img src = 'https://c.tenor.com/4_R-q6m3cZ8AAAAC/30000000social-credit-minus30000000social-credit.gif'><br>" \
               f".<img src='https://avatars.githubusercontent.com/{username}', width = '100px', height = 'auto'>" \
               f" <img src='https://cloud-6sg94z1h0-hack-club-bot.vercel.app/0image_from_ios.jpg', width = '100px', height = 'auto'>"


if __name__ == "__main__":
    app.run(debug=True)
