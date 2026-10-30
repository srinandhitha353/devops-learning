import urllib.request

url = "https://github.com"

try:
    response = urllib.request.urlopen(url, timeout=5)
    print(f"{url} is UP (status {response.status})")
except Exception as error:
    print(f"{url} is DOWN ({error})")
