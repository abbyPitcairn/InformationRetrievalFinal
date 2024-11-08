from sentence_transformers import SentenceTransformer

import Encoder
import DataLoader


# For possible future use with cosine similarity of queries:
# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Create data structures
me_top_data = DataLoader.load_top_data("Data/ME-TOP")
us_top_data = DataLoader.load_top_data("Data/US-TOP")
ww_top_data = DataLoader.load_top_data("Data/WW-TOP")

# Example usage to view data:
# print(f"Top US job queries: {us_top_data["JOBS"]}")

# Example usage to extract unique terms between two regions from one category
cat = "HEALTH"
print(f"Terms in Maine, not US: {Encoder.get_unique_terms(me_top_data[cat], us_top_data[cat])}")
print(f"Terms in US, not Maine: {Encoder.get_unique_terms(us_top_data[cat], me_top_data[cat])}")
