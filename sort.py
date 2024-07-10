def sort(array):
    n = len(array) - 1
    for i in range(n):
        for j in range(n-i):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    
    print(array)


array = [2,5,8,1,4,9,6,3,7]
sort(array)


