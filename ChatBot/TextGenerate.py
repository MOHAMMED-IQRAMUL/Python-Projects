# Text Generation

from google import genai


client = genai.Client(api_key='GEMINI_API_KEY')

print()
Query = input("Enter Your Query: ")
print()

response = client.models.generate_content(
    model='gemini-1.5-flash', contents= Query
)

print()
print("Output: ", response.text)
print()
