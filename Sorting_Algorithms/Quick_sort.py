def quick_sort(products):
    if len(products)<= 1:
        return products
    pivot = products[len(products)//2]["Price"]
    left = [p for p in products if p["Price"] < pivot]
    middle = [p for p in products if p["Price"] == pivot]
    right = [p for p in products if p["Price"] > pivot]

    return quick_sort(left) + middle + quick_sort(right)
