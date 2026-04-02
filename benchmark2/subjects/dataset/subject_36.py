def findCommonElements(array1, array2):
    commonElements = []
    dictionary = {}
    
    for element in array1:
        dictionary[element] = False
    
    for element in array2:
        if element in dictionary and not dictionary[element]:
            dictionary[element] = True
            commonElements.append(element)
    
    return commonElements