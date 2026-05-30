# Importação das bibliotecas
from kaggle import api
from dotenv import load_dotenv
import os
import zipfile
import glob
import pandas as pd

load_dotenv()

os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_API_TOKEN')

file_path = 'data/raw/'


def downloadDataSet(repo, file):
    api.dataset_download_files(
        f'{repo}/{file}',
        path=file_path
    )

    zip_path = os.path.join(file_path, f'{file}.zip')

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:

        # procura automaticamente o csv
        csv_name = next(
            arquivo for arquivo in zip_ref.namelist()
            if arquivo.endswith('.csv')
        )

        print(f'CSV encontrado: {csv_name}')

        zip_ref.extract(csv_name, file_path)

        return os.path.join(file_path, csv_name)
    


def cleanDirectory():
    zip_files = glob.glob(
        os.path.join(file_path, '**', '*.zip'),
        recursive=True
    )

    pdf_files = glob.glob(
        os.path.join(file_path, '**', '*.pdf'),
        recursive=True
    )

    for arquivo in zip_files:
        os.remove(arquivo)

    for arquivo in pdf_files:
        os.remove(arquivo)


csv_path = downloadDataSet('namespaiva', 'base-varejo')

cleanDirectory()

df = pd.read_csv(csv_path, sep=';')