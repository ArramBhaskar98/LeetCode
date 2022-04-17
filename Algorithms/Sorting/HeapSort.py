class Heap:
    def heapify(self, heap):
        

        def subHeapify(A, n, i):
            largest = i
            l = 2*i + 1
            r = 2*i + 2

            if l < n and A[l] > A[largest]:
                largest = l
            if r < n and A[r] > A[largest]:
                largest = r
            if largest != i:
                # temp = A[i]
                A[i] = A[largest]
                A[largest] = A[i]
                subHeapify(A, n, largest)
            print(A)

        n = len(heap)
        for i in range(n//2 - 1, -1, -1):
            subHeapify(heap, n, i)
        for i in range(n-1, 0, -1):
            heap[i] = heap[0]
            heap[0] = heap[i]
            subHeapify(heap, i, 0)
        return heap



if __name__ == "__main__":
    sol = Heap()
    tests = [dict(heap = [20,10,30,40,60,70,80], Output = [80,70,60,40,30,20,10])]
    for test in tests:
        assert sol.heapify(test['heap']) == test['Output']
        print("-------------------------------------------")