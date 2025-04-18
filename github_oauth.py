import requests
from flask import Flask, request
import webbrowser
import threading
from github_utils import get_github_user
import creds

CLIENT_ID = 'Ov23lio2QJcy8fttrwfY'
CLIENT_SECRET = creds.client_s
REDIRECT_URI = 'http://localhost:5000/callback'
TOKEN = None

app = Flask(__name__)

@app.route('/callback')
def callback():
    global TOKEN
    global LoggedIn
    code = request.args.get('code')
    res = requests.post('https://github.com/login/oauth/access_token', headers={
        'Accept': 'application/json'
    }, data={
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'redirect_uri': REDIRECT_URI
    })

    TOKEN = res.json().get('access_token')
    print("✅ GitHub Token received:", TOKEN)
    print(get_github_user(TOKEN))
    return "You are now logged in. You can close this window."

def github_login():
    threading.Thread(target=lambda: app.run(port=5000, debug=False)).start()
    webbrowser.open(f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}")
