from tokenize import String
import QuerySetComparison
import StringMatcher
from QuerySetComparison import query_set_comparison_by_time, get_avg_max_cosine, compare_dice_coefficients_by_region
from StringMatcher import get_avg_query_length, get_longest_query_text, get_avg_query_length_words

# Print data analysis from QuerySetComparison.
# Authors: Abigail Pitcairn and Behrooz Mansouri
# Version: 11.18.2024

# List of category keywords
topics = ["ART", "BEAUTY", "BOOKS", "BUS", "COMP", "FOOD", "HEALTH", "HOBBIES", "JOBS",
          "NEWS", "ONLINE", "PEOPLE", "SHOP", "SPORT", "TRAVEL"]

metro_topics = ["ALL"]

# List of region keywords: United States, Texas, New York, Maine, Maine Metro Areas
regions = ["US","TX","NY", "ME"]
# List of Maine metro area keywords: Bangor, Portland-Auburn, Presque Isle
maine_metro_areas = ["PA", "BA", "PI"]
all_regions = regions + maine_metro_areas

# List of time period keywords
periods = ["12mo", "5yr"]

# Maine Metros' Similarity Scores
# get_avg_max_cosine("12mo", topics, "PA", "ME")
# get_avg_max_cosine("12mo", topics, "BA", "ME")
# get_avg_max_cosine("12mo", topics, "PI", "ME")
#
# get_avg_max_cosine("12mo", topics, "PA", "US")
# get_avg_max_cosine("12mo", topics, "BA", "US")
# get_avg_max_cosine("12mo", topics, "PI", "US")
#
# compare_dice_coefficients_by_region("12mo", topics, "PA", "ME")
# compare_dice_coefficients_by_region("12mo", topics, "BA", "ME")
# compare_dice_coefficients_by_region("12mo", topics, "PI", "ME")
#
# compare_dice_coefficients_by_region("12mo", topics, "PA", "US")
# compare_dice_coefficients_by_region("12mo", topics, "BA", "US")
# compare_dice_coefficients_by_region("12mo", topics, "PI", "US")

# for region in maine_metro_areas:
#    get_avg_query_length("12mo", topics, region)
#    get_avg_query_length_words("12mo", topics, region)
#    get_longest_query_text(region, "12mo", topics)

# # Get maximum cosine similarity score
# get_avg_max_cosine("12mo", topics, "US")
# get_avg_query_length("12mo", topics, "TX")
# get_avg_query_length("12mo", topics, "NY")
# get_avg_query_length("12mo", topics, "ME")
# get_avg_query_length("5yr", topics, "ME")

# Get average query lengths by category, and average of all categories,
# for region/time frame combinations.
# StringMatcher.get_avg_query_length_words("12mo", topics, "US")
# StringMatcher.get_avg_query_length_words("12mo", topics, "TX")
# StringMatcher.get_avg_query_length_words("12mo", topics, "NY")
# StringMatcher.get_avg_query_length_words("12mo", topics, "ME")
# StringMatcher.get_avg_query_length_words("5yr", topics, "ME")

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

# # Print all matching and unique queries between Maine and our 3 regions
# # and Maine 12mo versus Maine 5yr
# print("12mo health queries in TX and ME")
# StringMatcher.find_matching_queries_by_region("12mo", health_topic,"ME", "TX")
# print("12mo health queries in NY and ME")
# StringMatcher.find_matching_queries_by_region("12mo", health_topic, "ME", "NY")
# print("12mo health queries in US and ME")
# StringMatcher.find_matching_queries_by_region("12mo", health_topic, "ME", "US")
#
# print("12mo health queries in ME not TX")
# StringMatcher.find_unique_queries_by_region("12mo", health_topic,"ME", "TX")
# print("12mo health queries in ME not NY")
# StringMatcher.find_unique_queries_by_region("12mo", health_topic, "ME", "NY")
# print("12mo health queries in ME not NY")
# StringMatcher.find_unique_queries_by_region("12mo", health_topic, "ME", "US")
#
# print("12mo health queries in TX not ME")
# StringMatcher.find_unique_queries_by_region("12mo", health_topic,"TX", "ME")
# print("12mo health queries in NY not ME")
# StringMatcher.find_unique_queries_by_region("12mo", health_topic, "NY", "ME")
# print("12mo health queries in US not ME")
# StringMatcher.find_unique_queries_by_region("12mo", health_topic, "US", "ME")
#
# # StringMatcher.find_matching_queries_by_time("12mo","5yr",topics,"ME")
# StringMatcher.find_unique_queries_by_time("12mo", "5yr", health_topic, "ME")
# StringMatcher.find_unique_queries_by_time("5yr", "12mo", health_topic, "ME")

# # Print all dice coefficients and cosine similarities for
# # all topics and all regions for the input time period
# QuerySetComparison.query_set_comparison("12mo", topics)
# QuerySetComparison.query_set_comparison("5yr", topics)

