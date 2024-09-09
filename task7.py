def combine(list1,list2):

    for counter, element in enumerate(list2):
        list1.insert(2*counter + 1, element)
    
    return list1

