N= int(input())
adj = {}
for _ in range(N):
    node, l, r = list(input().split())
    adj[node] =[l,r]
result = ''


def preorder(node):
    global result
    left = adj.get(node)[0]
    right = adj.get(node)[1]
    result += node
    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)


def inorder(node):
    global result
    left = adj.get(node)[0]
    right = adj.get(node)[1]
    if left != '.':
        inorder(left)
    result += node
    if right != '.':
        inorder(right)

def postorder(node):
    global result
    left = adj.get(node)[0]
    right = adj.get(node)[1]
    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)
    result += node

result = ''
preorder('A')
print(result)

result = ''
inorder('A')
print(result)

result = ''
postorder('A')
print(result)