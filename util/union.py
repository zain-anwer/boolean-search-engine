# list1 OR list2

def union(list1,list2):
    
    result = []
    n1 = len(list1)
    n2 = len(list2)
    i = 0
    j = 0
    while i < n1 and j < n2:
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    while i < n1:
        result.append(list1[i])
        i += 1
    
    while j < n2:
        result.append(list2[j])
        j += 1
        
    return result