import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://steamdb.info/stats/releases/'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontre todas as tabelas na página
tables = soup.find_all('table')

# Verifique cada tabela em busca dos dados desejados
for table in tables:
    # Verifique se a tabela possui as colunas desejadas
    if all(col in table.text for col in ['Name', 'Price', 'Rating', 'Owners']):
        # Extrair os dados das colunas da tabela
        columns = [col.text.strip() for col in table.find_all('th')]

        # Extrair os dados das linhas da tabela
        rows = []
        for row in table.find_all('tr'):
            data = [cell.text.strip() for cell in row.find_all('td')]
            if data:
                rows.append(data)

        # Criar o DataFrame usando pandas
        df = pd.DataFrame(rows, columns=columns)
        print(df)
        break



