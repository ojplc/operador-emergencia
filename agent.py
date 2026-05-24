import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
API_KEY = os.getenv('API_KEY')

SYSTEM_PROMPT = open("system_prompt.txt", 'r', encoding="utf-8").read()

client = genai.Client(api_key= API_KEY)

chat = client.chats.create(model="gemini-3.5-flash", config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT))
print("Simulação de ligação ao 190\n")
mensagem = "*Comece a ligação*"

while True:
    if mensagem != "":
        print("Operador: ")
        response = chat.send_message_stream(mensagem)
        print("\n")
        for chunk in response:
            print(chunk.text, end="")
    else: break
    mensagem = input("\nUser: ")
    print("\n")
