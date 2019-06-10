import requests
import os
import time


def pdf_download(url, papername = None):

    DATA_DIR = "data/"
    os.makedirs(DATA_DIR, exist_ok=True)

    url = url.replace("abs", "pdf") + ".pdf"
    if papername is None:
        filename = DATA_DIR + url.split("/")[-1]
    else:
        filename = DATA_DIR + papername + ".pdf"

    if os.path.exists(filename):
        print("Downloaded: " + filename)
    else:
        print("Download: " + filename)
        res = requests.get(url)
        with open(filename, "wb") as f:
            f.write(res.content)

        print("Downloaded: " + filename) # 保存できていることを確認するため、保存したfilenameを表示
        time.sleep(1) # アクセスの間隔が1秒空くようにする
    return filename