class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#전위 순회
# A->B->D->E->C->F->G
def preorder_traverse(node):
    if node == None: return
    print(node.data, end = '->')
    # 재귀호출
    preorder_traverse(node.left)
    preorder_traverse(node.right)

#중위 순회
# D->B->E->A->F->C->G
def inorder_traverse(node):
    if node == None: return
    inorder_traverse(node.left)
    print(node.data, end = '->')
    inorder_traverse(node.right)

#후위 순위
# D->E->B->F->G->C->A
def postorder_traverse(node):
    if node == None: return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.data, end = '->')

root = None
def init_tree():
    global root

    new_node = Node("A")
    root = new_node
    new_node = Node("B")
    root.left = new_node
    new_node = Node("C")
    root.right = new_node

    new_node_1 = Node("D")
    new_node_2 = Node("E")

    node = root.left
    node.left = new_node_1
    node.right = new_node_2

    new_node_1 = Node("F")
    new_node_2 = Node("G")

    node = root.right
    node.left = new_node_1
    node.right = new_node_2

#단계 순회
# A->B->C->D->E->F->G
levelq = []
def levelorder_traverse(node):
    global levelq
    levelq.append(node)               # 매개변수로 받은 노드를 큐에 일단 저장
    while len(levelq) != 0:           # 큐의 길이가 0이 아닐때 출력처리
        visit_node = levelq.pop(0)    # 현재 가르키고 있는 노드
        print(visit_node.data, end = '->')
        if visit_node.left != None:   # 왼쪽 노드에 값이 있다면 출력
            levelq.append(visit_node.left)
        if visit_node.right != None:  # 오른쪽 노드에 값이 있다면 출력
            levelq.append(visit_node.right)


if __name__ == "__main__":
    init_tree()

    print("<Preorder Traverse>")
    preorder_traverse(root)
    print("\n")

    print("<Inorder Traverse>")
    inorder_traverse(root)
    print("\n")

    print("<Postorder Traverse>")
    postorder_traverse(root)
    print("\n")

    print("<Levelorder Traverse>")
    levelorder_traverse(root)