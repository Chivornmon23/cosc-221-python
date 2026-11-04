# Task 2: Sorting Algorithms in E-commerce

import time
import random

def generate_products(n=10000):
    products = []
    for i in range (1, n+1):
        product = {
            "ProductID": i,
            "Name": f"Product-{i}",
            "Price": round(random.uniform(10, 500), 2)
        }
        products.append(product)
    return products
# 1. MERGE SORT (Divide & Conquer)
def merge(left, right):
    result = [] # create an empty list to hold the merged, sorted products
    i = j = 0
    # i tracks the current position in left
    # j tracks the current position in right
    while i < len(left) and j < len(right):
    # this loops continues as long as both lists still have an unprocessed item
        if left[i]["Price"] <= right [j]["Price"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j +=1
    result.extend(left[i:]) # add each element from index i to the end of the left to the result
    result.extend(right[j:]) # add each element from index j to the end of the right to the result
    return result
def merge_sort(products):
    #Base case if a list containing 0 or 1 item
    if len(products) <= 1:
        return products
    # Find the middle and split the list
    mid = len(products)//2
    # takes elements from the beginning up to, but not including, index mid
    left = merge_sort(products[:mid])
    # takes elements from index mid to the end
    right = merge_sort(products[mid:])
    return merge(left, right)

# 2. Quick Sort (Pivot Partitioning)
def quick_sort(products):
    if len(products) <= 1:
        return products
    pivot = products[len(products)//2]["Price"]
    left = [p for p in products if p["Price"] < pivot]
    middle = [p for p in products if p["Price"] == pivot]
    right = [p for p in products if p["Price"] > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 3. Measure execution time
def measure_time(sort_function, products):
    start = time.time()
    sorted_products = sort_function(products.copy())
    end = time.time()
    return end - start

if __name__ == "__main__":
    products = generate_products(10000)

    print("Running Single Benchmark...")
    merge_time = measure_time(merge_sort, products)
    quick_time = measure_time(quick_sort, products)

    if merge_time is not None and quick_time is not None:
        print(f"Merge Sort Time: {merge_time:.5f} seconds")
        print(f"Quick Sort Time: {quick_time:.5f} seconds")

        print("\n=== Multi-Run Benchmark (3 Iterations)===")
        for run in range(1, 4):
            test_data = generate_products(10000)
            m_time = measure_time(merge_sort, test_data)
            q_time = measure_time(quick_sort, test_data)
            faster = "Merge Sort" if m_time < q_time else "Quick Sort"

            print(f"Run {run}: Merge Sort = {m_time:.5f}s | Quick Sort = {q_time:.5f}s --> {faster} was faster")
    else:
        print("[!] Complete merge_sort() and quick_sort() above to see timing results.")
