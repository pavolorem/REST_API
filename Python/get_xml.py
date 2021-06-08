import time
import urllib3
import requests

url = ""

payload = ""
headers = {
  'Content-Type': 'text/xml'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
print(response.status_code)
print(response.elapsed.total_seconds())


