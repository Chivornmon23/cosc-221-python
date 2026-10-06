# I traced the code manually for code comprehension and study.

class Node:
    def __init__(self, name: str, is_file: bool = False):
        self.name = name
        self.is_file = is_file
        self.left = None
        self.right = None

    @staticmethod
    def add_node(parent: 'Node', name: str, is_file: bool = False) -> bool:
        """Adds a new file or directory under parent. Returns False if name exists."""
        if parent is None or parent.is_file:
            # if a parent doesn't exist or the parent is a file, don't add anything
            return False
        # left = first child
        curr = parent.left # start with the parent's first child
        if curr is not None: # Does the parent alr have at least one child
            if curr.name == name: # if the name alr exists
                # Root
                # ├── Documents
                # └── Documents
                return False # return False
            while curr.right is not None: # Keep moving thru the siblings until reach the last one
                curr = curr.right # move to the next sibling
                if curr.name == name: # if the sibling name alr exists
                    return False
                #Root
                # ├── Documents
                # ├── Pictures
                # └── Music
                # Internally: Documents → Pictures → Music → None

                # Now -> Documents → Pictures → Music → Videos → None
            curr.right = Node(name, is_file) # we need "Videos"
        # if the parent has no children
        else:
            parent.left = Node(name, is_file) # make a new one
        return True

    @staticmethod
    def search(node: 'Node', name: str) -> 'Node | None':
        """Recursively searches for a node by name in the tree."""
        if node is None:
            return None
        if node.name == name:
            return node
        found = Node.search(node.left, name)
        if found:
            return found
        return Node.search(node.right, name)
    # search current node
    #        ↓
    # search child
    #        ↓
    # if not found
    #        ↓
    # search sibling
    # This is Depth-First Search

    @staticmethod
    def print_tree(node: 'Node', level: int = 0) -> None:
        """Prints the hierarchical structure with indentation."""
        if node is None:
            return

        if level == 0:
            print("📁 " + node.name)
        else:
            indent = "    " * level
            icon = "📄 " if node.is_file else "📁 "
            print(f"{indent}{icon}{node.name}")

        if node.left is not None:
            Node.print_tree(node.left, level + 1)

        if level > 0 and node.right is not None:
            Node.print_tree(node.right, level)
            # LEFT  → child   → level + 1
            # RIGHT → sibling → same level

# root = Node("Root") # create root
# Node.add_node(root, "Document") # add "Document"
# Root
# └── Document
# Node.add_node(root, "Pictures") # add "Pictures" but root alr has "Document" -> curr = root.left = Document
# Root
# └── Document
# └── Pictures

# Node.add_node(root, "Music")
# It walks through:
#       Documents
#           ↓
#       Pictures
#           ↓
#          None
# then add " Music"
# Root
# └── Document
# └── Pictures
# └── Musics

# Now add something inside "Document"
# Node.add_node(root, "Homework.txt", True)

def main():
    root = Node("Root", is_file=False)

    while True:
        print("\nChoose an action:")
        print("1. Add Directory or File")
        print("2. Print File System Structure")
        print("3. Search for a File/Directory")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            parent_name = input("Enter the parent directory name: ").strip()
            name = input("Enter the name of the file or directory: ").strip()
            type_input = input("Is it a file or directory? (f/d): ").strip().lower()

            is_file = True if type_input == 'f' else False

            parent_node = Node.search(root, parent_name)
            success = Node.add_node(parent_node, name, is_file)

            if success:
                item_type = "file" if is_file else "directory"
                print(f"Added {item_type} '{name}' under '{parent_name}'.")
            else:
                print(f"Failed to add '{name}'. Parent not found, is a file, or name already exists.")

        elif choice == "2":
            print("\nFile System Structure:")
            Node.print_tree(root)

        elif choice == "3":
            name = input("Enter the name of the file or directory to search: ").strip()
            result = Node.search(root, name)
            if result:
                item_type = "File" if result.is_file else "Directory"
                print(f"Found: {result.name} ({item_type})")
            else:
                print(f"'{name}' not found.")

        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()