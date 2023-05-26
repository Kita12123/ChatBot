"""
会話データ保存
"""
import pickle
from pathlib import Path

file_path = Path(__file__).parent / "static" / "history.txt"


def input_history():
    with open(file=file_path, mode="rb") as f:
        history = pickle.load(f)
    return history


def output_history(history):
    with open(file=file_path, mode="wb") as f:
        pickle.dump(history, f)
