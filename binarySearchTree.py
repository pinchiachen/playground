class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def insert(self, value):
        if not self.val:
            self.val = value
        else:
            if value > self.val:
                if self.right == None:
                    self.right = TreeNode(value)
                else:
                    self.right.insert(value)
            elif value < self.val:
                if self.left == None:
                    self.left = TreeNode(value)
                else:
                    self.left.insert(value)
            else:
                print("Err: value exist!")

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()

    def get_node_count(self, root):
        if not root:
            return 0
        return (1 + self.get_node_count(root.left) + self.get_node_count(root.right))

    def delete_tree(self):
        self.val = None
        if self.left:
            self.left.delete_tree()
        if self.right:
            self.right.delete_tree()

    def find(self, value):
        if value == self.val:
            return True
        elif value > self.val and self.right:
            return self.right.find(value)
        elif value < self.val and self.left:
            return self.left.find(value)
        return False

    def get_height(self, value):
        if value == self.val:
            return 1
        elif value > self.val and self.right:
            return 1 + self.right.get_height(value)
        elif value < self.val and self.left:
            return 1 + self.left.get_height(value)
        return -1

    def get_min_node(self, root):
        if root.left:
            return self.get_min(root.left)
        return root

    def get_min(self, root):
        if root.left:
            return self.get_min(root.left)
        return root.val

    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.val

    def delete_value(self, root, value):
        if not root:
            print("value does not exist")
        elif value > root.val:
            root.right = self.delete_value(root.right, value)
        elif value < root.val:
            root.left = self.delete_value(root.left, value)
        elif root.right and root.left:
            tmp_min = self.get_min_node(root.right)
            root.val = tmp_min.val
            root.right = self.delete_tree(root.right, tmp_min.val)
        elif root.right:
            root = root.right
        elif root.left:
            root = root.left
        else:
            root = None
        return root


    def max_height(self):
        if self.right and self.left:
            return 1 + max(self.left.max_height(), self.right.max_height())
        elif self.right:
            return 1 + self.right.max_height()
        elif self.left:
            return 1 + self.left.max_height()
        else:
            return 1

def main():
    root = TreeNode(8)
    root.insert(9)        
    root.insert(7)
    root.insert(1)
    root.insert(4)
    root.insert(5)
    root.insert(3)
    root.insert(2)
    root.insert(6)
    root.insert(12)
    root.insert(10)
    root.insert(11)
    root.insert(13)
    # root.delete_tree()
    # root.print_tree()
    # print(root.get_node_count(root))
    # print(root.find(2))
    # print(root.find(11))
    # print(root.get_height(11))
    # print(root.get_min(root))
    # print(root.get_max())
    # print(root.delete_value(3))
    # root.print_tree()
    # print(root.max_height())
    # root.delete_value(root, 20)
    root.print_tree()

if __name__ == "__main__":
    main()