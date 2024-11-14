import QuerySetComparison

# Use string functions to find unique queries between two regions
# and average query lengths by category by region.
# Authors: Abigail Pitcairn and Behrooz Mansouri
# Version: 11.14.2024

def find_unique_queries(time, topic, region1, region2):
    print(f"For {topic}:")
    set1 = f"Data/{time}/{region1}/{region1}-{topic}.csv"
    set2 = f"Data/{time}/{region2}/{region2}-{topic}.csv"
    queries1 = QuerySetComparison.read_trend_file_to_set(set1)
    queries2 = QuerySetComparison.read_trend_file_to_set(set2)

    unique_queries1 = [query for query in queries1 if query not in queries2]
    print(f"{region1} only: {unique_queries1}")

    unique_queries2 = [query for query in queries2 if query not in queries1]
    print(f"{region2} only: {unique_queries2}\n")

def find_unique_queries_all_topics(time, topics, region1, region2):
    for topic in topics:
        find_unique_queries(time, topic, region1, region2)


def get_avg_query_length(time, topic, region):
    queries_path = f"Data/{time}/{region}/{region}-{topic}.csv"
    queries = QuerySetComparison.read_trend_file_to_set(queries_path)
    total_length = 0
    num_of_queries = 0
    for query in queries:
        total_length += len(query)
        num_of_queries += 1
    return total_length / num_of_queries

def get_avg_query_length_all_topics(time, topics, region):
    total_query_length = 0
    num_of_topics = 0
    for topic in topics:
        total_query_length += get_avg_query_length(time, topic, region)
        num_of_topics += 1
    return total_query_length / num_of_topics



