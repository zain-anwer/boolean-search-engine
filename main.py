from src.indexer import createInvertedIndex
from util.proximity_intersect import proximity_intersect
from util.normalizer import normalize_tokens
import json
from src.search import search

inverted_index = createInvertedIndex("data/Trump Speeches/")
# print(inverted_index)


print(search("NOT Hammer"))
