import requests
from config import Config

config = Config()

TOKEN = config.TOKEN
CHANNEL = config.CHANNEL


def post_message_slack(text):
    param = {
        'token': TOKEN,
        'channel': CHANNEL,
        'text': text,
        "user_name" : "arxiver"
    }
    requests.post("https://slack.com/api/chat.postMessage", data=param)

def post_file_slack(file_dir, text):
    files = {'file': open(file_dir, 'rb')}
    param = {
        'token':TOKEN,
        'channels':CHANNEL,
        'initial_comment': text,
        'title': file_dir.split("/")[-1]
    }
    requests.post(url="https://slack.com/api/files.upload",params=param, files=files)
