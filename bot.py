import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get("OPENAI_SECRET_KEY")


class Bot:

    def __init__(self, message: str):
        self.completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"rolw": "user", "content": message}
            ]
        )

    def system(self, *args):
        self.system_messages = [
            {"role": "system", "content": text}
            for text in args
        ]

    def chat(self, message: str, /) -> str:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                *self.system_messages,
                {"role": "user", "content": message}
            ]
        )
        return completion.choices[0].message.content
    

cute_bot = Bot(
    "語尾ににゃんをつけてください。",
    "可愛く答えてください。"
)
print(
    cute_bot.talk("正しい箸の持ち方を教えて")
)
