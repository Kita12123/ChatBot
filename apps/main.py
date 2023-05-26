from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from pathlib import Path

app = Flask(__name__)

from apps import bot
from apps import db


def to_system_json(text):
    """システム用定義"""
    return {"role": "system", "content": str(text)}


def to_assistant_json(text):
    """AI応答"""
    return {"role": "assistant", "content": str(text)}


def to_user_json(text):
    """ユーザーリクエスト"""
    return {"role": "user", "content": str(text)}


# 初期処理（トーク履歴クリア）
history_default = [
    to_system_json("出来る限り１００文字以内で返答してください。")
]
reply = bot.request([
    *history_default,
    to_user_json("あいさつをしてください。")
])
history_default.append(to_assistant_json(reply))
db.output_history(history_default)


@app.route("/", methods=["GET", "POST"])
def index():
    history = db.input_history()
    if request.method == "POST":
        req = request.form.get("request")
        if req == "初期化":
            return render_template(
                "index.html",
                history=history_default
            )
        user_json = to_user_json(req)
        reply = bot.request([*history, user_json])
        assistant_json = to_assistant_json(reply)
        history = [
            *history,
            user_json,
            assistant_json
        ]
        db.output_history(history)
    return render_template(
        "index.html",
        history=history
    )


@app.route('/favicon.ico')
def favicon():
    return send_file(
        Path(app.root_path) / "static" / "favicon.ico"
    )
