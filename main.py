from src.indexer import createInvertedIndex

inverted_index = createInvertedIndex("data/Trump Speeches/")
print(inverted_index)