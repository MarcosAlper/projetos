from google import genai
import sys

# Configuração do Cliente
client = genai.Client(api_key="AIzaSyAXe1PoDB61uiauIiQpS3bWZF9LmKzPJ_Q")

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