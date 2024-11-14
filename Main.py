import QuerySetComparison

# Print data analysis from QuerySetComparison.
# Authors: Abigail Pitcairn and Behrooz Mansouri
# Version: 11.14.2024

# Set the time period for printed results
period = "12mo"  # or "5yr"

# Dice coefficient and cosine similarity for Maine and US
print(f"Maine vs. US {period}:")
QuerySetComparison.compare_dice_coefficients(period,"ME","US")
QuerySetComparison.compare_cosines(period, "ME", "US")

# Dice coefficient and cosine similarity for Maine and Texas
print(f"Maine vs. Texas {period}:")
QuerySetComparison.compare_dice_coefficients(period,"ME","TX")
QuerySetComparison.compare_cosines(period, "ME", "TX")

# Dice coefficient and cosine similarity for Maine and New York
print(f"Maine vs. New York {period}:")
QuerySetComparison.compare_dice_coefficients(period,"ME","NY")
QuerySetComparison.compare_cosines(period, "ME", "NY")
