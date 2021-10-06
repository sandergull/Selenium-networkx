import networkx as nx
import selenium
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random as RC
import re
import urllib.parse

firefox_options = Options()

driver = webdriver.Firefox(executable_path="drivers/geckodriver", options = firefox_options)
driver.get('https://twitter.com/hashtag/Winter?src=hashtag_click')

teller = 0
G = nx.Graph()
nyhashtags = []
nodeliste = []

while teller<=20:
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located(
            (By.PARTIAL_LINK_TEXT, "#")))
    expression = re.compile("(https://twitter.com/hashtag/)")

    links = driver.find_elements_by_tag_name("a")
    liste=[]
    for linker in links:
        link = linker.get_attribute('href')
        liste.append(link)

    hashtags = []
    for x in liste:
        if expression.match(x):
            hashtags.append(x)
    tall = RC.randint(0, len(hashtags) - 1)
    nyhashtags.append(hashtags[tall])
    print(hashtags)
    print(nyhashtags)
    xd=driver.get(nyhashtags[-1])
    s = nyhashtags[-1]
    try:
        found = re.search('https://twitter.com/hashtag/(.+?)src', s).group(1)
    except AttributeError:
        found = ''
    nynode = found[:-1]
    if nynode not in nodeliste:
        nodeliste.append(f"#{nynode}")
    teller+=1
print(nodeliste)
driver.quit()
nyteller = -1
for noder in nodeliste:
    G.add_node(noder)
    G.add_edge(nodeliste[nyteller],noder)
    nyteller +=1

nx.draw(G, with_labels=True)
plt.show()
nx.write_graphml(G, "mingraf.graphml")
