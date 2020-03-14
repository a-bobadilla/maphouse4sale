
import requests
from bs4 import BeautifulSoup
def separador(latitud_longitud):
    contador=0
    for x in latitud_longitud:
        contador+=1 
        if x==',':
            index_coma=contador
            break   
    latitud= latitud_longitud[0:index_coma]
    longitud= latitud_longitud[index_coma: ]
    #para ver en consola los datos formateados descomentar la siguiente línea 
    #print("lat:",latitud,"long:", longitud)
    return latitud, longitud
def casas():
    """
    Funcion que extrae los datos de las casas de hendyla
    y retorna estos datos en un diccionario
    """
    page=requests.get("https://casas.hendyla.com/")   
    soup= BeautifulSoup(page.content,'html.parser')
    datos = soup.find_all('article',class_ ='product-item clasificado')
    lista_datos=[] # diccionario donde se cargan todos los datos
    for indice in range(len(datos)):  
        try:
            dcasas = datos[indice]
            print("-----------------------")
            # buscamos el precio y formateamos los datos
            precio= dcasas.find_all('div',class_='precio left')[0].p.get_text()[10:].replace(" ",'')
            print(precio)
            descripcion= dcasas.select('div.desc a')[0].get_text()
            print(descripcion)
            url_publicacion= dcasas.select('div.desc a')[0].get('href')
            print(url_publicacion)
            # sacar la latitud y longitud
            pagina2= requests.get(url_publicacion)
            soup2=BeautifulSoup(pagina2.content,'html.parser')
            latitud_longitud= soup2.find_all('div',id='map')
            latitud_longitud= latitud_longitud[0].find('iframe').get("src")
            # extraemos latitud y longitud de la url
            index_primero= latitud_longitud.find('=')
            index_final= latitud_longitud.find('&')
            latitud_longitud= latitud_longitud[index_primero+1:index_final]
            latitud,longitud= separador(latitud_longitud)
            resultado={
                "precio": precio,
                "descripcion":descripcion,
                "ubicacion": {
                    "latitud": latitud,
                    "longitud": longitud
                }
            }
            lista_datos.append(resultado)
            print("--------------------------------------")
        except:
            
            otra= soup2.find_all('div', id='zona-map')
            latitud_long= otra[0].iframe.get('src')
            index_primero= latitud_long.find('=')
            index_final= latitud_long.find('&')
            latitud_longitud= latitud_long[index_primero+1:index_final]
            print("excepcion")
            latitud,longitud= separador(latitud_longitud)
            resultado={
                "precio": precio,
                "descripcion":descripcion,
                "ubicacion": {
                    "latitud": latitud,
                    "longitud": longitud
                }
            }
            lista_datos.append(resultado)

    print("cantidad colectada:", len(lista_datos))
    return lista_datos

#casas()


