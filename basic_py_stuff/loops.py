# LOOPS

#FOR LOOP
people = ['John', 'Sara', 'Tim', 'Bob']
for person in people:
    print('Current Person: ', person)
    
# Iterate by seq index
for i in range(len(people)):
    print('Current Person: ',people[i])
    
for i in range(0, 10):
    print(i)
    
# WHILE lOOP

count = 0
while count <= 10:
    print('Count: ', count)
    if count == 5:
        break
    count = count + 1

# ITC Test

new_arr = []

def getMinimumUniqueSum(arr):
    for i in range(len(arr)):
    	incrementUntilUnique(arr[i])

def incrementUntilUnique(int):
	if int not in new_arr:
    	append(int)
    else:
    	int = int + 1
    	incrementUntilUnique(int)

def append(int)
	new_arr.append(int)

print(new_arr);

