def lower_bound(array,x):
    up,down = len(array),0
    while up - down > 1:
        mid = (up + down) // 2
        if x <= array[mid]:
            up = mid
        else: # x > array[mid]
            down = mid    

    if x = array[down]:
        return down
    else:
        return "not found"

def upper_bound(array,x):
    up,down = len(array),0
    while up - down > 1:
        mid = (up + down) // 2
        if x <= array[mid]:
            up = mid
        else: # x > array[mid]
            down = mid    

    if x = array[up]:
        return up
    else:
        return "not found"
