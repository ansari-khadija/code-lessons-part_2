# web scrapping with regular expression


import re
import urllib
from urllib.request import urlopen

url = "https://example.com"

html = urlopen(url).read().decode("utf-8")

data = re.findall(r"<p>(.*?)</p>", html, re.IGNORECASE | re.DOTALL)

for item in data:
    print(item)
