import requests, json

link= "http://httpbin.org/post"
# POST
rp = requests.post(link, data=json.dumps(open(r"resources/test.json").read()), headers = {'lord': 'sauron'})
print(rp)
print(rp.url)
print(rp.content)
print(rp.headers)