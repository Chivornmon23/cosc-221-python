# Task 1: Implementing BST for Contact Storage
class Node:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.right = None
        self.left = None

class PhoneBookBST:
    def __init__(self):
        self.root = None

    def insert(self, name, phone):
        self.root = self._insert(self.root, name, phone)
    def _insert(self, node, name, phone):
            if not node:
                return Node(name, phone)
            if name < node.name:
                node.left = self._insert(node.left, name, phone)
            elif name > node.name:
                node.right = self._insert(node.right, name, phone)
            else:
                node.phone = phone
            return node
    def search(self, name):
        return self._search(self.root, name)
    def _search(self, node, name):
        if node is None:    # Contact was found
            return None     # return None
        if node.name == name: # We found the contact
            return node.phone   # return its phone number
        if name < node.name:    # If the requested name is alphabetically smaller,
            return self._search(node.left, name)    # search left.
        return self._search(node.right, name) # Otherwise, search right.

    def delete(self, name):
        self.root = self._delete(self.root, name)

    def _delete(self, node, name):
        if node is None:
            return None
        if name < node.name:
            node.left = self._delete(node.left, name)
        elif name > node.name:
            node.right = self._delete(node.right, name)
        else:
            # Case 1 & 2: 0 or 1 child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Case 3: 2 Children
            successor = self._min_value_node(node.right)
            node.name = successor.name
            node.phone = successor.phone
            node.right = self._delete(node.right, successor.name)

        return node
    def _min_value_node(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current
    def autocomplete(self, prefix):
        results = []
        self._autocomplete(self.root, prefix, results)
        return results

    def _autocomplete(self, node, prefix, results):
        if node is None:
            return
        self._autocomplete(node.left, prefix, results)
        if node.name.startswith(prefix):
            results.append((node.name, node.phone))
        self._autocomplete(node.right, prefix, results)

phonebook = PhoneBookBST()

contacts = {("Alice", "123-456-7890"),
            ("Bob", "234-567-8901"),
            ("Charlie", "345-678-9012"),
            ("David", "456-789-0123"),
            ("John", "567-890-1234"),
            ("Joanne", "678-901-2345"),
            ("Joy", "789-012-3456")}

for contact in contacts:
    phonebook.insert(*contact)
print("1. Search")
print("Search for Bob: ", phonebook.search("Bob"))
print("Search for Alice: ", phonebook.search("Alice"))
print("Search for Unknown: ", phonebook.search("Unknown"))

print("")
print("2. After Deleted")
print("After deleting Charlie: ", phonebook.delete("Charlie"))

print("")
print("3. Autocomplete")
print("Autocomplete for 'Jo': ", phonebook.autocomplete("Jo"))

