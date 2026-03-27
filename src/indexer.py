from pathlib import Path
from util.normalizer import normalize_tokens

# document ids would be generated sequentially starting from zero

def parseFolderAndTokenize(folder_path):
    
    directory = Path(folder_path)
    doc_id : int = 0

    if not directory.is_dir():
        print("Error: Invalid Directory Path")
        return
    
    token_list = []
    
    with open("../data/Stopword List.txt",'r') as stopword_file:
        stopwords = stopword_file.read().split

    for file_path in directory.glob('*.txt'):
        with open(file_path,'r') as file:
            content = file.read()
        
        # tokenize the output based on spaces
        token_list = content.split()
        normalized_token_list = normalize_tokens(token_list)

        # removing stopwords
        final_tokens = [for token in normalized_token_list if token not in stopwords]

        doc_id += 1
    