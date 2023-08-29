# Heap Sort
<h3><b>Code explanation:<br></b></h3>
heapify function: This function takes an array arr, the size of the heap n, and an index i. It ensures that the subtree rooted at index i follows the max heap property. It compares the parent node with its left and right children, and if needed, swaps the parent with the largest child.
<br>

<br>heap_sort function: This function implements the Heap Sort algorithm. It first builds a max heap using the heapify function by starting from the last parent node and moving up the tree. Then, it repeatedly extracts the maximum element from the heap (root) and swaps it with the last element in the heap. After each swap, it calls heapify on the reduced heap to restore the max heap property.
<hr>

<h3><b>Function explanation:<br></b></h3>
<h4><b>1) heapify:</b></h4>
i) def heapify(arr, n, i):: This line defines the heapify function, which takes the array arr, the size of the heap n, and the index i as arguments.

<br>ii) largest = i: Initialize a variable largest with the value of the current index i. This will be used to track the index of the largest element among the parent and its two children.

iii) left_child = 2 * i + 1: Calculate the index of the left child of the current parent index i.

iv) right_child = 2 * i + 2: Calculate the index of the right child of the current parent index i.

v) if left_child < n and arr[left_child] > arr[largest]:: This line checks if the left child index is within the heap size n and if the value of the element at the left child index is greater than the value at the largest index. If true, update largest to be the index of the left child.

vi) if right_child < n and arr[right_child] > arr[largest]:: Similar to the previous line, this checks if the right child index is within the heap size n and if the value of the element at the right child index is greater than the value at the largest index. If true, update largest to be the index of the right child.

vii) if largest != i:: After checking both left and right children, this line verifies if the largest element is not the current parent. If they are different, it means that one of the children is larger, and a swap is needed.

viii) arr[i], arr[largest] = arr[largest], arr[i]: Swap the element at the current parent index i with the element at the largest index. This moves the larger element to the parent position.

ix) heapify(arr, n, largest): Recursively call the heapify function on the subtree rooted at the largest index. This ensures that the subtree also maintains the max heap property.

<h4><b>2) heapify:</b></h4>

i) def heap_sort(arr):: This line defines the heap_sort function that takes an array arr as an argument.

ii) n = len(arr): This line calculates the length of the input array arr and assigns it to the variable n.

iii) for i in range(n // 2 - 1, -1, -1):: This for loop iterates over the indices of the array that correspond to the parent nodes in a heap. The loop starts from the last parent node and goes backward towards the root node.

iv) heapify(arr, n, i): Inside the loop, the heapify function is called on the array arr, with n as the size of the heap and i as the current index. This step builds the max heap by ensuring that the subtree rooted at index i follows the max heap property.

v) for i in range(n - 1, 0, -1):: This second for loop iterates in reverse order, starting from the last element index and going down to the second element.

vi) arr[i], arr[0] = arr[0], arr[i]: Inside the loop, this line swaps the maximum element (root of the max heap) with the current last element of the heap. This effectively places the maximum element in its correct sorted position at the end of the array.

vii) heapify(arr, i, 0): After swapping, the heapify function is called on the reduced heap, excluding the element that has been moved to its sorted position. This maintains the max heap property on the remaining elements of the heap.

