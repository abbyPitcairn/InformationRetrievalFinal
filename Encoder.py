from sentence_transformers import util

def encoding(bert_model, queries):
    q_scores = {}
    for q in queries:
        q_score = bert_model.encode(q)
        q_scores[q] = q_score
    return q_scores

def compare(encoded_queries1, encoded_queries2):
    cosine_sim_scores = {}
    for q1 in encoded_queries1:
        for q2 in encoded_queries2:
            cosine_sim = util.cos_sim(q1, q2).item()
            cosine_sim_scores[q1,q2] = cosine_sim
    return cosine_sim_scores

def avg_scores(cosine_sim_scores):
    return sum(cosine_sim_scores)/len(cosine_sim_scores)

def get_avg_scores(bert_model, queries1, queries2):
    encoded_queries1 = encoding(bert_model, queries1)
    encoded_queries2 = encoding(bert_model, queries2)
    cosine_sim_scores = compare(encoded_queries1, encoded_queries2)
    return avg_scores(cosine_sim_scores)

def get_unique_terms(target_queries, queries1, queries2):
    unique_terms = []
    term_set1 = queries1.split()
    term_set2 = queries2.split()
    for query in target_queries:
        for term in query:
            if term not in term_set1 and term not in term_set2:
                unique_terms.append(term)
    return unique_terms

def read_in_trends(filepath):






