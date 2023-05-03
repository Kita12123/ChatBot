from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask import url_for

from apps.bot import Bot

app = Flask(__name__)
bot = Bot("出来る限り１００文字以内で返答してください。")


@app.route("/", methods=["GET", "POST"])
def index():
    user_ip = request.remote_addr
    reply = "はじめまして、お好きにお話してください。"
    if request.method == "POST":
        req = request.form.get("request")
        reply = bot.chat(req).replace(
            "\n", "<br>"    # 改行
        ).replace(
            " ", "&nbsp;"   # 半角スペース
        ).replace(
            "　", "&emsp;"  # 全角スペース
        )
    return render_template(
        "index.html",
        reply=reply,
        history=bot.history
    )


@app.route('/favicon.ico')
def favicon():
    return send_file(
        url_for("static", filename="favicon.ico")
    )
