# Get unique terms between 2 or 3 data structures
# Future use: encode and compare cosine similarity
from sentence_transformers import SentenceTransformer

# For future use with cosine similarity of queries:
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


def get_unique_terms(target_queries, queries1):
    unique_terms = []
    target_queries = set(target_queries.keys())
    queries1 = set(queries1.keys())

    for query in target_queries:
        # Check if the full query string is unique
        if query not in queries1:
            unique_terms.append(query)

    return unique_terms
