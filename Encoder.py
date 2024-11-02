from sentence_transformers import SentenceTransformer, util

# Load the SBERT model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Define your text samples
text1 = "This is the first sample text."
text2 = "This is the second sample text."

# Encode the texts
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)

# Calculate cosine similarity
cosine_similarity = util.cos_sim(embedding1, embedding2).item()

# Display the result
print(f"Cosine Similarity: {cosine_similarity}")