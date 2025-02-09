# Chats

import google.generativeai as genai

genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash", system_instruction="You are a ChatBot. You can generate text based on the prompt you receive.")

chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)

print()
op = input("Welcome!, Enter(Y/N) to start the chat: ")
while(op == 'Y'):
    user_input = input("You: ")
    response = chat.send_message(user_input)
    print("ChatBot: ", response.text)
    op = input("Enter(Y/N) to continue the chat: ")
else:
    print("Thank you for using the ChatBot!")

