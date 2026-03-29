from pathlib import Path                       # to loop over directory
from util.normalizer import normalize_tokens   # to normalize tokens
import re                                      # to extract doc_id from name
import json                                    # to store indexes in json file
from nltk import PorterStemmer                 # for stemming


# document ids are being extracted through document names
# instead of removing stopwords before addition to inverted_index/positional_index, we skip them to keep the position values of each word accurate

def createInvertedIndex(folder_path):

    # check whether the index file exists if so then return

    index_file_path = Path("index.json")
    if index_file_path.exists():
        print("Index already exists")
        return
    print("Generating Indexes")
    
    
    # inverted index implemented as python dict
    inverted_index = {}

    # positional index implemented as nested dict with list as values
    positional_index = {}

    directory = Path(folder_path)

    if not directory.is_dir():
        print("Error: Invalid Directory Path")
        return
    
    with open("data/Stopword List.txt",'r') as stopword_file:
        stopwords = stopword_file.read().split()

    # create stemmer
    stemmer = PorterStemmer()

    for file_path in directory.glob('*.txt'):
        
        doc_id = re.sub(r'[^0-9]','',file_path.name)
        doc_id = int(doc_id)

        with open(file_path,'r') as file:
            content = file.read()
        
        # tokenize the output based on spaces
        token_list = re.split(r'[\s,.?!\-/\\()\[\]"\'\:]+',content)
        normalized_token_list = normalize_tokens(token_list)

        for position, token in enumerate(normalized_token_list):
            
            # skipping stopwords
            if token in stopwords:
                continue;
            
            # reducing token to it's stem
            token = stemmer.stem(token)

            # adding tokens to inverted_index
            
            if token in inverted_index:
                if doc_id not in inverted_index[token]:
                    inverted_index[token].append(doc_id)
            else:
                inverted_index[token] = [doc_id]

            # adding tokens to positional_index

            if token not in positional_index:
                positional_index[token] = {}

            if doc_id not in positional_index[token]:
                positional_index[token][doc_id] = []
                
            positional_index[token][doc_id].append(position)

            

    # we will sort the posting lists now (because documents aren't stored in-order)

    for posting_list in inverted_index.values():
        posting_list.sort()
    
    for token in positional_index.keys():
        for doc_id in positional_index[token]:
            positional_index[token][doc_id].sort()

    with open("index.json","w") as f:
        data = {
            "inverted":inverted_index, 
            "positional":positional_index
        }
        json.dump(data,f)
    print("Indexes saved to disk successfully!")

def main():
    createInvertedIndex()

if __name__ == "__main__":
    main()