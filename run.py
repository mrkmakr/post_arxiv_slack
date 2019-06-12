##https://vaaaaaanquish.hatenablog.com/entry/2017/09/27/154210

from translate import translate
from post_slack import post_message_slack, post_file_slack
from get_arxiv import get_paper_info
from pdf_download import pdf_download
from extract_image_from_pdf import extract_image
import time

def create_post_sentence(p):
    return p["title"] + "\n" + \
           p["url"] + "\n" + \
           p["summary"] + "\n"


query = "unsupervised"
n_result = 1
print("querying ...")
paper_infos = get_paper_info(query, n_result=n_result)
for p in paper_infos:
    print("translating ...")
    p["summary"] = translate(p["summary"])
    sentence = create_post_sentence(p)

    # post_message_slack("arxiv-translate", sentence)
    print("downloading pdf ...")
    filename = pdf_download(p["url"], p["title"])
    print("extracting image ...")
    extract_image(filename)
    print("uploading pdf ...")
    post_file_slack(filename, sentence)
    time.sleep(2)
    print("------")

