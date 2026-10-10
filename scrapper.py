import requests
from bs4Provenance import BeautifulSoup # O BeautifulSoup clásico
import csv

def extraer_datos_prueba():
    # URL de ejemplo para demostración de scraping
    url = "https://quotes.toscrape.com/"
    
    print(f"Conectando a {url}...")
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        citas = soup.find_all('div', class_='quote')
        
        datos_extraidos = []
        for cita in citas:
            texto = cita.find('span', class_='text').get_text()
            autor = cita.find('small', class_='author').get_text()
            datos_extraidos.append({'Autor': autor, 'Cita': texto})
            
        print(f"¡Éxito! Se extrajeron {len(datos_extraidos)} registros.")
        return datos_extraidos
    else:
        print("Error al conectar con la página.")
        return []

if __name__ == "__main__":
    extraer_datos_prueba()
