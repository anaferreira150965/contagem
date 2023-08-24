import os
import openai
import dotenv

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
prompt_sistema = """
Você é um categorizador de produtos.
Você deve escolher uma categoria da lista abaixo:
##### Lista de categorias válidas
Beleza
Entretenimento
Esportes
Outros
##### Exemplo
bola de tenis
Esportes
"""

resposta = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
          "role": "system",
          "content": prompt_sistema
        },
        {
            "role": "user",
            "content": "bola de tenis de mesa"
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    n=5
)
for i in range(0,5):
    print(resposta.choices[i].message.content)
    print("-------------------")
