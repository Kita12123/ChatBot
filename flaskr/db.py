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
    def db(self) -> dict[str, str]:
        with open(file=self.file_path, mode="r", encoding="cp932") as f:
            db = json.load(f)
        return db
