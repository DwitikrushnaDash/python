import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def create_tree(self, root, data):
        tmp = root
        if tmp is None:
            tmp = Node(data)
            self.root = tmp
        else:
            while tmp:
                if data <= tmp.data:
                    if tmp.left is None:
                        tmp.left = Node(data)
                        break
                    else:
                        tmp = tmp.left
                else:
                    if tmp.right is None:
                        tmp.right = Node(data)
                        break
                    else:
                        tmp = tmp.right

    # Inorder search
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    # Breadth wise search
    def breadth_traverse(self, root):

        list_tmp = []
        if root is None:
            return
        list_tmp.append(root)

        # While list is not empty
        while len(list_tmp) != 0:
            tmp_node = list_tmp.pop(0)
            print(tmp_node.data)
            if tmp_node.left:
                list_tmp.append(tmp_node.left)
            if tmp_node.right:
                list_tmp.append(tmp_node.right)

    def get_height(self, root):
        if root is None:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def get_max(self, root):
        if root is None:
            return 0

        left_max = self.get_max(root.left)
        right_max = self.get_max(root.right)
        if left_max > right_max:
            max = left_max
        else:
            max = right_max
        if max < root.data:
            max = root.data
        return max

    def rotate(self, root):
        if not root:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.rotate(root.left)
        self.rotate(root.right)

    def count_breadth(self, root):
        ''''
            Level wise number of elements
        '''
        breadth_cnt = []
        if not root:
            breadth_cnt[0] = 0
            return breadth_cnt

        # Add first Node to list and also add None (will be used to track the level)
        level_node = []
        cnt = 0
        level_node.append(root)
        level_node.append(None)

        #Taverse till level_node list is empty
        level_number = 0
        while len(level_node) != 0:
            tmp = level_node.pop(0)
            if tmp is None:
                if len(level_node) != 0:
                    level_node.append(None)
                    breadth_cnt.append(cnt)
                    cnt = 0
            else:
                cnt += 1
                if tmp.left:
                    level_node.append(tmp.left)
                if tmp.right:
                    level_node.append(tmp.right)

        return breadth_cnt

    def size(self, root):
        if root is None:
            return 0
        return(self.size(root.left) + 1 + self.size(root.right))

    def print_level_reverse(self, root):
        level_list = []
        level_final = []
        if root:
            level_list.append(root)
        while len(level_list) != 0:
            tmp = level_list.pop(0)
            if tmp.left:
                level_list.append(tmp.left)
            if tmp.right:
                level_list.append(tmp.right)
            # Add elements
            level_final.append(tmp)

        #Print list in reverse order
        for i in reversed(level_final):
            print(i.data)

    def deepest_node(self, root):
        if root is None:
            return None

        level_list = []
        level_list.append(root)

        while len(level_list) != 0:
            tmp = level_list.pop(0)
            if tmp.left:
                level_list.append(tmp.left)
            if tmp.right:
                level_list.append(tmp.right)

        return tmp


    def number_leaves(self, root):
        if root is None:
            return 0

        level_list = []
        level_list.append(root)
        cnt = 0

        while len(level_list) != 0:
            tmp = level_list.pop(0)
            #For leaves
            if tmp.left is None and tmp.right is None:
            #For full node
            # if tmp.left and tmp.right:
                cnt += 1

            if tmp.left:
                level_list.append(tmp.left)
            if tmp.right:
                level_list.append(tmp.right)

        return cnt

    def number_leaves_rec(self, root):
        if root is None:
            return 0
        cnt = 0
        #For leaves
        if root.left is None and root.right is None:
        # For full Node
        # if root.left and root.right:
            cnt += 1
            return cnt

        return self.number_leaves_rec(root.left) + self.number_leaves_rec(root.right)

    # Check structurally Identical (2 binary trees)
    def check_symmetry(self, root1, root2):
        if root1 is None and root2 is None:
            return 1
        if root1 is None or root2 is None:
            return 0
        return (root1.data == root2.data and self.check_symmetry(root1.left, root2.left) and
                self.check_symmetry(root1.right, root2.right))

    # Max element in level
    def max_val_level(self, root):
        if root is None:
            return 0
        level_list = []
        level_list.append(root)
        level_list.append(None)

        max_val = 0
        while len(level_list) != 0:
            tmp = level_list.pop(0)

            if tmp is None:
                if len(level_list) != 0:
                    level_list.append(None)
                    print(max_val)
                    max_val = 0
            else:
                if tmp.data > max_val:
                    max_val = tmp.data
                if tmp.left:
                    level_list.append(tmp.left)
                if tmp.right:
                    level_list.append(tmp.right)

    def get_level_max_sum(self, root):
        if root is None:
            return 0

        max_sum = 0
        level = 0
        max_level = 0
        level_total = 0

        level_list = []
        level_list.append(root)
        level_list.append(None)

        while len(level_list) != 0:
            tmp = level_list.pop(0)
            if tmp is None:

                if level_total > max_sum:
                    max_sum = level_total
                    max_level = level
                if len(level_list) != 0:
                    level_list.append(None)
                    level_total = 0
                level += 1

            else:
                level_total += tmp.data
                if tmp.right:
                    level_list.append(tmp.right)
                if tmp.left:
                    level_list.append(tmp.left)

        return max_level, max_sum

    def sum_all_elements(self, root):
        if root is None:
            return 0
        return root.data + self.sum_all_elements(root.left) + self.sum_all_elements(root.right)

    def print_all_path_to_leaves(self, root, path):
        if root is None:
            return None

        path.append(root.data)
        if root.left is None and root.right is None:
            print(path)
            # path = []
        else:
            self.print_all_path_to_leaves(root.left, path)
            self.print_all_path_to_leaves(root.right, path)



################################################################################
data_list = [31,45,67,29,100,79,65,88,2]
new_tree = Tree()
for data in data_list:
    new_tree.create_tree(new_tree.root, data)

# new_tree.inorder(new_tree.root)
# new_tree.breadth_traverse(new_tree.root)
# height = new_tree.get_height(new_tree.root)
# print(height)
# max = new_tree.get_max(new_tree.root)
# print(max)
# print("=================================")
# new_tree.rotate(new_tree.root)
# new_tree.inorder(new_tree.root)
# lvl_tree = new_tree.count_breadth(new_tree.root)
# count = new_tree.size(new_tree.root)
# print("=================================")
# print(count)
# # new_tree.print_level_reverse(new_tree.root)
# tmp_node = new_tree.deepest_node(new_tree.root)
# print("Deepest Node: {}".format(tmp_node.data))
# cnt = new_tree.number_leaves(new_tree.root)
# print("Number of leaves: {}".format(cnt))
# cnt_rec = new_tree.number_leaves_rec(new_tree.root)
# print("Number of leaves Rec: {}".format(cnt_rec))
#
# print("Check symmetry: {}".format(str(new_tree.check_symmetry(new_tree.root, new_tree.root))))
# print("==================================")
# print("Max value in each level:")
# new_tree.max_val_level(new_tree.root)
# print("=================================")
# (max_level, max_sum) = new_tree.get_level_max_sum(new_tree.root)
# print("Max level: {}, Max sum:{}".format(max_level, max_sum))
# print("=================================")
#
print("Total: {}".format(new_tree.sum_all_elements(new_tree.root)))
print("=================================")
new_tree.print_all_path_to_leaves(new_tree.root, path=[])
print("=================================")