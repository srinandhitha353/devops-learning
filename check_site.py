import urllib.request

sites = [
    "https://github.com",
    "https://google.com",
    "https://thissitedoesnotexist12345.com",
]

for url in sites:
    try:
        response = urllib.request.urlopen(url, timeout=5)
        print(f"{url} is UP (status {response.status})")
    except Exception as error:
        print(f"{url} is DOWN ({error})")
