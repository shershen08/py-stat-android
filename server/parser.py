import requests
import json
from bs4 import BeautifulSoup

#soup = BeautifulSoup(html_doc, 'html.parser')

def get_page(page_url):
    result = requests.get(page_url)

    if(result.status_code == 200):
        return result.content, result

def parse_result(item_content):
    soup = BeautifulSoup(item_content, "html.parser")

    print('\n images \n')
    items_count = 0
    for images_index, img in enumerate(soup.find_all('img')):
        if(img['src']):
            items_count += 1
            print(items_count, img['src'])
    
    print('\n styles \n')
    items_count = 0
    for styles_index, style in enumerate(soup.find_all('link')):
        if(style['rel'] == ['stylesheet'] and hasattr(style, 'href')):
            items_count += 1
            print(items_count, style['href'])
    
    print('\n scripts \n')
    items_count = 0
    for scripts_index, script in enumerate(soup.find_all('script')):
        try:
            items_count += 1
            print(items_count, script.attrs['src'])
        except KeyError:
            items_count -= 1
            pass


def get_size(item_url):
    req = requests.get(item_url)
    req_header = req.headers
    print(req_header)
    # if(req.status_code == 200 and hasattr(req_header, 'content-length')):
    #     return int(req_header['content-length'])/1024
    
    #return '..'

# init

url = "https://docs.python.org/3/tutorial/errors.html"
cont, resp_object = get_page(url)
total_time = resp_object.elapsed.total_seconds()
print('time: ', total_time)
parse_result(cont)

# print(soup.prettify())