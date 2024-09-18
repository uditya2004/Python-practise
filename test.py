def read(n, book, target): 
    dict1 = {}

    for i in range(0,n):
        remaining = target - book[i]

        if remaining in dict1:
            return [dict1[remaining], i]
        else:
            dict1[book[i]] = i
    
    return [-1,-1]

book= [3,3]
print(read(len(book),book, target = 6))
