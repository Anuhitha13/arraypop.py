import array
arr = array.array('i',[1, 4, 3, 1, 6])
print('the created array is:',end=" ")
for i in range(0,5):
    print(arr[i],end=" ")
print("\r")
print("the popped element is:",end=" ")
print(arr.pop(2));
print('the array after popping is:',end=" ")
print('\r')
arr.remove(1)
print('the array after removing is:',end=" ")
for i in range(0,3):
     print(arr[i],end=" ")