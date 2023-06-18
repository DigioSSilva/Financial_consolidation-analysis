
import pandas as pd
import wget
from zipfile import ZipFile

url_base = 'https://ftp.ibge.gov.br/Precos_Indices_de_Precos_ao_Consumidor/IPCA/Resultados_por_Subitem/'

for i in range(1, 13):
    for j in range(2005, 2023):
        url = f"{url_base}{j}/ipca_{j}{i:02d}Subitem.zip"
        try:
            wget.download(url)
            print("Download concluído!")
        except Exception as e:
            print(f"Erro durante o download: {e}")
