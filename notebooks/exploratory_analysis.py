import pandas as pd
import numpy as np

from utils import functions as f

# Apresentação dos 5 primeiros registros do arquivo
def first_five_entries(f):
    print(f.head())

# Mostra informações do DataFrame
def show_info(f):
    print('\n')
    print('=' * 50)
    print('INFORMAÇÕES SOBRE A BASE DE DADOS')
    print('=' * 50)
    print(f'\nLinhas: {f.shape[0]}\nColunas:{f.shape[0]}\n')
    print('TIPOS DE DADOS')
    print(f.dtypes)

    print(f'\nColunas que estão totalmente vazias:\n{f.columns[f.isnull().any()].tolist()}\n')



# LIMPOEZA DA BASE:
# Replace em registros nulos
# Limpeza de colunas vazias ou duplicadas
# Normaliza campos de string
# Converte campo data de string para date

def replace_nulls(f):
    df = f.replace({'NULL': np.nan, 'N/A': np.nan, '': np.nan, '#N/D': np.nan})
    df = df.dropna(axis=1, how='all')
    df = df.dropna(subset=['PR_CAT', 'PR_NOME'])
    df = df.drop_duplicates(keep='first')
    df = df.reset_index(drop=True)
    print(f'Total de linhas após limpeza: {len(df)}')
    df['PR_CAT'] = df['PR_CAT'].str.title().str.strip()
    df['PR_NOME'] = df['PR_NOME'].str.title().str.strip()

    return df

def reports(f):
    print('\n')
    print('=' * 50)
    print('INFORMAÇÕES SOBRE A BASE DE DADOS')
    print('=' * 50)
    nulls = f.isnull().sum()
    pct = nulls / len(f) * 100
    print('*' * 10)
    duplicateds = f.duplicated().sum()
    print(pd.DataFrame({'Nulos': nulls, '% Nulos': pct}))
    print('*' * 10)
    print(f'Linhas duplicadas: {duplicateds}')

def new_file(f):
    f.to_csv('data/processed/Base Limpa.csv',sep=';')
    print('Novo arquivo \'Base Limpa.csv\' limpo salvo com sucesos.')


show_info(f.df)
print('=' * 50)
print('=' * 50)
replaced = replace_nulls(f.df)
new_file(replaced)
show_info(replaced)
first_five_entries(replaced)
reports(f.df)
reports(replaced)