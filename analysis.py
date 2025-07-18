"""
Algorithm Performance Analysis
MSCS532 Assignment 3 - Dheeraj Kumar

This script analyzes and compares the performance of randomized quicksort
vs deterministic quicksort, and demonstrates hash table operations.
"""

import random
import time
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

try:
    from randomized_quicksort import RandomizedQuickSort, DeterministicQuickSort
    from hash_table_chaining import HashTable
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure src/randomized_quicksort.py and src/hash_table_chaining.py exist")
    sys.exit(1)


def compare_quicksort_algorithms():
    """Compare randomized vs deterministic quicksort on different inputs."""
    print("QUICKSORT PERFORMANCE COMPARISON")
    print("=" * 50)
    
    # Test different array sizes
    sizes = [100, 500, 1000]
    
    for size in sizes:
        print(f"\nTesting with array size: {size}")
        print("-" * 30)
        
        # Generate different types of arrays
        random_array = [random.randint(1, 1000) for _ in range(size)]
        sorted_array = list(range(1, size + 1))
        reverse_array = list(range(size, 0, -1))
        
        test_cases = [
            ("Random", random_array),
            ("Sorted", sorted_array),
            ("Reverse", reverse_array)
        ]
        
        rqs = RandomizedQuickSort()
        dqs = DeterministicQuickSort()
        
        for test_name, test_array in test_cases:
            # Test randomized quicksort
            start_time = time.time()
            rqs.sort(test_array.copy())
            r_time = time.time() - start_time
            r_comparisons = rqs.metrics.comparisons
            
            # Test deterministic quicksort
            start_time = time.time()
            try:
                dqs.sort(test_array.copy())
                d_time = time.time() - start_time
                d_comparisons = dqs.metrics.comparisons
                speedup = d_time / r_time if r_time > 0 else 1
            except RecursionError:
                d_time = float('inf')
                d_comparisons = float('inf')
                speedup = float('inf')
                print(f"{test_name:>8}: Deterministic failed (RecursionError)")
                continue
            
            print(f"{test_name:>8}: Rand={r_time:.4f}s({r_comparisons} comp), "
                  f"Det={d_time:.4f}s({d_comparisons} comp), "
                  f"Speedup={speedup:.2f}x")


def analyze_hash_table():
    """Analyze hash table performance with different load factors."""
    print("\n\nHASH TABLE LOAD FACTOR ANALYSIS")
    print("=" * 50)
    
    table_sizes = [5, 10, 20]
    
    for table_size in table_sizes:
        print(f"\nHash table size: {table_size}")
        print("-" * 25)
        
        ht = HashTable(table_size)
        
        # Insert elements gradually
        for num_elements in [table_size//2, table_size, table_size*2]:
            # Clear and rebuild table
            ht = HashTable(table_size)
            
            # Insert elements
            for i in range(num_elements):
                key = f"key_{i}"
                ht.insert(key, i)
            
            load_factor = ht.get_load_factor()
            chain_lengths = ht.get_chain_lengths()
            max_chain = max(chain_lengths)
            avg_chain = sum(c for c in chain_lengths if c > 0) / len([c for c in chain_lengths if c > 0]) if any(chain_lengths) else 0
            
            # Measure search time
            search_keys = [f"key_{i}" for i in range(min(10, num_elements))]
            start_time = time.time()
            for key in search_keys:
                ht.search(key)
            search_time = (time.time() - start_time) / len(search_keys) if search_keys else 0
            
            print(f"Elements: {num_elements:2d}, Load Factor: {load_factor:.2f}, "
                  f"Max Chain: {max_chain}, Avg Chain: {avg_chain:.2f}, "
                  f"Search Time: {search_time:.6f}s")


def theoretical_analysis():
    """Print theoretical analysis of both algorithms."""
    print("\n\nTHEORETICAL ANALYSIS")
    print("=" * 50)
    
    print("RANDOMIZED QUICKSORT:")
    print("- Average Case: O(n log n)")
    print("- Worst Case: O(n²) - very unlikely due to randomization")
    print("- Best Case: O(n log n)")
    print("- Space: O(log n) average due to recursion depth")
    print("- Key advantage: Eliminates dependence on input order")
    print()
    
    print("DETERMINISTIC QUICKSORT (first element pivot):")
    print("- Average Case: O(n log n)")
    print("- Worst Case: O(n²) - occurs on sorted/reverse sorted input")
    print("- Best Case: O(n log n)")
    print("- Space: O(log n) average, O(n) worst case")
    print("- Problem: Poor performance on already sorted data")
    print()
    
    print("HASH TABLE WITH CHAINING:")
    print("- Insert: O(1) average, O(n) worst case")
    print("- Search: O(1 + α) average, O(n) worst case (α = load factor)")
    print("- Delete: O(1 + α) average, O(n) worst case")
    print("- Space: O(n)")
    print("- Load factor should be kept low (< 0.75) for good performance")


def main():
    """Run complete analysis."""
    print("ALGORITHM EFFICIENCY AND SCALABILITY ANALYSIS")
    print("MSCS532 Assignment 3 - Dheeraj Kumar")
    print("=" * 60)
    
    # Set recursion limit higher for larger arrays
    import sys
    sys.setrecursionlimit(2000)
    
    compare_quicksort_algorithms()
    analyze_hash_table()
    theoretical_analysis()
    
    print("\n" + "=" * 60)
    print("Analysis complete!")


if __name__ == "__main__":
    main()
