#!/user/bin/python3
""" a simple HTTP client """
import http.client

conn = http.client.HTTPConnection("localhost", "8000")

conn.request('HEAD', '/')

res = conn.getresponse()

print(dir(res))

print(res.status, res.reason)

conn.request('GET', '/')
res = conn.getresponse()

print(res.status, res.reason)

print(res.readlines())
