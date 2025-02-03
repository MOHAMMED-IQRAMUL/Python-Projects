# Text Generation

from google import genai


client = genai.Client(api_key='Gemini_API_Key')

print()
Query = input("Enter Your Query: ")
print()

response = client.models.generate_content(
    model='gemini-1.5-flash', contents= Query
)

print()
print("Output: ", response.text)
print()
