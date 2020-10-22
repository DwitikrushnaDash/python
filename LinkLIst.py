class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = node

    def print_list(self, head=None):
        if head is None:
            tmp = self.head
        else:
            tmp = head
        while tmp:
            print(tmp.data)
            tmp = tmp.next

    def print_rev(self, head):
        # if head:
        #     self.print_rev(head.next)
        #     print(head.data)
        # else:
        #     return
        if head is None:
            return
        self.print_rev(head.next)
        print(head.data)

    def reverse_list(self, head):
        if head is None or head.next is None:
            return head
        tmp = self.reverse_list(head.next)
        head.next.next = head
        head.next = None
        return tmp

    def rev_list(self):
        if self.head is None or self.head.next is None:
            return self.head
        prv = None
        cur = self.head
        while(cur is not None):
            next_node = cur.next
            cur.next = prv
            prv = cur
            cur = next_node
        return prv

    def rev_group(self, head, k):
        cur = head
        prv = None
        cnt = 1

        while cur is not None and cnt <= k:
            next_node = cur.next
            cur.next = prv
            prv = cur
            cur = next_node
            cnt += 1

        # next is now a pointer to (k+1)th node
        # recursively call for the list starting
        # from current. And make rest of the list as
        # next of first node
        if next_node is not None:
            head.next = self.rev_group(next_node, k)
        return prv

    def print_last_n_nodes(self, head, k):
        cur = head
        prv = head
        cnt = 0
        while cur and cnt < k:
            cur = cur.next
            cnt += 1

        if cnt >= k:
            while cur:
                prv = prv.next
                cur = cur.next
            while prv:
                print(prv.data)
                prv = prv.next

    def find_cycle(self, head):
        slow = head
        fast = head

        if not head or not head.next:
            return False

        cycle_exist = False
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle_exist = True
        #         return True
        # return False
        if cycle_exist:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    def delete_middle(self, head):
        prv = None
        slow = head
        fast = head

        if slow is None or slow.next is None:
            return head
        while fast and fast.next:
            prv = slow
            slow = slow.next
            fast = fast.next.next

        prv.next = slow.next
        return head

    def remove_duplicate(self, head):
        if head is None or head.next is None:
            return head
        cur = head
        while cur.next:
            if cur.data == cur.next.data:
                cur.next = cur.next.next
                # cur.next = next_node
            else:
                cur = cur.next
        return head

    def check_palindrome(self, head):
        if head is None or head.next is None:
            return False
        stack = []
        cur = head
        #Travese First time
        while cur:
            stack.append(cur.data)
            cur = cur.next
        print(stack)
        cur = head
        cnt = len(stack) - 1
        while cur:
            if cur.data != stack[cnt]:
                return False
            cur = cur.next
            cnt = cnt - 1
        return True

    def rotate(self, k):
        cnt = 1
        cur = self.head
        while cnt < k and cur is not None:
            cur = cur.next
            cnt += 1
        kthNode = cur

        if cur is None:
            return

        while cur.next is not None:
            cur = cur.next
        # Change next of last node to previous head
        # Next of 60 is now changed to node 10
        cur.next = self.head
        # Change head to (k + 1)th node
        # head is not changed to node 50
        self.head = kthNode.next
        # change next of kth node to NULL
        # next of 40 is not NULL
        kthNode.next = None

    def delete_last_occurance(self, data):
        tmp = self.head
        while tmp:
            if tmp.data == data:
                last = tmp
            tmp = tmp.next
        #Not last Node
        if last and last.next is not None:
            last.data = last.next.data
            last.next = last.next.next
        # If last Node
        if last and last.next is None:
            cur = self.head
            while cur.next != last:
                cur = cur.next
            cur.next = None

    def skip_and_delete(self, m, n):
        cur = self.head
        while cur:
            for i in range(1, m):
                if cur is None:
                    return
                cur = cur.next
            #If linklist has m elements only
            if cur is None:
                return
            tmp = cur.next
            for j in range(1, n+1):
                if tmp is None:
                    return
                tmp = tmp.next
            cur.next = tmp
            cur = tmp






dup_list = LinkList()
dup_list.add_node(1)
dup_list.add_node(2)
dup_list.add_node(3)
dup_list.add_node(1)
dup_list.add_node(1)
dup_list.add_node(6)
dup_list.add_node(7)

dup_list.print_list()
print("===============================")
dup_list.delete_last_occurance(1)
dup_list.print_list()
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

dup_list.skip_and_delete(3, 2)
dup_list.print_list()
# if dup_list.check_palindrome(dup_list.head):
#     print("Palindrome")
# else:
#     print("Not palindrome")
#
# dup_list.rotate(4)
# dup_list.print_list()
# print("Remove duplicates")
# dup_head = dup_list.remove_duplicate(dup_list.head)
# dup_list.print_list(dup_head)


#
# l1 = LinkList()
# l1.add_node(50)
# l1.add_node(70)
# l1.add_node(100)
# l1.add_node(120)
# l1.add_node(51)
# l1.add_node(71)
# l1.add_node(101)
# # l1.add_node(60)
# # l1.add_node(80)
# # l1.add_node(110)
# print("Lnk list elements")
# print("======================")
# l1.print_list()
#
# l2 = l1.delete_middle(l1.head)
# print("Print After - Deleted Node ")
# l1.print_list(l2)
# # print(l2.data)
# print("Print reverse")
# print("======================")
# # l1.print_rev(l1.head)
# # nodeHead = l1.reverse_list(l1.head)
# # l1.print_list(nodeHead)
#
# # l1.head = l1.rev_list()
# # l1.print_list()
#
# # l1.head = l1.rev_group(l1.head, 3)
# # l1.print_list()
#
# # l1.print_last_n_nodes(l1.head, 3)