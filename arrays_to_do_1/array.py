from hashlib import new
import random

# Shuffle

def shuffle(arr):
    new_arr = []
    for i in range(len(arr)):
        random_index = random.randint(0,len(arr) - 1)
        new_arr.append(arr[random_index])
        arr.pop(random_index)
    return new_arr

print(shuffle([43,21,78,9,7,2]))


# Skyline heights

def skyline(arr):
    new_arr = []
    last_tallest = 0
    for i in range(len(arr)):
        print(i)
        if arr[i] > 0 and arr[i] > last_tallest:
            # arr.pop(i)
            new_arr.append(arr[i])
    print(new_arr)
skyline([-1,-5,1,1,7,-3])

# Zip it

def zip_it(arr1, arr2):
    larger_arr= arr1 if len(arr1)> len(arr2) else arr2
    new_arr=[]
    for i in range(len(larger_arr)):
        if i <= (len(arr1))-1:
            new_arr.append(arr1[i])
        if i <= (len(arr2))-1:
            new_arr.append(arr2[i])
    return new_arr

