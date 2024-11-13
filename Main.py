import Encoder
import DataLoader

# Create data structures
me_12mo = DataLoader.load_top_data("Data/ME-12mo")
us_12mo = DataLoader.load_top_data("Data/US-12mo")
me_5yr = DataLoader.load_top_data("Data/ME-5yr")
us_5yr = DataLoader.load_top_data("Data/US-5yr")

# Example usage to view data:
# print(f"Top US job queries over past 12 months: {us_12mo["JOBS"]}")

# Example usage to extract unique terms between two regions from one category
cat = "HEALTH"
print(f"Terms in Maine, not US: {Encoder.get_unique_terms(me_5yr[cat], us_5yr[cat])}")
print(f"Terms in US, not Maine: {Encoder.get_unique_terms(us_5yr[cat], me_5yr[cat])}")
