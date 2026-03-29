# assuming list1 AND NOT list2

def negate(list1,list2):
    
    result = []
    n1 = len(list1)
    n2 = len(list2)
    i = 0
    j = 0

    while i < n1 and j < n2:
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else: 
            j += 1        # list 2 value is smaller so it can contain current list1[i]

    while i < n1:
        result.append(list1[i])
        i += 1        
    
    return result