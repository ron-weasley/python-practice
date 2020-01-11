import socket

print(socket.gethostname())

import http
from http.client import HTTPConnection

conn = HTTPConnection("api.open-notify.org")
conn.connect()
conn.request("GET", "/iss-now.json")

result = conn.getresponse()
print("\n", result.read().decode("utf-8"))

conn.close()
