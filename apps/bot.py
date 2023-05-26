import openai
from openai.error import RateLimitError
import os
from dotenv import load_dotenv
from pathlib import Path
import pickle

load_dotenv()
openai.api_key = os.environ.get("OPENAI_SECRET_KEY")


def request(history):
    """リクエスト応答"""
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=history
        )
        reply = completion.choices[0].message.content
    except (openai.error.RateLimitError):
        reply = "ごめんなさい。エラーが発生しました。\n時間をおいてからもう一度お願いします。"
    reply_html = reply.replace(
        "\n", "<br>"    # 改行
    ).replace(
        " ", "&nbsp;"   # 半角スペース
    ).replace(
        "　", "&emsp;"  # 全角スペース
    )
    return reply_html
