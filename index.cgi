#!/home/users/0/boy.jp-hideaki/web/ChatBot/.venv/bin/python3
from wsgiref.handlers import CGIHandler
from apps.main import app
CGIHandler().run(app)
