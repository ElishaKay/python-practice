Just in case:

# Complete the customSort function below.
# Aim: Sort by frequency, then incrementing value
# Example: [3,1,2,2,4] should output [1, 3, 4, 2, 2]

freqDict = {}
items_of_same_freq = []
new_arr = []

def customSort(arr):
    for i in range(len(arr)):
        calculateFreq(arr[i])
    sortByFreq(freqDict,1)
        
def calculateFreq(key):
    if key in freqDict:
        freqDict[key] += 1
    else:
        freqDict[key] = 1

def sortItemsofSameFreq(items):
    lowestVal = 0;
    
        
def sortByFreq(dictionary,currentlyLowestFreq):
    for key in dictionary:
        if dictionary[key] == currentlyLowestFreq:
            for i in range(dictionary[key]):
                items_of_same_freq.append(key)
    sortItemsofSameFreq(items_of_same_freq)
    currentlyLowestFreq += 1
    if all(key in new_arr for key in dictionary):
        for i in range(len(new_arr)): 
            print(new_arr[i]) 
    else:
        sortByFreq(dictionary,currentlyLowestFreq)