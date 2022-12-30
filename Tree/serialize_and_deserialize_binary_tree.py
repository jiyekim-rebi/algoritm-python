# 이진 트리 직렬화, 역직렬화
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree
import collections
from idlelib.tree import TreeNode


# 이진트리 데이터 구조는 논리적인 구조를 가지고 있음.
# 파일 또는 디스크에 저장하려면 물리적인 형태로 변경해주는 과정 = 직렬화 = pickle
# 파일 또는 디스크에 저장된 물리적인 형태를 논리적인 데이터 구조로 변경해주는 작업 = 역직렬화
class Codec:
    # 직렬화
    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result = ['#']

        # 트리 bfs 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    # 역직렬화
    def deserialize(self, data: str) -> TreeNode:
        if data == '#':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2

        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
            
        return root