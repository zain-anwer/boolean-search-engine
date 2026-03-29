from src.indexer import createInvertedIndex
from util.proximity_intersect import proximity_intersect
import json

inverted_index = createInvertedIndex("data/Trump Speeches/")
# print(inverted_index)

index = None
with open("index.json","r") as f:
    index = json.load(f)

dict1 = index["positional"]["after"]
dict2 = index["positional"]["years"]

print(proximity_intersect(dict1,dict2,1))