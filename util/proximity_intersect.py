from util.intersect import intersect

def proximity_intersect(dict1,dict2,k):
    
    result = []
    
    # find the common doc ids 
    
    common_doc_ids = intersect(list(dict1.keys()),list(dict2.keys()))

    for doc_id in common_doc_ids:

        n1 = len(dict1[doc_id])
        n2 = len(dict2[doc_id])

        i = 0
        j = 0

        # two pointer approach:

        while i < n1 and j < n2:

            # in standard implementations \k means at most k words apart
            # however judging from the test cases this implementation should have absolute/exact distance

            if abs(dict1[doc_id][i] - dict2[doc_id][j]) == k + 1:
                result.append(doc_id)
                break
            if dict1[doc_id][i] < dict2[doc_id][j]:
                i += 1
            else:
                j += 1
    
    result.sort(key=int)
    return result

        