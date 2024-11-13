import csv

from sentence_transformers import SentenceTransformer
from sentence_transformers import util


def read_trend_file_to_set(csv_file_path):
    """
    This method takes in the file path to a trend file and return only the set of queries annotated as top
    @param csv_file_path: file path to trend file
    @return: set of queries in top
    """
    queries = []
    with open(csv_file_path, mode='r', newline='', encoding="utf-8") as file:
        csvFile = csv.reader(file)
        next(csvFile)
        next(csvFile)
        for line in csvFile:
            if len(line) < 2:
                break
            queries.append(line[0].lower())
    return list(set(queries))


def dice_coefficient(list1, list2):
    """
    This method takes in two set of queries and return their dice coefficient
    @param list1: query terms 1
    @param list2: query terms 2
    @return: dice coefficient
    """
    set1 = set(list1)
    set2 = set(list2)

    intersection = set1.intersection(set2)

    return 2 * len(intersection) / (len(set1) + len(set2))


def get_avg_max_cosine(list1, list2):
    model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
    embeddings1 = model.encode(list1, convert_to_tensor=True)
    embeddings2 = model.encode(list2, convert_to_tensor=True)
    similarities = util.semantic_search(embeddings1, embeddings2)
    sum = 0.0
    for item in similarities:
        max_score = item[0]['score']
        sum += max_score
    return sum / len(similarities)


def compare_dice_coefficients():
    Topics = ["ART", "BOOKS", "SHOP", "FOOD", "BEAUTY", "HOBBIES", "TRAVEL", "SPORT", "COMP"]
    Path_to_NY = "newData/NY-5yr/"
    Path_to_TX = "newData/TX-5yr/"
    for topic in Topics:
        ny = Path_to_NY+"NY-"+topic+".csv"
        ny_queries = read_trend_file_to_set(ny)
        tx = Path_to_TX + "TX-" + topic + ".csv"
        tx_queries = read_trend_file_to_set(tx)
        print(topic + f"\t\tDice coefficient: {dice_coefficient(ny_queries, tx_queries)}")

def compare_cosines():
    Topics = ["ART", "BOOKS", "SHOP", "FOOD", "BEAUTY", "HOBBIES", "TRAVEL", "SPORT", "COMP"]
    Path_to_NY = "newData/NY-5yr/"
    Path_to_TX = "newData/TX-5yr/"
    for topic in Topics:
        ny = Path_to_NY+"NY-"+topic+".csv"
        ny_queries = read_trend_file_to_set(ny)
        tx = Path_to_TX + "TX-" + topic + ".csv"
        tx_queries = read_trend_file_to_set(tx)
        print(topic + f"\t\tAvg. Cosine: {get_avg_max_cosine(ny_queries, tx_queries)}")


# Example 1 for dice coefficients: find dice coefficient between two set of queries; e.g. NY vs. TX
compare_dice_coefficients()

# Example 2 for cosine sim: find average of max query similarity between pairs of querys in two sets; e.g. NY vs. TX
compare_cosines()
