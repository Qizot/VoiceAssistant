from bs4 import BeautifulSoup
import requests
import random

curiosities = []


def get_curiosities_from_wikipedia_page(response, add_intro=False):
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    for c in soup.find('div', class_='mw-parser-output').findAll('li'):
        if add_intro:
            t = 'Czy wiesz, że '
        else:
            t = ''
        t += c.text
        curio = {
            "curio": t
        }
        curiosities.append(curio)


def get_curiosities():
    response = requests.get('https://pl.wikipedia.org/wiki/Portal:Informatyka/Ciekawostki')
    get_curiosities_from_wikipedia_page(response)

    response = requests.get('https://pl.wikipedia.org/wiki/Portal:Zoologia/Ciekawostki')
    get_curiosities_from_wikipedia_page(response, add_intro=True)

    response = requests.get('https://pl.wikipedia.org/wiki/Portal:%C5%BBegluga/Ciekawostki')
    get_curiosities_from_wikipedia_page(response, add_intro=True)

    response = requests.get('https://pl.wikipedia.org/wiki/Portal:%C5%BBeglarstwo/Czy_wiesz,_%C5%BCe')
    get_curiosities_from_wikipedia_page(response)


def get_random_curio():
    if len(curiosities) == 0:
        get_curiosities()
    get_curiosities()
    index = random.randint(0, len(curiosities))
    return curiosities[index]


def get_wake_words():
    return ["ciekawostki", "ciekawego", "ciekawostka"]


def wake_function(frame, *rest):
    frame.assistant_speaks(get_random_curio()['curio'])
