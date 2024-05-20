#Returns the middle element of the dynamic array.
def middle(arr):
    if not arr:
        return None
    
    middle_index=len(arr)//2
    if len(arr)%2==1:
        return arr[middle_index]
    else:
        return arr[middle_index-1],arr[middle_index]
    
arr1=[5,6,7,8,9] # odd case
arr2=[1,2,3,4] #even case

print(middle(arr1))
print(middle(arr2))
