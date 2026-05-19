import requests
import pandas as pd

def request_data(api):
    try:
        response = requests.get(api, timeout=10)
        print(f"Status da API: {response.status_code} ({response.reason})")
        response.raise_for_status()
        data = response.json()
        return data if isinstance(data, list) else [data]  #Caso a API retorne apenas 1 registro, transforma o dicionario em lista
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        return None

def export_csv(data, file_name, filter_columns=None):
    if not data:
        print("Nenhum dado disponível para exportar.")
        return False

    try:
        df = pd.DataFrame(data)

        if filter_columns:
            existing_columns = [col for col in filter_columns if col in df.columns]
            df = df[existing_columns]

        df.to_csv(file_name, sep=";",index=False, encoding="utf-8")
        print(f"{len(df)} registros exportados para '{file_name}'.")
        return True
    except Exception as e:
        print(f"Erro ao salvar o arquivo CSV: {e}")
        return False

if __name__ == "__main__":
    id_character = list(range(1, 51))

    id_character_format = ",".join(map(str, id_character))

    URL_API = f"https://rickandmortyapi.com/api/character/{id_character_format}"
    OUTPUT_FILE = f"character_RickAndMorty_{id_character[0]}_to_{id_character[-1]}.csv"
    REQUIRED_COLUMNS = ["id", "name", "status", "species", "type", "gender"]

    data_api = request_data(URL_API)

    if data_api:

        export_csv(data_api, OUTPUT_FILE, filter_columns=REQUIRED_COLUMNS)