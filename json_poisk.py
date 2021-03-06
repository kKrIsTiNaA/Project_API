from io import BytesIO
import requests
from PIL import Image


def json_poisk_roma(delta="0.005", dvigat=[0, 0], type="map",
                    toponym_to_find='Москва, ул. Ак. Королева, 12', metka=False):
    delta = str(delta)
    # работаю один, т.к. мне хватило 2ух часов, потраченных с этими людьми!
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        return False
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    map_params = {
        "ll": ",".join([str(float(toponym_longitude) + dvigat[0]),
                        str(float(toponym_lattitude) + dvigat[1])]),
        "spn": ",".join([delta, delta]),
        "l": type,
        "size": "450,450"
    }
    if metka:
        map_params['pt'] = ",".join([str(float(toponym_longitude)),
                                     str(float(toponym_lattitude))])
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    if type == 'map':
        im = open('map.png', 'wb')
    else:
        im = open('map.jpg', 'wb')
    im.write(response.content)
    im.close()
    return True


json_poisk_roma()
