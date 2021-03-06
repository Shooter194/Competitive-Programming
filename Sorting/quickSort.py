


### Quick Sort ####

def partition(arr,l,r):
    pivot = arr[r]
    
    i = l-1
    
    for j in range(l,r):
        if arr[j] < pivot:
            i += 1
            
            arr[i],arr[j] = arr[j],arr[i]
            
    arr[i+1],arr[r] = arr[r],arr[i+1]
    
    return i+1
    
def quickSort(arr,l,r):

    if r > l:
        pi = partition(arr,l,r)
        
        quickSort(arr,l,pi-1)
        quickSort(arr,pi+1,r)
        
if __name__ == "__main__":

    arr = [10,7,8,9,1,5]
    quickSort(arr,0,len(arr)-1)
    
    print (arr)