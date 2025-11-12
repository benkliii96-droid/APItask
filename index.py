import requests
import wikipediaapi
from PIL import Image


GRAND = {
    "name": "Троице-Сергиева_лавра",
    "x": 38.130492,
    "y": 56.311120
}

def req_wiki(name1):
    if name1 == GRAND.get("name"):
        wiki = wikipediaapi.Wikipedia("Evg13n", "ru")
        page = wiki.page(name1)
        return page.text
    else:
        raise Exception("Места нету в списке)")


def req_map(ux, uy):
    if all([ux == GRAND.get("x"), uy == GRAND.get("y")]):
        map = requests.get(f"https://static-maps.yandex.ru/1.x/?ll={ux},{uy}&spn=0.005,0.005&l=map")
        with open("map.png", "wb") as f:
            f.write(map.content)
    else:
        raise Exception("Места с таким координатами нет)")


name = input("Введите имя достопримечательности\n")
coord = input("Введите координаты в формате: y x\n").split()
if len(coord) != 2:
    raise Exception("Должно быть 2 координаты")
x = float(coord[0])
y = float(coord[1])
info = req_wiki(name)
req_map(x, y)

img = Image.open('map.png')
print(name)
img.show()
print(info)