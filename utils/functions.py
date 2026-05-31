from pathlib import Path
from kaggle import api
from dotenv import load_dotenv
import pandas as pd
import zipfile
import os


class DatasetLoader:

    def __init__(
        self,
        data_dir="data/raw",
        repo=None,
        dataset=None,
        file_name=None
    ):
        self.data_dir = Path(data_dir)
        self.repo = repo
        self.dataset = dataset
        self.file_name = file_name

        self.data_dir.mkdir(parents=True, exist_ok=True)

    def authenticate(self):

        username = os.getenv("KAGGLE_USERNAME")
        token = os.getenv("KAGGLE_API_TOKEN")

        if not username or not token:
            raise ValueError(
                "KAGGLE_USERNAME ou KAGGLE_API_TOKEN não encontrados."
            )

        os.environ["KAGGLE_USERNAME"] = username
        os.environ["KAGGLE_KEY"] = token

        api.authenticate()

    def download(self):

        api.dataset_download_files(
            f"{self.repo}/{self.dataset}",
            path=str(self.data_dir)
        )

        zip_file = self.data_dir / f"{self.dataset}.zip"

        with zipfile.ZipFile(zip_file, "r") as zip_ref:

            csv_name = next(
                file for file in zip_ref.namelist()
                if file.endswith(".csv")
            )

            zip_ref.extract(csv_name, self.data_dir)

            return self.data_dir / csv_name

    def find_csv(self):

        csvs = list(self.data_dir.glob("*.csv"))

        if self.file_name:

            target = self.data_dir / self.file_name

            if target.exists():
                return target

        return csvs[0] if csvs else None

    def clean(self):

        for ext in ("*.zip", "*.pdf"):
            for file in self.data_dir.rglob(ext):
                file.unlink()

    def load_dataframe(
        self,
        sep=";",
        encoding="latin-1"
    ):

        csv_file = self.find_csv()

        if csv_file:
            print(f"Arquivo encontrado: {csv_file}")

        else:

            self.authenticate()

            csv_file = self.download()

            self.clean()

        return pd.read_csv(
            csv_file,
            sep=sep,
            encoding=encoding
        )
    
load_dotenv()

loader = DatasetLoader(
    repo="namespaiva",
    dataset="base-varejo"
)

df = loader.load_dataframe()