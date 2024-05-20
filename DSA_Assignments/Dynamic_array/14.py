#Resizing the arrays with custom factor given by user (other than 2)
def resize_arr(arr,fact):
    if fact <=0:
        raise ValueError("Resize factor must be greater than 0.")
    new_size=len(arr)*fact
    resized_arr=arr+[None]*(new_size-len(arr))

    return resized_arr

arr=[3,4,5,6,7,8]
factor=2
print(resize_arr(arr,factor))