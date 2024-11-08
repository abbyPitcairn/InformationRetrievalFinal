# Get unique terms between 2 or 3 data structures
# Future use: encode and compare cosine similarity


def get_unique_terms(target_queries, queries1, queries2=None):
    unique_terms = []
    target_queries = set(target_queries.keys())
    queries1 = set(queries1.keys())

    # If queries2 is provided, convert it to a set; otherwise, use an empty set
    queries2 = set(queries2.keys()) if queries2 else set()

    for query in target_queries:
        # Check if the full query string is unique
        if query not in queries1 and query not in queries2:
            unique_terms.append(query)

    return unique_terms
