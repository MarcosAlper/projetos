import os
from google import genai
import sys

# Busca a chave na memória do terminal
# O os.getenv busca exatamente a variável definida no PowerShell
api_key_sistema = os.getenv("GEMINI_API_KEY")


# Verificação de segurança (Caso eu esqueça de colar a chave no terminal)
if not api_key_sistema:
    print("""
          Erro: Chave API não encontrada no sistema.
          Use o comando: $env:GEMINI_API_KEY = 'sua_chave' no terminal PowerShell
          """)
    sys.exit()

# Configuração do Cliente usando a variável da memória
client = genai.Client(api_key=api_key_sistema)

# Iniciando a sessão de chat com o modelo que funcionou para você
chat = client.chats.create(model="gemini-flash-lite-latest")

print("--- CHAT GEMINI (Terminal) ---")
print("Digite 'sair' para encerrar a conversa.\n")

while True:
    # Recebe o input do usuário
    user_input = input("Você: ")

    # Condição de saída
    if user_input.lower() in ["sair", "exit", "quit"]:
        print("Encerrando chat...")
        break

    try:
        # Envia a mensagem e recebe a resposta em modo contínuo
        response = chat.send_message(user_input)
        
        # Exibe a resposta
        print(f"\nGemini: {response.text}\n")
        print("-" * 30)

    except Exception as e:
        print(f"\nErro na comunicação: {e}")