# Complete the function below.

# def first_index_of_an_integer(arr, integer_to_look_for):

def first_index_of_an_integer(arr, integer_to_look_for):
    for i in range(len(arr)):
        if arr[i] == integer_to_look_for:
            print(i)
            return
            # print('currently at iteration #:',i)
    print(-1)


for i in range(len(operations)):
	eval(operations[i])