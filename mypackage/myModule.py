def top_n(items,n):
    """Return top n items in array in descending order
    
    Args:
        items (array) list or array-like object
        n (int) nums of items to return

    Return:
        array: top n i items in desc order

    Expl:
        >>> top_n([8,3,2,7,4],3)
        [8,7,3]
    """
    for i in range(n): #keep sorting until we have the to n items
        for j in range(len(items)-i-i):

            if items [j] > items[j+1]: #if this item is bigger than next item...
                items[j],items[j+1]=items[j+1],items[j] #swap the two!

    #get last two items
    top_n = items[-n:]

    #return in descing order 
    return top_n[::-1]