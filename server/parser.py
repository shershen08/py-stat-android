import requests
import json
from bs4 import BeautifulSoup

#soup = BeautifulSoup(html_doc, 'html.parser')

def get_page(page_url):
    result = requests.get(page_url)

    if(result.status_code == 200):
        return result.content, result

def parse_result_json(item_content):
    soup = BeautifulSoup(item_content, "html.parser")
    json_data = {}

    json_data['image'] = []
    for img in soup.find_all('img'):
        if(img['src']):
            json_data['image'].append(img['src'])
    
    json_data['stylesheet'] = []
    for style in soup.find_all('link'):
        if(style['rel'] == ['stylesheet'] and hasattr(style, 'href')):
            json_data['stylesheet'].append(style['href'])
    
    json_data['script'] = []
    for script in soup.find_all('script'):
        try:
            json_data['script'].append(script.attrs['src'])
        except KeyError:
            pass
    
    return json_data

def get_stats(resp):
    print(resp)
    return 42

def get_header(item_url):
    req = requests.get(item_url)
    req_header = req.headers
    print(req_header)
    # if(req.status_code == 200 and hasattr(req_header, 'content-length')):
    #     return int(req_header['content-length'])/1024
    
    #return '..'

# init

def get_all(url="https://docs.python.org/3/tutorial/errors.html"):
    cont, resp_object = get_page(url)

    json_output = parse_result_json(cont)
    json_output['total_time'] = resp_object.elapsed.total_seconds()
    print(resp_object.__dict__.keys())
    return json_output
    #jj
    #stats = get_stats(resp_object)
    #print(json_output)


if __name__ == "__main__":
    print(get_all())

# get all html
#
# soup = BeautifulSoup(cont, "html.parser")
# print(soup.prettify())