import QuerySetComparison
import StringMatcher

# Print data analysis from QuerySetComparison.
# Authors: Abigail Pitcairn and Behrooz Mansouri
# Version: 11.14.2024

topics = ["ART", "BEAUTY", "BOOKS", "BUS", "COMP", "FOOD", "HEALTH", "HOBBIES", "JOBS",
          "NEWS", "ONLINE", "PEOPLE", "SHOP", "SPORT", "TRAVEL"]

regions = ["US","TX","NY"]

for region in regions:
    StringMatcher.find_unique_queries_all_topics("12mo", topics,"ME",region)
    StringMatcher.find_unique_queries_all_topics("5yo", topics, "ME", region)

# Print all dice coefficients and cosine similarities for
# all topics and all regions for the input time period
QuerySetComparison.query_set_comparison("12mo")
QuerySetComparison.query_set_comparison("5yr")





