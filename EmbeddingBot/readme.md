# Generating Embeddings with Google Generative AI

This example demonstrates how to generate embeddings for a sentence using the Google Generative AI library.

## Prerequisites

- Install the `google-generativeai` library.
- Set up your GEMINI API key.

## Code

```python
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
```

### Explanation

1. **Import Libraries**: Import the necessary libraries including `google.generativeai`, `os`, and `numpy`.
2. **Configure API Key**: Set up the GEMINI API key in the environment variables.
3. **Define Sentence**: Define the sentence for which you want to generate the embedding.
4. **Generate Embedding**: Use the `embed_content` method to generate the embedding for the sentence.
5. **Extract and Print Vector**: Extract the embedding vector and print it.

### Output

The code will output the embedding vector for the given sentence.
