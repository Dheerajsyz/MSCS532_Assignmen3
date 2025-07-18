# Algorithm Efficiency and Scalability

## Overview

This repository contains my implementation and analysis of two fundamental algorithms:

1. **Randomized Quicksort** - Quicksort with random pivot selection
2. **Hash Table with Chaining** - Hash table using linked lists for collision resolution

## Files

- `src/randomized_quicksort.py` - Randomized and deterministic quicksort implementations
- `src/hash_table_chaining.py` - Hash table with chaining implementation  
- `analysis.py` - Performance comparison and analysis
- `docs/analysis_report.md` - Detailed theoretical and empirical analysis
- `README.md` - This file

## How to Run

### Running Individual Algorithms

```bash
# Test randomized quicksort
python src/randomized_quicksort.py

# Test hash table
python src/hash_table_chaining.py
```

### Running Complete Analysis

```bash
# Run performance comparison
python analysis.py
```

## Key Findings

### Randomized Quicksort vs Deterministic Quicksort

- **Random arrays**: Both perform similarly
- **Sorted arrays**: Randomized quicksort is much faster (avoids O(n²) worst case)
- **Reverse sorted arrays**: Randomized quicksort significantly outperforms deterministic

### Hash Table Performance

- **Load factor** greatly affects performance
- **Chaining** effectively handles collisions
- **Search time** increases with load factor as expected

## Theoretical Analysis

### Randomized Quicksort
- **Average case**: O(n log n) - proven using indicator random variables
- **Worst case**: O(n²) but very unlikely due to random pivot selection
- **Key advantage**: Eliminates worst-case behavior on sorted inputs

### Hash Table with Chaining
- **Average case operations**: O(1) for insert/search/delete
- **Load factor α**: Affects performance as O(1 + α)
- **Collision resolution**: Chaining with linked lists

## Implementation Details

### Randomized Quicksort Features
- Random pivot selection using `random.randint()`
- Performance metrics tracking (comparisons, swaps, time)
- Comparison with deterministic version

### Hash Table Features
- Simple hash function for strings and integers
- Chaining with linked list nodes
- Load factor calculation and monitoring
- Insert, search, and delete operations

## Results Summary

The empirical testing confirms theoretical predictions:

1. Randomized quicksort eliminates worst-case O(n²) behavior on sorted inputs
2. Hash table performance degrades gracefully as load factor increases
3. Both algorithms demonstrate their expected complexity characteristics
