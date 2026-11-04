import random

def generate_products(n= 10):
    products = []
    for i in range (1, n+1):
        product = {
            "ProductID": i,
            "Name": f"Product-{i}",
            "Price": round(random.uniform(1, 50), 2)
        }
        products.append(product)
    return products

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["Price"] <= right [j]["Price"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(products):
    # Base case: if a list containing 0 or 1 item
    if len(products) <= 1:
        return products

    mid = len(products)//2
    left = merge_sort(products[:mid])
    right = merge_sort(products[mid:])
    return merge(left, right)
