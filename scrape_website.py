from bs4 import BeautifulSoup
import requests
import re
import math
import re
import sys
import os
import time
import random

save_to_folder = '/home/radbrt/notebooks/hackathon/job_vacancies/raw/'

url = "https://tjenester.nav.no/stillinger/stillinger?sort=akt&rpp=100&rv=l&ad=S1&p="
p = 0

html = requests.get(url + str(p)).text
soup = BeautifulSoup(html, "html.parser")

ingress = soup.find_all('p', attrs={'class', 'ingress'})[0].string
v =re.findall(r'\d+', ingress)
e = float(v[0])
final = math.ceil(e/100)


for i in range(0, int(final)):
    time.sleep(5+random.random()*10)
    html = requests.get(url + str(i)).text
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find_all('tbody')
    for entry in table:
        time.sleep(2+random.random())
        link = entry.find_all('a')[0]["href"][1:]
        adurl = 'https://tjenester.nav.no/stillinger' + link

        pattern = 'ID=([0-9]+)'
        pid = re.search(pattern, adurl).group(0).replace("ID=", "")
        jobtext = requests.get(adurl).text

        f = open(save_to_folder + 'jobb' + pid + '.html', 'w')
        f.write(jobtext)
        f.close()
