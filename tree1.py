class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Membuat tree sesuai gambar
#         A
#        / \
#       B   C
#      / \    \
#     D   E    F

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

# Fungsi traversal
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')

# Menampilkan hasil traversal
print("Tampilan Inorder")
print("================")
inorder(root)
print("\n")

print("Tampilan Preorder")
print("=================")
preorder(root)
print("\n")

print("Tampilan Postorder")
print("==================")
postorder(root)
print()
