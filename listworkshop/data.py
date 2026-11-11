def nameAnalyze(): 
    listName = [ "Stina", "Ahmed", "Pelle" ]
    return listName

def add_toList():
    temp = 24
    temperatureList = [ 12, 34, 2, -24, 4 ]
    temperatureList.append(temp,fromUser)
    return temperatureList

def meanValue(): 
    myList = add_toList()
    sum = 0
    for number in myList:               
        sum = sum + number
    mean = myList / len(myList)
    fruits= ["äpple", "banan"]
