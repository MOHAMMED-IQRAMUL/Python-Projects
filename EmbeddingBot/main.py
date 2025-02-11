import google.generativeai as genai
import os
import numpy as np

# Configure the GEMINI API key
os.environ["GEMINI_API_KEY"] = ""  
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Define sentences for embedding
sentence1 = "An array is a non-linear data structure because its elements are stored in a sequential, contiguous order."

# Generate embeddings for sentences
embedding1 = genai.embed_content(model="models/text-embedding-004", content=sentence1)

# Extract embedding vectors
vector1 = np.array(embedding1['embedding'])

# Print the embedding vector
print("Embedding vector for sentence1: ")
print(embedding1)
print()
print("Vector: ")
print(vector1)
