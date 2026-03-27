from util.normalizer import normalize_tokens

raw_tokens = ["Réseau", "123-GO!", "Niño", "Café??", "Python3.1"]

print(normalize_tokens(raw_tokens))
with open("data/Stopword List.txt",'r') as stopword_file:
        stopwords = stopword_file.read().split()

print(stopwords)