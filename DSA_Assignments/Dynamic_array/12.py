"""Returns the index of the first occurrence of the specified element in the dynamic 
array, or -1 if the element is not found."""

def find_index(arr,value):
    try:
        index=arr.index(value)
        return index
    except ValueError:
        return -1
arr=[1,2,3,4,5]
value=3
value1=0 
print(find_index(arr,value)) # found case
print(find_index(arr,value1)) #-1 case