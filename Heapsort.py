def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (max) element with the last element
        heapify(arr, i, 0)  # Call heapify on the reduced heap

arr=[]
num=int(input("Enter no. of elements:"))
print("Enter the elements:")
for i in range(num):
  a=int(input())
  arr.append(a)

print("Unsorted array:", arr)
heap_sort(arr)
print("Sorted array:", arr)

