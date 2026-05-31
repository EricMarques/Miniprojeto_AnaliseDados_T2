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
    print(f'\nLinhas: {f.shape[0]}\nColunas:{f.shape[1]}\n')
    print('TIPOS DE DADOS')
    print(f.dtypes)

    print(f'\nColunas que estão totalmente vazias:\n{f.columns[f.isnull().any()].tolist()}\n')



# LIMPOEZA DA BASE:
# Replace em registros nulos
# Limpeza de colunas vazias ou duplicadas
# Normaliza campos de string
# Converte campo data de string para date

def clean_database(f):
    df = f.replace({'NULL': np.nan, 'N/A': np.nan, '': np.nan, '#N/D': np.nan})
    df = df.dropna(axis=1, how='all')
    df = df.dropna(subset=['PR_CAT', 'PR_NOME'])
    df = df.drop_duplicates(keep='first')
    df = df.reset_index(drop=True)
    df['PR_CAT'] = df['PR_CAT'].str.title().str.strip()
    df['PR_NOME'] = df['PR_NOME'].str.title().str.strip()

    return df

def analysis(f):
    print('=' * 50)
    print('1. ANÁLISE REFERENTE A QUANTIDADE DE FILHOS POR COMPRAS.')
    print('=' * 50)

    average_number_children = f['CL_FHL'].mean()
    print(f'Média de filhos: {average_number_children:.2f}')

    number_children = f['CL_FHL']
    print(f'\nQuantidade de filhos:\n\tMín:{number_children.min()} - Máx: {number_children.max()}')
    print('\n')
    print('=' * 50)
    print('2. ANÁLISE REFERENTE A QUANTIDADE DE COMPRAS POR GÊNERO.')
    print('=' * 50)

    gender = {
        'M': 'Masculino',
        'F': 'Feminino'
    }

    f['Gênero'] = f['CL_GENERO']
    f['Gênero'] = f['CL_GENERO'].map(gender)
    shopping_by_genre = f['Gênero'].value_counts().reset_index(name='Quantidade')
    print(f'Compras por gênero:\n{shopping_by_genre.to_string()}')
    
    marital_status = {
    1: 'Casado ou União Estável',
    2: 'Divorciado',
    3: 'Separado',
    4: 'Solteiro',
    5: 'Viúvo'
    }

    f['Estado Civil'] = f['CL_EC'].map(marital_status)
    f['Gênero'] = f['CL_GENERO'].map(gender)

    gender_by_marital_status = (
        f.groupby(['Gênero', 'Estado Civil'])
        .size()
        .reset_index(name='Quantidade')
    )
    print(f'\nCompras agrupadas pos gênero e estado civil:\n{gender_by_marital_status.to_string()}')

    items_per_purchase = f.groupby('CO_ID')['PR_ID'].count().mean()
    print(f'\nMédia de itens por compra: {items_per_purchase:.2f}')

    products_by_marital_status = (
        f.groupby(['Estado Civil', 'PR_NOME'])
        .size()
        .reset_index(name='Quantidade')
        .rename(columns={'PR_NOME': 'Produto'})
    )

    top_five_products_by_marital_status = (
        products_by_marital_status
        .sort_values(
            ['Estado Civil', 'Quantidade'],
            ascending=[True, False]
        )
        .groupby('Estado Civil')
        .head(5)
    )
    print(f'\nCinco produtos mais comprados separados por gênero:\n{top_five_products_by_marital_status.to_string(index=False)}')

    items_per_purchase = (
        f.groupby(['CL_SEG', 'CO_ID'])['PR_ID']
        .count()
        .reset_index(name='Quantidade')
    )

    average_items_by_class = (
        items_per_purchase
        .groupby('CL_SEG')['Quantidade']
        .mean()
        .round(2)
        .reset_index(name='Média de Itens por Compra')
        .sort_values('Média de Itens por Compra', ascending=False)
        .rename(columns={'CL_SEG': 'Classe'})
    )

    print(f'\nItens/compra X Classe\n{average_items_by_class.to_string(index=False)}')
    
    print('=' * 50)

def reports(f):
    nulls = f.isnull().sum()
    pct = nulls / len(f) * 100
    duplicateds = f.duplicated().sum()
    print(pd.DataFrame({'Nulos': nulls, '% Nulos': pct}))
    print('\n')
    print(f'Linhas duplicadas: {duplicateds}')
    
    print(f'\nLinhas: {f.shape[0]}\nColunas:{f.shape[1]}\n')

def new_file(f):
    f.to_csv('data/processed/Base Limpa.csv',sep=';')
    print('\n')
    print('=' * 50)
    print('=' * 50)
    print('Novo arquivo \'Base Limpa.csv\' salvo com sucesos.')
    print('=' * 50)
    print('=' * 50)

def execute():
    show_info(f.df)
    first_five_entries(f.df)

    print('\n')
    print('=' * 50)
    print('INFORMAÇÕES SOBRE A BASE DE DADOS ANTES DA LIMPEZA')
    print('=' * 50)
    reports(f.df)
    cleaned = clean_database(f.df)

    print('\n')
    print('=' * 50)
    print('INFORMAÇÕES SOBRE A BASE DE DADOS APÓS LIMPEZA')
    print('=' * 50)
    reports(cleaned)

    analysis(cleaned)

    new_file(cleaned)
