from flask import Flask, request
from pyngrok import ngrok
import requests
import sys
sys.path.append('../')
import conf.settings
from cache.redis import save_chat

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def handler():
    if request.method == "POST":
        save_chat(request.get_json())
    
    return "ok"

@app.route('/set')
def webhook():
    public_url_ngrok = get_public_url("2hbUMvo6QYBQV5O8pmKlKP0G6Ze_4tZqgcM3DwsWqUsUiCxrG")

    response = requests.post(conf.settings.TELEGRAM_API_URL+ "setWebhook?url=" + public_url_ngrok).json()
    print(response)
    return "response"

def get_public_url(AUTH_TOKEN):
    ngrok.set_auth_token(AUTH_TOKEN)
    public_url = ngrok.connect(8080)
    print(f"webhook : {public_url.public_url}")
    
    return public_url

if __name__ == '__main__':
    app.run(debug=True, port="8080")