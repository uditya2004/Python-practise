"""
We are swapping start and end element , then move both start and end pointers inwards and swap again.

1. in odd length list star and end index pointers will overlap(becomes same).
2. in even length list , in final iteration, startindex moves ahead of endindex.
"""
def rev(list):
    startindex=0
    endindex=len(list)-1

    while startindex<endindex:

        list[startindex], list[endindex]=list[endindex], list[startindex]

        startindex +=1
        endindex -=1
    
    return list

l=[10,20,30,40]
l2=["ab","bc","cd"]
print(rev(l))
print(rev(l2))