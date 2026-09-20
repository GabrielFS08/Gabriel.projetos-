import json
import requests
import numpy
import pandas as pd


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
endpoint_products = "https://dummyjson.com/products/"

def loop_load_data(endpoint):
    url = "https://dummyjson.com/" + endpoint
    i = 1
    limit = 10
    while True:
        data = extract_data(url + "/" + str(i))
        if data and i < limit:#se o data users tiver alguma coisa...
            load_data(data, "raw/" + endpoint)
        elif i >= limit:
            break
        else:
            print(f"Erro ao extrair dados da API: {data}")
            break
        i += 1

def transform_data_json_to_csv(endpoint, i):
    with open(f"raw/{endpoint}/{i}.json", "r") as file:
        data = json.load(file)
    #convertendo o json para csv
    df = pd.DataFrame(data)
    df.to_csv(f"curated/{endpoint}/{i}.csv", index=False)

endpoints = ["user", "products"]

#for endpoint in endpoints:
    #loop_load_data(endpoint)

transform_data_json_to_csv("user", 1)