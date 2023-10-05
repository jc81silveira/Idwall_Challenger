import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import re

import requests
from bs4 import BeautifulSoup
import requests

from bs4 import BeautifulSoup
import json

# Loop através das páginas de 1 a 8
for page in range(1, 9):
    # URL da página com o número de página atual
    url = f'https://ws-public.interpol.int/notices/v1/red?resultPerPage=20&page={page}'

    # Enviar uma solicitação GET para a URL
    response = requests.get(url)

    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Analisar o conteúdo JSON da página
        data = json.loads(response.text)

        # Acessar a lista de avisos (notices)
        notices = data['_embedded']['notices']

        # Iterar pela lista de avisos e extrair os dados desejados
        for notice in notices:
            name = notice['forename'] + ' ' + notice['name']
            date_of_birth = notice['date_of_birth']

            # Verificar se 'nationalities' é uma lista antes de usá-la com join
            if isinstance(notice['nationalities'], list):
                nationalities = ', '.join(notice['nationalities'])
            else:
                nationalities = notice['nationalities']  # Se não for uma lista, use o valor diretamente

            # Imprimir os dados
            print("Name:", name)
            print("Date of Birth:", date_of_birth)
            print("Nationalities:", nationalities)
            print("\n")

    else:
        print(f"Falha ao acessar a página {page}: {response.status_code}")
