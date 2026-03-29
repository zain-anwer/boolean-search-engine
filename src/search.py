from util.normalizer import normalize_tokens, normalize_query
from util.intersect import intersect
from util.union import union
from util.negate import negate
from util.proximity_intersect import proximity_intersect
from src.indexer import createInvertedIndex

from util.postfix_converter import convert_to_postfix
from nltk import PorterStemmer
import json 
import time

def search(query:str):
    
    createInvertedIndex("data/Trump Speeches/")

    terms = normalize_query(query)
    print(terms)
    
    # read the index to pass it on
    
    index = None
    with open("index.json","r") as f:
        index = json.load(f)

    # used to differentiate queries

    boolean_search = False
    
    for keyword in ['and','or','not']:
        if keyword in terms:
            boolean_search = True
            break
    
    if (len(terms) == 1):
        boolean_search = True

    if (boolean_search):
        return booleanSearch(terms,index["inverted"])
    
    else:
        
        # here we handle implicit proximity queries (phrase queries) like hillary clinton
        
        # value will be zero if k not given
        
        val = 0
        
        # otherwise val would be k
        
        if len(terms) > 2:
            val = int(terms[2]) # converting it into integer from string

        # --- checking if words exist before searching or else it'll throw a type errorrr ---
        
        if terms[0] not in index["positional"] or terms[1] not in index["positional"]:
            return []

        return proximitySearch(terms[0],terms[1],val,index["positional"])


def booleanSearch(tokens,index):
    
    # get tokens into a postfix order for evaluation
    output_queue = convert_to_postfix(tokens)
   
    # evaluation using a stack
    eval_stack = []

    # all doc_ids in case we have queries like NOT (A AND B)
    # otherwise we will just use it a binary operation like A AND NOT B
    
    universe_set = set()
    for posting_list in index.values():
        universe_set.update(posting_list)
    
    all_doc_ids = sorted(list(universe_set))


    for token in output_queue:
        
        if token == 'AND':
        
            right, left = eval_stack.pop(), eval_stack.pop()
        
            # smallest list first for efficiency in AND operation
            
            if len(left) > len(right): left, right = right, left
            eval_stack.append(intersect(left,right))
        
        elif token == 'OR':
        
            right, left = eval_stack.pop(), eval_stack.pop()

            # apparently greater efficiency (minute difference though when the first list is longer is OR operation)
            
            if len(left) < len(right): left, right = right, left
            eval_stack.append(union(left,right))
        
        elif token == 'NOT':

            operand = eval_stack.pop()
            eval_stack.append(negate(all_doc_ids,operand))
        
        else:

            # pushing our doc_id list here
            if isinstance(token, list):
                # converting all of them to integer for comparison operators
                eval_stack.append([int(i) for i in token])
            else:
                # Use .get() to avoid KeyErrors for words not in the speeches
                eval_stack.append(index.get(token, []))

    return sorted(eval_stack[0], key=int) if eval_stack else []


def proximitySearch(t1,t2,k,index):
    return proximity_intersect(index[t1],index[t2],k)