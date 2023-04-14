import openai
from openai.error import RateLimitError
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get("OPENAI_SECRET_KEY")


class Bot:

    def __init__(self, *args):
        self.chat_logs = [
            {"role": "system", "content": arg}
            for arg in args
        ]

    def chat(self, request: str, /) -> str:
        self.chat_logs.append({"role": "user", "content": request})
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.chat_logs
        )
        reply = completion.choices[0].message.content
        self.chat_logs.append({"role": "assistant", "content": reply})
        return reply


if __name__ == "__main__":
    bot = Bot(
        "出来る限り１００文字以内に返答してください。"
    )
    print("好きな質問をしてください。Enterで終了します。")

    while True:
        request = input("\n>>")
        if not request:
            print("終了します。")
            break
        print(bot.chat(request))
