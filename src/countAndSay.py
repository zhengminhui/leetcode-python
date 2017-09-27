def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    oldStr = '1'
    for i in range(n -1):
        tmp = ''
        count = 1
        for j in range(1,len(oldStr)+1):
            if j<len(oldStr) and oldStr[j] == oldStr[j -1]:
                count += 1
            else:
                tmp += str(count) + oldStr[j-1]
                count = 1
                print tmp
        oldStr = tmp
    return oldStr
            

        



print countAndSay(4)  
# print countAndSay(4)  #1211
# print countAndSay(5)  #111221
# 
# print countAndSay(11)  #11131221133112132113212221
