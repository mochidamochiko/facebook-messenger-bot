# -*- coding: utf-8 -*-
# 日本語を使う場合は絶対に必要

# flaskなどの必要なライブラリをインポート
import os
from flask import Flask, request

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']

# 自分の名称を app という名前でインスタンス化
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/webhook', methods=['GET'])
def verification():
    if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):     
        print("succefully verified")
        return request.args.get('hub.challenge', '')
    else:
        print("Wrong verification token!")
        return "Wrong validation token"

@app.route('/webhook', methods=['POST'])
def getMessage():
    data = request.get_json()
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):  
                    message_text = messaging_event["message"]
                    print(message_text)

    return "echo: {}".format(message_text)


# bashで叩いたかimportで入れたかを判定する
if __name__ == '__main__':
    app.run()
