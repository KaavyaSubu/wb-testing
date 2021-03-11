
def printFib():

    fibList = [0,1]

    while len(fibList <= 10):
        fibList.append(fibList[len(fibList) - 1] + fibList[len(fibList) - 2])

    return fibList

