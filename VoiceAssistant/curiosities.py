from bs4 import BeautifulSoup
import requests
import random

curiosities = []

def get_curiosities():
    response = requests.get('https://pl.wikipedia.org/wiki/Portal:Informatyka/Ciekawostki')
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    for c in soup.find('div', class_ = 'mw-parser-output').findAll('li'):
        try:
            t = c.text
            curio = {
                "curio": t
            }
            curiosities.append(curio)
        except Exception as e:
            pass
    response = requests.get('https://pl.wikipedia.org/wiki/Portal:Zoologia/Ciekawostki')
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    for c in soup.find('div', class_='mw-parser-output').findAll('li'):
        try:
            t = 'Czy wiesz, że' + c.text
            curio = {
                "curio": t
            }
            curiosities.append(curio)
        except Exception as e:
            pass
    response = requests.get('https://pl.wikipedia.org/wiki/Portal:%C5%BBegluga/Ciekawostki')
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    for c in soup.find('div', class_='mw-parser-output').findAll('li'):
        try:
            t = 'Czy wiesz, że' + c.text
            curio = {
                "curio": t
            }
            curiosities.append(curio)
        except Exception as e:
            pass
    response = requests.get('https://pl.wikipedia.org/wiki/Portal:%C5%BBeglarstwo/Czy_wiesz,_%C5%BCe')
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    for c in soup.find('div', class_='mw-parser-output').findAll('li'):
        try:
            t = c.text
            curio = {
                "curio": t
            }
            curiosities.append(curio)
        except Exception as e:
            pass



def get_random_curio():
    if len(curiosities) == 0:
        get_curiosities()
    index = random.randint(0, len(curiosities))
    return curiosities[index]