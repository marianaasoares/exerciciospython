arr = [3,4,5,6,6]

z = max(arr)
while max(arr) == z:
    arr.remove(max(arr))

print (max(arr))