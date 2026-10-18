# A student attempts to insert new_node right after current_node
# in a singly list:
# head -> 10 -> 20 -> 30
#Student code:
# current_node.next = new_node # current_node.next (10.next) = 40 (new_node)
# new_node.next = current_node.next # new_node.next (40.next) = 40

# new_node.next points to new_node itself instead of the original
# current_node.next, causing a self-loop and disconnecting the rest
#   of the linked list.

# new_node.next = current_node.next # new_node.next (40.next) = 10.next
# current_node.next = new_node + 