import requests
# link = "https://movies-directory.herokuapp.com"
link = "https://fb.com"
r=requests.get(link)
print(r)
print(r.text) # or print(r.content)
print(r.headers)
print(r.elapsed)
print(r.reason) # OK, Not Found
print(r.encoding)
print(r.status_code)
print(r.history)
print(list(r.cookies))
print(requests.codes['ok'])
print(requests.codes['temporary_redirect'])
print(requests.codes['forbidden'])