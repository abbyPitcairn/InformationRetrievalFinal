# Read in the Google Trends data and sort it into categories.
# Categories:
# 1.
# 2.
# 3.
from pytrends.request import TrendReq

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Set parameters without a specific category
geo_location = 'US'  # Use broader scope for more results
timeframe = 'today 12-m'

# Build payload with a relevant keyword
pytrends.build_payload(kw_list=['travel'], timeframe=timeframe, geo=geo_location)

# Retrieve related queries and handle empty results
try:
    related_queries = pytrends.related_queries()
    if 'travel' in related_queries and related_queries['travel']:
        print("Top Travel Queries:")
        print(related_queries['travel']['top'])
        print("Rising Travel Queries:")
        print(related_queries['travel']['rising'])
    else:
        print("No related queries found for the specified parameters.")
except IndexError:
    print("No data available for the selected parameters.")


interest_region = pytrends.interest_by_region(resolution='region')
print(interest_region)


from pytrends.request import TrendReq

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Parameters to get top search results
geo_location = 'US-ME'  # Maine
timeframe = 'today 12-m'  # Last 12 months

# Use the top_charts method to retrieve trending searches
try:
    top_searches = pytrends.top_charts(date='2023', geo=geo_location)
    if top_searches is not None and not top_searches.empty:
        print("Top Searches in Maine (Last 12 Months):")
        print(top_searches)
    else:
        print("No top searches found for Maine in the specified timeframe.")
except Exception as e:
    print(f"An error occurred: {e}")