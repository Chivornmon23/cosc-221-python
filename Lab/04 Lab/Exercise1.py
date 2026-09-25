
box = ["book", ["pen", "pencil"], [["toy"], "watch"]]

def count_gifts(box):
    total = 0 
    # loop through everything in the box
    for item in box: 
        # If the item is a list, it's the inner box: call recursively 
        if isinstance(item, list):
            total += count_gifts(item)
        # otherwise it is a individual gift like a string
        else: 
            total += 1
    return total

print("Test cases result: ")
print(count_gifts([]))
print(count_gifts(["book"]))
print(count_gifts(box))
print(count_gifts([[], ["ball"], [["kite", "ball"]]]))
print(count_gifts([[["ring"]]]))
