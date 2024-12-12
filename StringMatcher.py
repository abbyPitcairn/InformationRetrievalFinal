import QuerySetComparison

# Use string functions to find unique queries between two regions
# and average query lengths by category by region.
# Authors: Abigail Pitcairn and Behrooz Mansouri
# Version: 11.18.2024

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
    """
    Find unique queries that are in region1 but not region2
    :param time: time period for queries
    :param topics: list of topics to search across
    :param region1: queries that are in region1, but not in region2
    :param region2: queries that are not in region2, but are in region1
    :return:
    """
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
    print(f"Queries for {region} in both {time1} and {time2}:")
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
    print(f"Queries for {region} in {time1} that are not in {time2}:")
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
        try:
            queries = QuerySetComparison.read_trend_file_to_set(queries_path)
        except FileNotFoundError:
            print(f"{queries_path} not found. Skipping...")
            continue
        except Exception as e:
            print(f"An error occurred while reading {queries_path}: {e}")
            continue
        total_length = 0
        num_of_queries = 0
        for query in queries:
            total_length += len(query)
            num_of_queries += 1
        average_length = total_length / num_of_queries
        #print(f"{topic}: {average_length}")
        total_average += average_length
    print(f"Average length for {region}, {time} for all topics: {total_average/len(topics)} characters.")


def get_avg_query_length_words(time, topics, region):
    total_average = 0
    for topic in topics:
        queries_path = f"Data/{time}/{region}/{region}-{topic}.csv"
        try:
            queries = QuerySetComparison.read_trend_file_to_set(queries_path)
        except FileNotFoundError:
            print(f"{queries_path} not found. Skipping...")
            continue
        except Exception as e:
            print(f"An error occurred while reading {queries_path}: {e}")
            continue
        total_length = 0
        num_of_queries = 0
        for query in queries:
            total_length += query.count(" ")
            total_length += 1
            num_of_queries += 1
        average_length = total_length / num_of_queries
        #print(f"{topic}: {average_length}")
        total_average += average_length
    print(f"Average length for {region}, {time} for all topics: {total_average/len(topics)} words.")


def get_avg_query_length_manual(topics):
    avg_length = 0
    for query in topics:
        avg_length += len(query)
    print(f"Average query length: {avg_length/len(topics)}")


def get_longest_query_text(region, time, topics):
    longest_q_by_topic = {}
    for topic in topics:
        queries_path = f"Data/{time}/{region}/{region}-{topic}.csv"
        try:
            queries = QuerySetComparison.read_trend_file_to_set(queries_path)
        except FileNotFoundError:
            print(f"{queries_path} not found. Skipping...")
            continue
        max_length_query = queries[0]
        for query in queries:
            if len(query) > len(max_length_query):
                max_length_query = query
        #print(f"{max_length_query} is {len(max_length_query)} characters.")
        longest_q_by_topic[topic] = max_length_query
    max_length_query = ""
    for query in longest_q_by_topic.values():
        if len(query) > len(max_length_query):
            max_length_query = query
    topic_w_longest_q = next((k for k, v in longest_q_by_topic.items() if v == max_length_query), None)
    print(f"Longest query is {max_length_query} from {topic_w_longest_q} at {len(max_length_query)} chars.")




