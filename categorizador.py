import os
import openai
import dotenv

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

resposta = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": "Você é um categorizador de produtos"
        },
        {
            "role": "user",
            "content": "escova de dentes"
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
