#first answer

def selSort(arr, n):
    
    for index in range(n):
        minIndex = index
 
        for j in range(index + 1, n):

            if arr[j] < arr[minIndex]:
                minIndex = j

        (arr[index], arr[minIndex]) = (arr[minIndex], arr[index])
 
Inarr = [5,416,54,21,6135,15,741]
n = len(Inarr)
selSort(Inarr, n)
print('The array after using the selection sorting is :')
print(Inarr)
