# Heap Sort
<h3><b>Code explanation:<br></b></h3>
heapify function: This function takes an array arr, the size of the heap n, and an index i. It ensures that the subtree rooted at index i follows the max heap property. It compares the parent node with its left and right children, and if needed, swaps the parent with the largest child.
<br>

<br>heap_sort function: This function implements the Heap Sort algorithm. It first builds a max heap using the heapify function by starting from the last parent node and moving up the tree. Then, it repeatedly extracts the maximum element from the heap (root) and swaps it with the last element in the heap. After each swap, it calls heapify on the reduced heap to restore the max heap property.
<hr>

<h3><b>Function explanation:<br></b></h3>
<h4><b>1) heapify:</b></h4>


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
                
i) def heapify(arr, n, i):: This line defines the heapify function, which takes the array arr, the size of the heap n, and the index i as arguments.

ii) largest = i: Initialize a variable largest with the value of the current index i. This will be used to track the index of the largest element among the parent and its two children.

iii) left_child = 2 * i + 1: Calculate the index of the left child of the current parent index i.

iv) right_child = 2 * i + 2: Calculate the index of the right child of the current parent index i.

v) if left_child < n and arr[left_child] > arr[largest]:: This line checks if the left child index is within the heap size n and if the value of the element at the left child index is greater than the value at the largest index. If true, update largest to be the index of the left child.

vi) if right_child < n and arr[right_child] > arr[largest]:: Similar to the previous line, this checks if the right child index is within the heap size n and if the value of the element at the right child index is greater than the value at the largest index. If true, update largest to be the index of the right child.

vii) if largest != i:: After checking both left and right children, this line verifies if the largest element is not the current parent. If they are different, it means that one of the children is larger, and a swap is needed.

viii) arr[i], arr[largest] = arr[largest], arr[i]: Swap the element at the current parent index i with the element at the largest index. This moves the larger element to the parent position.

ix) heapify(arr, n, largest): Recursively call the heapify function on the subtree rooted at the largest index. This ensures that the subtree also maintains the max heap property.

<h4><b>2) heap_sort:</b></h4>


        def heap_sort(arr):
            n = len(arr)
    
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)
    
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i] 
                heapify(arr, i, 0)  

i) def heap_sort(arr):: This line defines the heap_sort function that takes an array arr as an argument.

ii) n = len(arr): This line calculates the length of the input array arr and assigns it to the variable n.

iii) for i in range(n // 2 - 1, -1, -1):: This for loop iterates over the indices of the array that correspond to the parent nodes in a heap. The loop starts from the last parent node and goes backward towards the root node.

iv) heapify(arr, n, i): Inside the loop, the heapify function is called on the array arr, with n as the size of the heap and i as the current index. This step builds the max heap by ensuring that the subtree rooted at index i follows the max heap property.

v) for i in range(n - 1, 0, -1):: This second for loop iterates in reverse order, starting from the last element index and going down to the second element.

vi) arr[i], arr[0] = arr[0], arr[i]: Inside the loop, this line swaps the maximum element (root of the max heap) with the current last element of the heap. This effectively places the maximum element in its correct sorted position at the end of the array.

vii) heapify(arr, i, 0): After swapping, the heapify function is called on the reduced heap, excluding the element that has been moved to its sorted position. This maintains the max heap property on the remaining elements of the heap.
<hr>

# Hamiltonian Cycle
<h3><b>Function explanation:<br></b></h3>
<h4><b>1) is_valid:</b></h4>
i) Here, the function takes four arguments: v (the current vertex being considered), pos (the current position in the path), path (the path being constructed), and graph (the graph's adjacency matrix).

ii) The first condition checks if there is an edge between the last vertex in the path (path[pos - 1]) and the current vertex v. If graph[path[pos - 1]][v] is 1, it means there's an edge, and the condition is satisfied. If it's not 1, it means there's no edge, so the function returns False, indicating that adding vertex v to the path at the current position is not valid.

iii) The second condition checks whether the current vertex v is already present in the path. The in keyword checks if v is a member of the path list. If it is, it means that adding v would create a duplicate in the path, which is not allowed for a Hamiltonian Cycle. In this case, the function returns False.

iv) If both conditions above are not met, it means that adding vertex v to the path at the current position is valid. Therefore, the function returns True.

<h4><b>2) hamiltonian_cycle_util:</b></h4>

i) The hamiltonian_cycle_util function takes three arguments: graph (the graph's adjacency matrix), path (the current path being constructed), and pos (the current position in the path).

ii) The first condition checks if pos has reached the length of the graph. If it has, it means that all vertices have been visited, and it's time to check if a Hamiltonian Cycle exists. To do this, the function checks if there's an edge from the last vertex in the path (path[pos - 1]) back to the starting vertex (path[0]). If this edge exists (i.e., graph[path[pos - 1]][path[0]] is 1), then a valid cycle has been formed, and the function returns True. If there's no edge between the last and starting vertices, it returns False, indicating that no Hamiltonian Cycle exists.

iii)  
        
      for v in range(1, len(graph)):
        if is_valid(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            path[pos] = -1
      return False
      
This part of the function is responsible for attempting to add the next vertex to the path. It iterates over all vertices (excluding the starting vertex, which is always at index 0) and checks if adding each vertex v to the path is valid according to the is_valid function. If adding v is valid, it sets path[pos] to v and makes a recursive call to hamiltonian_cycle_util with an incremented position pos + 1.

If the recursive call returns True, it means that a valid Hamiltonian Cycle has been found, and the function immediately returns True.

If the recursive call returns False or completes without finding a cycle, the vertex v is removed from the path by setting path[pos] to -1 (backtracking).
If no Hamiltonian Cycle is found for the current configuration of the path and graph, the function returns False.

<h4><b>2) hamiltonian_cycle_util:</b></h4>

i)  

        path = [-1] * len(graph)
        path[0] = 0

Here, the path list is initialized. It will hold the vertices of the Hamiltonian Cycle being constructed. The length of the path list is set to match the number of vertices in the graph. The starting vertex (vertex 0) is placed at the beginning of the path.

ii) 


        if not hamiltonian_cycle_util(graph, path, 1):
                print("No Hamiltonian Cycle exists")
        return False

This part of the code uses the hamiltonian_cycle_util function to attempt to find a Hamiltonian Cycle. The hamiltonian_cycle_util function starts building the path from position 1 (pos = 1), as the starting vertex is already in place (path[0] = 0).

If the hamiltonian_cycle_util function returns False, it means that no Hamiltonian Cycle could be found starting from the current configuration. In that case, the function prints a message indicating that no Hamiltonian Cycle exists and returns False.

iii)


        print("Hamiltonian Cycle exists:")
        for vertex in path:
                print(vertex, end=" ")
        print(path[0])

If the hamiltonian_cycle_util function returns True, it means a Hamiltonian Cycle has been found. The code prints a message indicating that a Hamiltonian Cycle exists and then prints the vertices of the cycle. The loop iterates over each vertex in the path list and prints it. Finally, the first vertex (starting vertex) is printed again to complete the cycle.















