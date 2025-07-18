"""
Randomized Quicksort Implementation
MSCS532 Assignment 3 - Dheeraj Kumar
"""

import random
import time


class SortingMetrics:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.time_taken = 0.0


class RandomizedQuickSort:
    def __init__(self):
        self.metrics = SortingMetrics()
    
    def sort(self, arr):
        if not arr:
            return arr
            
        self.metrics = SortingMetrics()
        start_time = time.time()
        
        arr_copy = arr.copy()
        self._quicksort(arr_copy, 0, len(arr_copy) - 1)
        
        self.metrics.time_taken = time.time() - start_time
        return arr_copy
    
    def _quicksort(self, arr, low, high):
        if low < high:
            pivot_index = self._partition(arr, low, high)
            self._quicksort(arr, low, pivot_index - 1)
            self._quicksort(arr, pivot_index + 1, high)
    
    def _partition(self, arr, low, high):
        # Randomly select pivot
        random_index = random.randint(low, high)
        arr[random_index], arr[high] = arr[high], arr[random_index]
        self.metrics.swaps += 1
        
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            self.metrics.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.metrics.swaps += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.metrics.swaps += 1
        
        return i + 1


class DeterministicQuickSort:
    def __init__(self):
        self.metrics = SortingMetrics()
    
    def sort(self, arr):
        if not arr:
            return arr
            
        self.metrics = SortingMetrics()
        start_time = time.time()
        
        arr_copy = arr.copy()
        self._quicksort(arr_copy, 0, len(arr_copy) - 1)
        
        self.metrics.time_taken = time.time() - start_time
        return arr_copy
    
    def _quicksort(self, arr, low, high):
        if low < high:
            pivot_index = self._partition(arr, low, high)
            self._quicksort(arr, low, pivot_index - 1)
            self._quicksort(arr, pivot_index + 1, high)
    
    def _partition(self, arr, low, high):
        # Use first element as pivot
        arr[low], arr[high] = arr[high], arr[low]
        self.metrics.swaps += 1
        
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            self.metrics.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.metrics.swaps += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.metrics.swaps += 1
        
        return i + 1


def test_algorithms():
    print("Testing Randomized vs Deterministic Quicksort")
    print("=" * 50)
    
    test_cases = {
        "Random": [64, 34, 25, 12, 22, 11, 90, 5],
        "Sorted": [1, 2, 3, 4, 5, 6, 7, 8],
        "Reverse": [8, 7, 6, 5, 4, 3, 2, 1],
        "Duplicates": [5, 2, 8, 2, 9, 5, 3, 2]
    }
    
    rqs = RandomizedQuickSort()
    dqs = DeterministicQuickSort()
    
    for test_name, test_array in test_cases.items():
        print(f"\nTesting {test_name} array: {test_array}")
        
        sorted_r = rqs.sort(test_array)
        r_metrics = rqs.metrics
        
        sorted_d = dqs.sort(test_array)
        d_metrics = dqs.metrics
        
        print(f"Sorted result: {sorted_r}")
        print(f"Randomized - Comparisons: {r_metrics.comparisons}, "
              f"Swaps: {r_metrics.swaps}, Time: {r_metrics.time_taken:.6f}s")
        print(f"Deterministic - Comparisons: {d_metrics.comparisons}, "
              f"Swaps: {d_metrics.swaps}, Time: {d_metrics.time_taken:.6f}s")


if __name__ == "__main__":
    test_algorithms()
