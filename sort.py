def shellSort(arr): 
    n = len(arr) 
    gap = n//2 
    while gap > 0:  
        for i in range(gap,n):  
            temp = arr[i] 
  
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
 		print(arr)
            arr[j] = temp 
        gap //= 2

l = [1, 5, 2, 9, 12, 17, 1, 3]

shellSort(l)
