class BinarySearchTree:
    class _Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # 재귀 이용
    def recursive_search(self, data):
        return self._recursive_search_value(data, self.root)

    def _recursive_search_value(self, data, node):
        if not node:
            return None
        if node.data == node:
            return node

        if data < node.data:
            self._recursive_search_value(data, node.left)
        else:
            self._recursive_search_value(data, node.right)

    def search(self, data):
        node = self.root
        while node:
            if data == node.data:
                return node
            elif data < node.data:
                node = node.left
            else:
                node = node.right
        return None

    def insert(self, data):
        node = self.root
        if not node:
            self.root = self._Node(data)
            return

        while node:
            if data == node.data:
                raise Exception(f"이미 존재하는 값입니다 => {data}")
            elif data < node.data:
                nxt = node.left
                if not nxt:
                    node.left = self._Node(data)
                    return
            else:
                nxt = node.right
                if not nxt:
                    node.right = self._Node(data)
                    return
            node = nxt

    def recursive_insert(self, data):
        if not self.root:
            self.root = self._Node(data)
        else:
            self._recursive_insert_value(data, self.root)

    def _recursive_insert_value(self, data, node):
        if not node:
            return self._Node(data)

        if data == node.data:
            raise Exception(f"이미 존재하는 값입니다 => {data}")

        if data < node.data:
            node.left = self._recursive_insert_value(data, node.left)
        else:
            node.right = self._recursive_insert_value(data, node.right)

        return node

    def recursive_delete(self, data):
        return self._recursive_delete_value(data, self.root)

    def _recursive_delete_value(self, data, node):
        if not node:
            return None, False

        deleted = False
        if data == node.data:
            deleted = True
            # 왼쪽 오른쪽 둘 다 있는 경우, 오른쪽의 가장 작은 원소로 대체
            if node.left and node.right:
                parent, child = node, node.right
                while child.left:
                    parent, child = child, child.left

                # parent == node => 오른쪽의 가장 작은 원소가 node.right인 경우
                if parent != node:
                    parent.left = child.right
                    child.right = node.right

                child.left = node.left
                node = child

            # 한 쪽만 있는 경우, 한 쪽 서브트리의 루트로 대체
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None

        elif data < node.data:
            node.left, deleted = self._recursive_delete_value(data, node.left)
        else:
            node.right, deleted = self._recursive_delete_value(data, node.right)

        # 대체된 노드와 삭제 여부 반환
        return node, deleted


bst = BinarySearchTree()

numbers = [4, 1, 3, 5, 2, 10, 7]

for num in numbers:
    bst.recursive_insert(num)

# bst.inorder(bst.root)

print(bst.recursive_delete(1))
bst.inorder(bst.root)
print(bst.recursive_delete(6))
bst.inorder(bst.root)
print(bst.recursive_delete(2))
bst.inorder(bst.root)
