#Q.Find the second largest element . If list has 0 or 1 or all same elements , seclargest number should be None

def largest(list):
    if list == []:
        return None
    else:
        maxnum = list[0]
        for i in range(1,len(list)):
            if list[i] > maxnum:
                maxnum = list[i]
        
        return maxnum

#METHOD 1 - Use of in-built function ( O(1) )
# def seclargest(list):
#     l2= sorted(l1, reverse=True)
#     return l2[1]

#METHOD 2 - 2 iterations ( O(n) )
# def seclargest(list):
#     large=largest(list)
#     seclarge=None
#     for i in list:
#         if i != large:
#             if seclarge ==None:
#                 seclarge = i
#             else:
#                 if i>seclarge:
#                     seclarge = i
#     return seclarge

#METHOD 3 - 1 iterations ( O(n) )
def seclar(list):
    if len(list) <=1:
        return None
    
    large=list[0]
    seclarge= None
    for i in list[1:]:
        if i > large:
            seclarge = large
            large = i   
        
        elif i<large:
            if seclarge == None or  i>seclarge:
                seclarge = i 
        
    return seclarge



l1=[3,1,2,3]
print(seclar(l1))