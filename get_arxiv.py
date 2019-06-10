import re
import requests

def parse(data, tag):
    # parse atom file
    # e.g. Input :<tag>XYZ </tag> -> Output: XYZ

    pattern = "<" + tag + ">([\s\S]*?)<\/" + tag + ">"
    if all:
        obj = re.findall(pattern, data)
    for k in range(len(obj)):
        obj[k] = obj[k].replace("\n  ", " ")
        obj[k] = obj[k].replace("\n", " ")
    return obj


def parse_url(data):
    pattern = "link href=\"" + "([\s\S]*?)" + "\""
    if all:
        obj = re.findall(pattern, data)
    return obj[1:]


def get_paper_info(query, start=0, n_result=10):
    url = 'http://export.arxiv.org/api/query?search_query=' + query + '&start=' + str(
        start) + '&max_results={}&sortBy=lastUpdatedDate&sortOrder=descending'.format(n_result)
    data = requests.get(url).text

    title = parse(data, "title")
    summary = parse(data, "summary")
    url = parse_url(data)

    paper = []
    for k in range(len(title)):
        dic = {"title" : title[k], "summary" : summary[k], "url" : url[k]}
        paper.append(dic)

    return paper