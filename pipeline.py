import pandas as pd
import numpy as np
import openai

api_key = "sk-...BH5h"
openai.api_key = api_key

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50  # Ajuste o número de tokens conforme necessário
    )
    return response.choices[0].text

def extract_data():
    data = pd.read_csv('dados.csv')
    return data

def transform_data(data):

    data['nova_coluna'] = data['coluna_existente'] * 2
    data['outra_coluna'] = np.log(data['outra_coluna'])
    return data


def load_data(data):
    data.to_csv('dados_transformados.csv', index=False)
    print("Dados carregados com sucesso!")

def etl_pipeline():
    data = extract_data()
    data = transform_data(data)
    
    for index, row in data.iterrows():
        question = f"Qual é o significado da coluna '{row['coluna_existente']}'?"
        answer = chat_with_gpt(question)
        data.at[index, 'significado'] = answer

    load_data(data)

if __name__ == "__main__":
    etl_pipeline()
