# Exercise 1
def count_gifts(box): 
    total = 0
    for item in box: 
        if isinstance(item, list): 
            total += count_gifts(item)
        else: 
            total += 1
    return total 

# Exercise 2
def contains_gift(box, target): 
    for item in box: 
        if isinstance(item, list):
            if contains_gift(item, target): 
                return True
        elif target == item: 
            return True
    return False

# Exercise 3
def isPalindromeNum(n): 
    digit = str(n)

    def check(left, right): 
        # Base case 1: If pointers cross or meet, all pairs matched! (checking indices)
        if left >= right: 
            return True
        
        # Base case 2: If characters at the pointers don't match
        if digit[left] != digit[right]: 
            return False
        
        # Recursive step: Move pointers inward
        return check(left + 1, right - 1)
    
    return check(0, len(digit) - 1) 

# Challenge 

print("--- Test: count_gifts ---")
print("Required: ([]) = ", count_gifts([]))
print("Required: ([\"book\"]) = ", count_gifts(["book"]))                          
print("Required: (box) = ", count_gifts([["book", ["pen"]], [["toy"], "watch"]])) 
print("New Extra: ([[\"phone\", [\"laptop\"]]]) = ", count_gifts([["phone", ["laptop"]]])) 

print("\n--- Test: contains_gift ---")
box_ex = [["book", ["pen", "pencil"]], [["toy"], "watch"]]
print("Required Test 1 (box, 'toy') = ", contains_gift(box_ex, "toy"))       
print("Required Test 2 (box, 'phone') = ", contains_gift(box_ex, "phone"))   
print("Required Test 3 ([], 'book') = ", contains_gift([], "book"))          
print("New Extra Test (box, 'book') = ", contains_gift(box_ex, "book"))      

print("\n--- Test: isPalindromeNum ---")
print("Required: (121) = ", isPalindromeNum(121))      
print("Required:  (12321) = ", isPalindromeNum(12321))  
print("Required: (1234) = ", isPalindromeNum(1234))    
print("New Extra: (7) = ", isPalindromeNum(7))            

# Challenge 1: Unpack all gifts
def unpack(box):
    flat_list = []
    for item in box:
        if isinstance(item, list):
            # Recursively unpack inner boxes and add their items
            flat_list.extend(unpack(item))
        else:
            # It's a gift name, so add it directly
            flat_list.append(item)
    return flat_list
# Challenge 2: Find the deepest box
def box_depth(box):
    if not box:
        return 1[cite: 2]
    max_sub_depth = 0
    for item in box:
        if isinstance(item, list):
            sub_depth = box_depth(item)[cite: 2]
            if sub_depth > max_sub_depth:
                max_sub_depth = sub_depth
    return 1 + max_sub_depth[cite: 2]

box = ["book", ["pen"]], [["toy"], "watch"]
unpack(box) 
unpack([["ball", "ball"]]) 
unpack([])  
# Answer

# What stops each function?
# - count_gifts: Stops when the loop finishes iterating through all items in the current box level.
# - contains_gift: Stops immediately when finding a match
# - sortHelper: Stops when low is no longer less than high 

# What becomes smaller?
# - count_gifts: The nested list (sub-boxes) being unpacked during recursive calls.
# - contains_gift: The remaining items in the loop being searched.
# - isPalindromeNum: The `left` increases and `right` decreases.
# - sortHelper: The unsorted range of the list

# Why can returning False too early fail?
# - In recursive search functions like contains_gift, 
# if an inner sub-box does not contain the target and you return False immediately, this 
# causes the function to miss items that exist elsewhere in the structure.

# Explain one extra test and the mistake it could detect.
# - Extra Test: contains_gift([["book", "pen"], ["pencil"]], "pencil") 