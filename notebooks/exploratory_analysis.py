import pandas as pd
import numpy as np

from utils import functions as f

# Apresentação dos 5 primeiros registros do arquivo
def first_five_entries(f):
    print(f.head())

# Mostra informações do DataFrame
def show_info(f):
    print('\n')
    print(f'\nTotal de linhas: {f.shape[0]}\nTotal de colunas:{f.shape[1]}\n')
    print('TIPOS DE DADOS')
    print(f.dtypes)

    print(f'\nColunas que estão totalmente vazias:\n{f.columns[f.isnull().any()].tolist()}\n')



# LIMPEZA DA BASE:
# Replace em registros nulos
# Limpeza de colunas vazias
# Normaliza campos de string
# Converte campo data de string para date

def clean_database(f):
    f = f.replace({
        'NULL': np.nan,
        'N/A': np.nan,
        '': np.nan
    })

    f = f.dropna(axis=1, how='all')
    duplicated_rows = f.duplicated().sum()
    print(f'Linhas potencialmente duplicadas: {duplicated_rows}')

    f = f.reset_index(drop=True)

    f['PR_CAT'] = (
        f['PR_CAT']
        .fillna('#N/D')
        .str.title()
        .str.strip()
    )

    f['PR_NOME'] = (
        f['PR_NOME']
        .fillna('#N/D')
        .str.title()
        .str.strip()
    )

    return f


# Análise exploratória
def analysis(f):
    # Definição de "opções" dos valores das variáveis e renomeação das chaves do dataframe
    gender = {
        'M': 'Masculino',
        'F': 'Feminino'
    }

    f['Gênero'] = f['CL_GENERO']
    f['Gênero'] = f['CL_GENERO'].map(gender)

    marital_status = {
    1: 'Casado ou União Estável',
    2: 'Divorciado',
    3: 'Separado',
    4: 'Solteiro',
    5: 'Viúvo'
    }

    f['Estado Civil'] = f['CL_EC'].map(marital_status)
    f['Gênero'] = f['CL_GENERO'].map(gender)

    f['Categoria'] = f['PR_CAT']
    f['Produto'] = f['PR_NOME']

    f['Classe'] = f['CL_SEG']

    print('\n')
    print('=' * 50)
    print('1. ANÁLISE REFERENTE A PRODUTOS INVÁLIDOS.')
    print('=' * 50)

    # Cópia de bases para produtos que possuam a informação #N/D
    products_df = f[
    (f['Categoria'] != '#N/D') &
    (f['Produto'] != '#N/D')
    ].copy()

    invalids_products = (
        (f['Categoria'] == '#N/D') |
        (f['Produto'] == '#N/D')
    ).sum()

    print(f'\nQuantidade de produtos inválidos(\'#N/D\'): {invalids_products}')
    print(f'Porcentagem de produtos inválidos(\'#N/D\'): {invalids_products / len(f) * 100:.2f}%')

    print('\n')
    print('=' * 50)
    print('2. ANÁLISE REFERENTE A QUANTIDADE DE FILHOS POR COMPRAS.')
    print('=' * 50)

    number_children = f['CL_FHL']
    print(f'\nQuantidade de filhos:\n\tMín:{number_children.min()} - Máx: {number_children.max()}')

    average_number_children = f['CL_FHL'].mean()
    print(f'\nMédia de filhos: {average_number_children:.2f}')

    print('\n')
    print('=' * 50)
    print('3. ANÁLISE REFERENTE A QUANTIDADE DE COMPRAS POR GÊNERO.')
    print('=' * 50)

    shopping_by_genre = f['Gênero'].value_counts().reset_index(name='Quantidade')
    print(f'\nCompras por gênero:\n{shopping_by_genre.to_string(index=False)}')

    gender_by_marital_status = (
        f.groupby([
            'Gênero',
            'Estado Civil'
        ])
        .size()
        .reset_index(name='Quantidade')
    )
    print(f'\nCompras agrupadas pos gênero e estado civil:\n{gender_by_marital_status.to_string(index=False)}')

    print('\n')
    print('=' * 50)
    print('4. ANÁLISE REFERENTE A QUANTIDADE ITENS POR COMPRAS.')
    print('=' * 50)

    average_items_per_purchase = (
        f.groupby('CO_ID')['PR_ID']
        .count()
        .mean()
    )
    print(f'\nMédia de itens por compra: {average_items_per_purchase:.2f}')

    products_by_marital_status = (
        products_df
        .groupby(['Estado Civil', 'Produto'])
        .size()
        .reset_index(name='Quantidade')
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

    items_per_purchase_by_class = (
        f.groupby(['Classe', 'CO_ID'])['PR_ID']
        .count()
        .reset_index(name='Quantidade')
    )

    average_items_by_class = (
        items_per_purchase_by_class
        .groupby('Classe')['Quantidade']
        .mean()
        .round(2)
        .reset_index(name='Média de Itens')
    )

    print(f'\nMédia de itens X Classe\n{average_items_by_class.to_string(index=False)}')

# Resultados da análise
def reports(f):
    nulls = f.isnull().sum()
    pct = nulls / len(f) * 100
    duplicateds = f.duplicated().sum()
    print(pd.DataFrame({'Nulos': nulls, '% Nulos': pct}))
    print('\n')
    print(f'Linhas ptenciaçmente duplicadas: {duplicateds}')
    print(f'Percentual de linhas: {duplicateds / len(f) * 100:.2f}%')

# Salvar nova base "limpa"
def new_file(f):
    f.to_csv('data/processed/Base Limpa.csv',sep=';')
    print('\n')
    print('=' * 50)
    print('=' * 50)
    print('Novo arquivo \'Base Limpa.csv\' salvo com sucesos.')
    print('=' * 50)
    print('=' * 50)

# Execução dos scripts
def execute():
    print('=' * 50)
    print('INFORMAÇÕES SOBRE A BASE DE DADOS')
    print('=' * 50)
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
    print('\n')

    reports(cleaned)

    analysis(cleaned)

    new_file(cleaned)
