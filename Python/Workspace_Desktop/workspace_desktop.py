from requests import get
from bs4 import BeautifulSoup

html_response = get('https://www.mangatown.com/latest/', stream=True, verify=False)

raw_html = html_response.content

html = BeautifulSoup(raw_html, 'html.parser')

title_list = []
for title in html.find_all('a'):
    title = title.get('title')
    if title is None:
        continue
    else:
        title_list.append(title)

title_list = title_list[0::3]
for i in title_list:
    print(i)


'''
new_title_list = list(set(title_list))

for i in new_title_list:
    print(i)
'''
