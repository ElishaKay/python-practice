# Complete the customSort function below.
# Aim: Sort by frequency, then incrementing value
# Example: [3,1,2,2,4] should output [1, 3, 4, 2, 2]

freqDict = {}
new_arr = []

def customSort(arr):
    for i in range(len(arr)):
        incrementFreq(arr[i])
    sortByFreq(freqDict,1)
        
def incrementFreq(key):
    if key in freqDict:
        freqDict[key] += 1
    else:
        freqDict[key] = 1
        
def sortByFreq(dictionary,currentlyLowestFreq):
    for key in dictionary:
        if dictionary[key] == currentlyLowestFreq:
            for i in range(dictionary[key]):
                new_arr.append(key)
    currentlyLowestFreq += 1
    if all(key in new_arr for key in dictionary):
        # print(new_arr)
        for i in new_arr:
            print(new_arr[i])
        # return new_arr    
    else:
        sortByFreq(dictionary,currentlyLowestFreq)