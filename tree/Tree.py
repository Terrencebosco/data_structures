# trees are recursive

# this is an individual node in the over arching tree.
class TreeNode:
    def __init__(self, data):
        self.data = data

        # each element in this list is an instance of treenode class.
        self.children = []
        self.parent = None

    def add_child(self, child):

        # this means that child is an instance of tree node class this will have
        # a parant property and we want to set that to self.
        child.parent = self
        self.children.append(child)

    # recursive print function
   def print_tree(self):
       print(self.data)
       if self.children:
           for child in self.children:
               child.print_tree()

def build_products_tree():
    root = TreeNode("electronics")

    laptop = TreeNode("laptop")

    root.add_child(laptop)

    return root

if __name__ == "__main__":
    root = build_products_tree()
    pass