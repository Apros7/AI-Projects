def linear_search(arr : list, v : int):
    for i, el in enumerate(arr): 
        if el == v:
            return True
    return False

