import json
import requests
#import pandas as pd


#função para extrair os dados da API DummyJSON
def extract_data(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao extrair dados da API: {response.status_code}")
        return None

def load_data(data, path):
    """dentro da pasta path cria um arquivo json
       com o nome do arquivo sendo o id do nome do arquivo .json"""
    
    id = data["id"]
    with open(f"{path}/{id}.json", "w") as file:
        json.dump(data, file)

endpoint_users = "https://dummyjson.com/users/1"


endpoint_products = "https://dummyjson.com/products/1"


for i in range(1, 10):
    data_users = extract_data(endpoint_users + str(i))
    load_data(data_users, "users")