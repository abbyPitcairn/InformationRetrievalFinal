from tokenize import String
import QuerySetComparison
import StringMatcher
from QuerySetComparison import query_set_comparison_by_time
from StringMatcher import get_avg_query_length

# Print data analysis from QuerySetComparison.
# Authors: Abigail Pitcairn and Behrooz Mansouri
# Version: 11.18.2024

# List of category keywords
topics = ["ART", "BEAUTY", "BOOKS", "BUS", "COMP", "FOOD", "HEALTH", "HOBBIES", "JOBS",
          "NEWS", "ONLINE", "PEOPLE", "SHOP", "SPORT", "TRAVEL"]

# List of region keywords
regions = ["US","TX","NY"]

# List of time period keywords
periods = ["12mo", "5yr"]


# Get maximum cosine similarity score



# # Get average query lengths by category, and average of all categories,
# # for region/time frame combinations.
# get_avg_query_length("12mo", topics, "US")
# get_avg_query_length("12mo", topics, "TX")
# get_avg_query_length("12mo", topics, "NY")
# get_avg_query_length("12mo", topics, "ME")
# get_avg_query_length("5yr", topics, "ME")

# # Compare queries for dice coefficient and cosine similarity
# # between Maine 12mo and Maine 5yr
# query_set_comparison_by_time("12mo", "5yr", topics)

# # Print all the queries by topic from Maine for last 12mo versus 5yr
# StringMatcher.compare_query_text_by_time("12mo", "5yr", topics, "ME")

# StringMatcher.get_avg_query_length("12mo", topics, "ME")
# StringMatcher.get_avg_query_length("12mo", topics, "TX")
# StringMatcher.get_avg_query_length("12mo", topics, "NY")
# StringMatcher.get_avg_query_length("12mo", topics, "US")
#
# StringMatcher.get_avg_query_length("5yr", topics, "ME")
# StringMatcher.get_avg_query_length("5yr", topics, "TX")
# StringMatcher.get_avg_query_length("5yr", topics, "NY")
# StringMatcher.get_avg_query_length("5yr", topics, "US")

# # Print all queries that are in both Maine and Texas (12 months),
# # Print all queries that are in both Maine and New York (12 months),
# # Print all queries that are in Maine for both 12 months and 5 years.
# StringMatcher.find_matching_queries("12mo", topics,"ME", "TX")
# StringMatcher.find_matching_queries("12mo", topics, "ME", "NY")
# StringMatcher.find_matching_queries_by_time("12mo","5yr",topics,"ME")

# # Print all dice coefficients and cosine similarities for
# # all topics and all regions for the input time period
# QuerySetComparison.query_set_comparison("12mo", topics)
# QuerySetComparison.query_set_comparison("5yr", topics)





