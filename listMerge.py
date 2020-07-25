#Wilson Wu

def copyList(newList, original):
    for i in range(len(original)):
        newList.append(original[i])
    return newList

def addList(original,add):
    
    for i in range(len(add)):
        duplicate = False
        for j in range(len(original)):
            if original[j] == add[i]:
                duplicate = True
        if duplicate == False:
            original.append(add[i])
    return original

def deleteList(original,delete):
    deleteArray=[]
    for i in range(len(original)):
        for j in range(len(delete)):

            if original[i] == delete[j]:
                deleteArray.append(original[i])

    for i in range(len(deleteArray)):
        original.remove(deleteArray[i])
    return original

def sortByAlpha(start, end , newList, sameSize):

    sameSize.sort()
    sameSize.reverse()
    i=0

    for j in range(start,start+len(sameSize)):
        newList[j] = sameSize[i]
        i+=1

    return newList
    

def getMax(original):
    max = 0
    maxString = ''
    for i in range(len(original)):
        if max < len(original[i]):
            maxString = original[i]
            max = len(original[i])
    return maxString

def orderList(original, add, delete):
    original = addList(original,add)
    original = deleteList(original,delete)

    newList=[]
    currentMax = ''
    maxLength = 0
    length = len(original)
    

    for i in range(length):
        currentMax = getMax(original)

        original.remove(currentMax)       
        newList.append(currentMax)


    start = 0
    end = 0

    j=0
    for i in range(len(newList)):
        sameSize = []
        end = 0
        j=i
        while j < len(newList):
            if len(newList[i]) == len(newList[j]):
                sameSize.append(newList[j])

                start = i
                end +=1
            j+=1
        newList = sortByAlpha(start,end,newList,sameSize)
        





    print("here",newList)


orderList(['a','aa','aaa','aaaa','aba','xxx'],['a','bbb','abcd','zzz'],['aaaa','aba'])