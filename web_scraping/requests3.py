from lxml import html
import requests
response = requests.get('http://www.data.gov/')
doc_gov = html.fromstring(response.text)
print(doc_gov)
