import requests
import xml.etree.ElementTree as ET
from collections import namedtuple

res = requests.get("http://export.arxiv.org/rss/cs.CV")
Article = namedtuple("Article", ("title", "link", "description"))

def parse_articles(xml):
    tree = ET.ElementTree(ET.fromstring(xml))
    ns = {"rss": "http://purl.org/rss/1.0/"}
    items = tree.findall("rss:item", ns)
    return [
       Article(*[
           item.find("rss:{}".format(field), ns).text
           for field in Article._fields
       ])
       for item in items
    ]


for article in parse_articles(res.text):
    article
    title = "".join(article.title.split(".")[:-3])
    abst = article.description[3:-5]
    url = article.link
    print(title, abst, url)