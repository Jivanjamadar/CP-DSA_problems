#Splits the dynamic array into two dynamic arrays at the specified index.

def split_arr(arr,index):
    if 0 <= index <len(arr):
        return arr[:index],arr[index:]
    else:
        raise IndexError("Index out of bounds")

arr=[4,5,6,-1,3]
split= 2
left,right=split_arr(arr,split)
print("Left_array :",left)
print("Right_array :",right)