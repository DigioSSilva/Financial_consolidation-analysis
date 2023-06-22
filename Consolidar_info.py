#Consolidar todas as informações das demonstrações em arquivos individuais que serão posteriormente salvos em DB
import os
import pandas as pd
import time
import csv


lista_dfps = ["BPA", "BPP", "DFC_MD", "DFC_MI", "DMPL", "DRA", "DRE", "DVA"]

def ConsolidarRelatorio():
    for relatorio in lista_dfps:
        data = pd.DataFrame()
        for i in range(2010, 2023):
            link = fr"C:\Users\RI-PC-0150\OneDrive - Leme\Área de Trabalho - Diego LEME\Files - Diego LEME\Code\Python\VsProjects\Financial_consolidation&analysis\Dfp\{i}\dfp_cia_aberta_{relatorio}_con_{i}.csv"
            with open(link, 'r', newline='', encoding='latin-1') as file:
                reader = csv.reader(file, delimiter=';')
                df = pd.DataFrame(reader)
                data = pd.concat([data, df])
                #data = data.append(df)
        data.reset_index(drop=True, inplace=True)
        link_export = fr"C:\Users\RI-PC-0150\OneDrive - Leme\Área de Trabalho - Diego LEME\Files - Diego LEME\Code\Python\VsProjects\Financial_consolidation&analysis\Dfp\Dfp_Consolidado\{relatorio}.csv"
        data.to_csv(link_export, index=False)
        print(f"Relatório {relatorio} concatenado e salvo!")

def AddTickereSetor():
    for relatorio in lista_dfps:
        link = fr"C:\Users\RI-PC-0150\OneDrive - Leme\Área de Trabalho - Diego LEME\Files - Diego LEME\Code\Python\VsProjects\Financial_consolidation&analysis\Dfp\Dfp_Consolidado\{relatorio}.csv"
        tickers = pd.read_excel(r"C:\Users\RI-PC-0150\OneDrive - Leme\Área de Trabalho - Diego LEME\Files - Diego LEME\Code\Python\VsProjects\Financial_consolidation&analysis\Dfp\Ticker\Ticker_CNPJ.xlsx")
        with open(link, 'r', newline='', encoding='latin-1') as file:
            reader = csv.reader(file, delimiter=';')
            dados = list(reader)
        df = pd.DataFrame(dados[1:], columns=dados[0])
        dict_ticker = tickers.set_index("CNPJ")["TICKER"].to_dict()
        dict_setor = tickers.set_index("CNPJ")["SETOR"].to_dict()
        df["TICKER"] = df["CNPJ_CIA"].map(dict_ticker)
        df["SETOR"] = df["CNPJ_CIA"].map(dict_setor)
        link_export = fr"C:\Users\RI-PC-0150\OneDrive - Leme\Área de Trabalho - Diego LEME\Files - Diego LEME\Code\Python\VsProjects\Financial_consolidation&analysis\Dfp\Dfp_Consolidado\{relatorio}.csv"
        df = df[1:]
        df.to_csv(link_export)
        print(f"Relatório {relatorio} ajustado!")

ConsolidarRelatorio()
