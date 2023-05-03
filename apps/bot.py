import openai
from openai.error import RateLimitError
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get("OPENAI_SECRET_KEY")


class Bot:

    def __init__(self, *args):
        self.history = [
            {"role": "system", "content": arg}
            for arg in args
        ]

    def chat(self, request: str, /) -> str:
        self.history.append({"role": "user", "content": request})
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.history
        )
        reply = completion.choices[0].message.content
        self.history.append({"role": "assistant", "content": reply})
        return reply


if __name__ == "__main__":
    bot = Bot(
        "出来る限り１００文字以内で返答してください。"
    )
    print("好きな質問をしてください。Enterで終了します。")

    while True:
        request = input("\n>>")
        if not request:
            print("終了します。")
            break
        print(bot.chat(request))
