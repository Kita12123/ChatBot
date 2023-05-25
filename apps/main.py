from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from pathlib import Path

from apps.bot import Bot

static_dir = Path(__file__).parent / "static"

app = Flask(__name__)
bot = Bot("出来る限り１００文字以内で返答してください。")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        req = request.form.get("request")
        bot.chat(req)
    return render_template(
        "index.html",
        history=bot.history
    )



@app.route('/favicon.ico')
def favicon():
    return send_file(
        static_dir / "favicon.ico"
    )
