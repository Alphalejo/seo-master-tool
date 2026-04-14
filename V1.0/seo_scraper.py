import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from collections import deque
import csv

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from collections import deque
import csv

def obtener_titulos_seo(url_base, limite_paginas=100):
    dominio_base = urlparse(url_base).netloc
    urls_por_visitar = deque([url_base])
    urls_visitadas = set()
    resultados = []

    # 1. Definimos las carpetas que queremos ignorar (sus hijos)
    carpetas_ignoradas = ('/blog/', '/neighborhoods/', '/developments/', '/properties/', '/agent/', '/agents/', '/home-search/', '/cdn-cgi/')
    
    # 2. Definimos las EXCEPCIONES: páginas que SÍ queremos aunque estén en carpetas ignoradas
    paginas_permitidas = ('/properties/sale', '/properties/sold')

    print(f"\nIniciando escaneo inteligente en: {url_base}\n")

    while urls_por_visitar and len(urls_visitadas) < limite_paginas:
        url_actual = urls_por_visitar.popleft()

        if url_actual in urls_visitadas:
            continue

        urls_visitadas.add(url_actual)
        print(f"Escaneando ({len(urls_visitadas)}/{limite_paginas}): {url_actual}")

        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            respuesta = requests.get(url_actual, headers=headers, timeout=10)
            if respuesta.status_code != 200 or 'text/html' not in respuesta.headers.get('Content-Type', ''):
                continue

            sopa = BeautifulSoup(respuesta.text, 'html.parser')

            # Extraer SEO Title
            etiqueta_titulo = sopa.find('title')
            titulo = etiqueta_titulo.text.strip() if etiqueta_titulo else "Sin título"
            
            resultados.append({
                'url': url_actual,
                'titulo': titulo,
                'longitud': len(titulo)
            })

            # LÓGICA DE FILTRADO DE ENLACES
            for enlace in sopa.find_all('a', href=True):
                url_absoluta = urljoin(url_base, enlace['href']).split('#')[0].rstrip('/')
                ruta_url = urlparse(url_absoluta).path.rstrip('/') # Limpiamos barras al final para comparar mejor

                if urlparse(url_absoluta).netloc == dominio_base:
                    
                    # ¿La ruta es una excepción permitida?
                    es_excepcion = any(ruta_url == p.rstrip('/') for p in paginas_permitidas)
                    
                    # ¿La ruta pertenece a una carpeta ignorada?
                    pertenece_a_ignorados = any(ruta_url.startswith(c) for c in carpetas_ignoradas)

                    # REGLA: Si es excepción, entra. Si no es excepción pero está en ignorados, fuera.
                    if es_excepcion or not pertenece_a_ignorados:
                        if url_absoluta not in urls_visitadas and url_absoluta not in urls_por_visitar:
                            urls_por_visitar.append(url_absoluta)

        except Exception:
            continue

    return resultados

# (El resto de la función guardar_en_csv y el __main__ se mantienen igual que antes)

def guardar_en_csv(datos, nombre_archivo="auditoria_seo.csv"):
    # Guardamos los datos en un archivo CSV
    if not datos:
        print("No hay datos para guardar.")
        return

    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=['url', 'titulo', 'longitud'])
        writer.writeheader()
        writer.writerows(datos)
    
    print(f"\n¡Listo! Los resultados se han guardado exitosamente en el archivo: {nombre_archivo}")

# Punto de entrada
if __name__ == "__main__":
    url_entrada = input("Introduce la URL de la página web (ej. https://ejemplo.com): ").strip()
    
    if not url_entrada.startswith(('http://', 'https://')):
        url_entrada = 'https://' + url_entrada

    # Aumenté el límite a 50 para abarcar un poco más del sitio
    datos_seo = obtener_titulos_seo(url_entrada, limite_paginas=50) 
    
    # Llamamos a la función para exportar
    guardar_en_csv(datos_seo)