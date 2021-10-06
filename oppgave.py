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
#oppg 1.1
"""
G = nx.karate_club_graph()
print(G.nodes,G.edges)
"""
#oppg 1.2
'''
G = nx.karate_club_graph()
var = nx.get_node_attributes(G, "club")
color_list = []
for y in var:
    if var[y]=="Mr. Hi":
        color_list.append("green")
    if var[y]=="Officer":
        color_list.append("blue")
print(color_list)
nx.draw(G, node_color=color_list, with_labels=True)
plt.show()
'''
#oppg 1.3
'''
G = nx.karate_club_graph()
var = nx.get_node_attributes(G, "club")
print(nx.dijkstra_path(G,24,16))
'''
#oppg 1.4
'''
G = nx.karate_club_graph()
layout = nx.spring_layout(G)
color_list = []
for x in G.nodes(data=True):
    if (16) in x:
        color_list.append("red")
    elif (14) in x:
        color_list.append("red")
    elif {'club': 'Mr. Hi'} in x:
        color_list.append("green")
    else:
        color_list.append("blue")

nx.draw(G, layout, node_color=color_list, with_labels=True)
plt.show()
'''
#oppg 2

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
