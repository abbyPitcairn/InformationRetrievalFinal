import QuerySetComparison

# Use string functions to find unique queries between two regions
# and average query lengths by category by region.
# Authors: Abigail Pitcairn and Behrooz Mansouri
# Version: 11.17.2024

def find_matching_queries_by_region(time, topics, region1, region2):
    for topic in topics:
        print(f"For {topic}:")
        set1 = f"Data/{time}/{region1}/{region1}-{topic}.csv"
        set2 = f"Data/{time}/{region2}/{region2}-{topic}.csv"
        queries1 = QuerySetComparison.read_trend_file_to_set(set1)
        queries2 = QuerySetComparison.read_trend_file_to_set(set2)
        same_queries = [query for query in queries1 if query in queries2]
        for same_query in same_queries:
            print(same_query)
        print("\n")


def find_unique_queries_by_region(time, topics, region1, region2):
    for topic in topics:
        print(f"For {topic}:")
        set1 = f"Data/{time}/{region1}/{region1}-{topic}.csv"
        set2 = f"Data/{time}/{region2}/{region2}-{topic}.csv"
        queries1 = QuerySetComparison.read_trend_file_to_set(set1)
        queries2 = QuerySetComparison.read_trend_file_to_set(set2)
        unique_queries = [query for query in queries1 if query not in queries2]
        for unique_query in unique_queries:
            print(unique_query)
        print("\n")


def find_matching_queries_by_time(time1, time2, topics, region):
    for topic in topics:
        print(f"For {topic}:")
        set1 = f"Data/{time1}/{region}/{region}-{topic}.csv"
        set2 = f"Data/{time2}/{region}/{region}-{topic}.csv"
        queries1 = QuerySetComparison.read_trend_file_to_set(set1)
        queries2 = QuerySetComparison.read_trend_file_to_set(set2)
        same_queries = [query for query in queries1 if query in queries2]
        for same_query in same_queries:
            print(same_query)
        print("\n")


def find_unique_queries_by_time(time1, time2, topics, region):
    for topic in topics:
        print(f"For {topic}:")
        set1 = f"Data/{time1}/{region}/{region}-{topic}.csv"
        set2 = f"Data/{time2}/{region}/{region}-{topic}.csv"
        queries1 = QuerySetComparison.read_trend_file_to_set(set1)
        queries2 = QuerySetComparison.read_trend_file_to_set(set2)
        unique_queries = [query for query in queries1 if query not in queries2]
        for unique_query in unique_queries:
            print(unique_query)
        print("\n")


def compare_query_text_by_region(time, topics, region1, region2):
    print(f"Queries in {region1} compared to {region2} for {time}:")
    find_matching_queries_by_region(time, topics, region1, region2)
    print(f"Queries in {region1} only:")
    find_unique_queries_by_region(time, topics, region1, region2)
    print(f"Queries in {region2} only:")
    find_unique_queries_by_region(time, topics, region2, region1)


def compare_query_text_by_time(time1, time2, topics, region):
    print(f"Queries in {time1} compared to {time2} for {region}:")
    find_matching_queries_by_time(time1, time2, topics, region)
    print(f"Queries in {time1} only:")
    find_unique_queries_by_time(time1, time2, topics, region)
    print(f"Queries in {time2} only:")
    find_unique_queries_by_time(time2, time1, topics, region)


def get_avg_query_length(time, topics, region):
    total_average = 0
    for topic in topics:
        queries_path = f"Data/{time}/{region}/{region}-{topic}.csv"
        queries = QuerySetComparison.read_trend_file_to_set(queries_path)
        total_length = 0
        num_of_queries = 0
        for query in queries:
            total_length += len(query)
            num_of_queries += 1
        average_length = total_length / num_of_queries
        print(f"{topic}: {average_length}")
        total_average += average_length
    print(f"Average length for {region}, {time} for all topics: {total_average/len(topics)}")





