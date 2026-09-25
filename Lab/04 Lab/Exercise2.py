box = ["book", ["pen", "pencil"], [["toy"], "watch"]]

def contains_gift(box, target): 

    # loop through each item in the current box
    for item in box: 
        # If the item is a list, it's an inner box: search it recursively 
        if isinstance(item, list):
            if contains_gift(item, target): 
                return True # Stop immediately if foubnd inside this inner box

            # otherwise, its a gift item: check for a exact match 
        elif target == item: 
            return True
      # return false after the loop has checked every single item in the box  
    return False

print("Test cases result: ")
print( contains_gift(box, "toy") ) # True
print(contains_gift(box, "watch")) # True
print(contains_gift(box, "phone")) # False
print(contains_gift(box, "Toy")) # False
print(contains_gift([], "book")) # False
print(contains_gift([[], ["pen"]], "pen")) # True
    