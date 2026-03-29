# the steps even though may give overlapping results are shown individually for clarity# since document ids (numbers) in the folder aren't sequential we will sort each posting list after insertion

from nltk import PorterStemmer
import unicodedata
import re

def normalize_tokens(tokens : list):
    
    normalized_tokens = []
    
    for token in tokens:
        
        # convert to lowercase
        token = token.lower()
        
        # strip whitespaces
        token = token.strip()

        # separate accented character into character and accents
        token = unicodedata.normalize('NFKD',token)

        # remove any character that is not a digit or an alphabet
        token = re.sub(r'[^a-z0-9]','',token)

        # don't add empty space cause it will skew up the positions

        if token != "": 
            normalized_tokens.append(token)
        
    return normalized_tokens

def normalize_query(query):
    
    # separating the brackets from the words if they are close to one another
    # this helps standardize query format and prevent splitting to group brackets with words

    query = query.replace('(',' ( ').replace(')',' ) ')
    
    # converting everything to lowercase

    query = query.lower()

    # removing anything that isn't a word, whitespace or bracket

    query = re.sub(r'[^a-z0-9\s\(\)]', '', query)
    query = unicodedata.normalize('NFKD',query)

    # splitting 

    terms = query.split()

    # stemming for consistency (we stem the token in index as well)

    stemmer = PorterStemmer()
    terms[:] = [stemmer.stem(term) for term in terms]
    return terms