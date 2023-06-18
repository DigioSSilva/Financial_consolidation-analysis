import zipfile
from zipfile import ZipFile
import pandas as pd
import wget
import time
import os

link_cvm = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'

year = time.localtime().tm_year

#Download infos
for i in range(2010, year+1):
        url = f"{link_cvm}/dfp_cia_aberta_{i}.zip"
        data_folder = r'C:\Users\RI-PC-0150\OneDrive - Leme\Área de Trabalho - Diego LEME\Files - Diego LEME\Code\Python\VsProjects\Analise_cias_B3\Dados\\'+ str(i)
        #Criar pastas por ano
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        file_name = os.path.join(data_folder, f'dfp_cia_aberta_{i}.zip')
        try:
            #Baixar zip
            wget.download(url, file_name)           
            
        except Exception as e:
            print(f"Erro durante o download: {e}")
        #Extrair arquivos zip
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(data_folder) 
            print(f"Download e extração ano {i} concluído!")