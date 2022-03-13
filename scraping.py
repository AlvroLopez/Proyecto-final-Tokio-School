from bs4 import BeautifulSoup as bs
import requests
import lxml

def naturgy():

    url = "https://www.naturgy.es/hogar/luz/tarifa_por_uso_luz"
    page = requests.get(url)
    soup = bs(page.content, 'lxml') 
    # El parser por defecto (html.parser) da error, devuelve None al buscar ciertos elementos aunque esté bien filtrado
    # Uso el parser recomendado en la documentación de BeautifulSoup
     
    result = soup.find(class_="col-md-3 infoMiddle").find('strong')
    # Búsqueda por filtros. Primero filtro por la clase de una etiqueta 'padre' en la que está contenida la información que busco
    # Dentro de esa etiqueta, el precio de la energía está dentro de una etiqueta <strong> que uso como segundo y último filtro

    result_str = result.string
    # La variable result es de tipo Tag, una clase propia de BeautifulSoup. La manera de convertirlo en el análogo a un string y poder
    # manejarlo mejor es accediendo al atributo .string
    # Este objeto es de tipo NavigableString, otra clase propia de BeautifulSoup, pero a la que se le pueden aplicar muchos métodos propios
    # de strings convencionales de Python, como hago a continuación

    result_str_format = float(result_str[0:6].replace(',','.'))  # Recordatorio: esto es precio sin impuestos, hay que sumarle el 10% de IVA
    # En mi programa no quiero un string que incluya caracteres como €/kWh, quiero un número con el que poder operar, así que le aplico
    # diferentes métodos de string

    # Precio potencia: 3 €/kW*mes
    return result_str_format*1.1    # Se multiplica por 1,1 porque el precio que aparece en la página no incluye el IVA (10%)



def iberdrola(): # Con sus ciertas particularidades, el web scraping del resto de las páginas sigue el mismo proceso

    url = "https://www.companias-de-luz.com/iberdrola/precio-kwh/"
    page = requests.get(url)
    soup = bs(page.content, 'lxml')
    result = soup.find(class_='table-container__wrapper').find('tbody').find_all('tr')[4].find_all('td')[1].contents[2]
    result_str = result.string
    result_str_format = float(result_str[2:8].replace(',','.'))
    return result_str_format*1.1

    # Precio potencia: 3,3 €/kW*mes

def endesa():

    url = "https://www.companias-de-luz.com/endesa/precio-kwh/"
    page = requests.get(url)
    soup = bs(page.content, 'lxml')
    result = soup.find_all('tbody')[2].find('tr').find_all('td')[2]
    result_str = result.string
    result_str_format = float(result_str[:6].replace(',','.'))
    return result_str_format*1.1

    # Precio potencia: 3,9 €/kW*mes

def repsol():

    url = "https://www.companias-de-luz.com/repsol/precio-kwh/"
    page = requests.get(url)
    soup = bs(page.content, 'lxml')
    result = soup.find('table').find_all('tr')[1].find_all('td')[2]
    result_str = result.string
    result_str_format = float(result_str[30:35].replace(',','.'))
    return result_str_format*1.1
    # Precio potencia: 4,8 €/kW*mes

def edp():

    url = "https://www.companias-de-luz.com/edp/precio-kwh/"
    page = requests.get(url)
    soup = bs(page.content, 'lxml')
    result = soup.find('table').find('tbody').find_all('tr')[2].find_all('td')[3]
    result_str = result.string
    result_str_format = float(result_str[:5].replace(',','.'))
    return result_str_format*1.1

    # Precio potencia: 3,48 €/kW*mes

def tarifa():

    # El precio del kWh obtenido para cada compañía se combinará en un sólo diccionario que aglutine todas las compañías que compararemos

    # Esta función sólo se usará la primera vez y cuando se pulse en la opción 'Crear más clientes'. Se guardarán los datos correspondientes
    # para no saturar el servidor de la página de la que estamos obteniendo los datos

    tarifas = {
        'Naturgy': naturgy(),
        'Iberdrola' : iberdrola(),
        'Endesa' : endesa(),
        'Repsol' : repsol(),
        'EDP' : edp()
    }

    return tarifas

if __name__ == "__main__":
    pass




