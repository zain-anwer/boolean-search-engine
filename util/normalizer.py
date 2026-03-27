# the steps even though may give overlapping results are shown individually for clarity

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

        normalized_tokens.append(token)
        
    return normalized_tokens
