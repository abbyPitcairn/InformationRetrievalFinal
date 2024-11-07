# Compare the data
from sentence_transformers import SentenceTransformer
import numpy as np

# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

ME_data = np.genfromtxt('Data/ME-TOP/ME-BUS.csv', delimiter='\n', dtype=None)

print(ME_data)