import requests as re
response = re.get('https://google.com')
html = response.text
print(html) 