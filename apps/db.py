"""
会話データ保存
"""
import json
from pathlib import Path

CD = Path(__file__).parent

class TaskHistory:

    file_path = CD / "database.json"

    def __init__(self):
        self.data = ""

    @property
    def db(self):
        with open(file=self.file_path, mode="r", encoding="cp932") as f:
            db: dict[str, str] = json.load(f)
        return db
