class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None   
        self.right = None 
        
def invert_binary_tree(tree) -> BinaryTree: 
    if tree is None :
        return None
        
    tree.left , tree.right = tree.right , tree.left
        
    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)
        
    return tree
    
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

def print_tree(tree):
    if tree is None:
        return
    print(tree.value)
    print_tree(tree.left)
    print_tree(tree.right)

print("До інвертування:")
print_tree(root)

invert_binary_tree(root)

print("Після інвертування:")
print_tree(root)
        
