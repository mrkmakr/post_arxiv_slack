import requests
# post_url = "https://hooks.slack.com/services/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"



TOKEN = 'xoxb-659272209077-660343215760-OedcQNtGJcxWYA06VwwXF5L8'
CHANNEL = 'arxiv_paper_info'


post_url = "https://hooks.slack.com/services/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"
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
        # 'filename': file_dir.split("/")[-1],
        'initial_comment': text,
        'title': file_dir.split("/")[-1]
    }
    requests.post(url="https://slack.com/api/files.upload",params=param, files=files)