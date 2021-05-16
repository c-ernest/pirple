myUniqueList = []
myLeftovers = []

def addToList(value):

    if value in myUniqueList:
        myLeftovers.append(value)
    else:
        myUniqueList.append(value)

addToList(89)
addToList(90)
addToList(89)
addToList(95)
addToList(80)
addToList(85)
addToList(85)

print(myUniqueList)
print(myLeftovers)



