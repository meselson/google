import time
import requests
today = time.strftime("%m%d")

url = f'https://raw.githubusercontent.com/pojiezhiyuanjun/freev2/master/{today}clash.yml'
info = requests.get(url).text
with open('free.yml', 'w', encoding = 'UTF-8') as f:
    f.write(info)
