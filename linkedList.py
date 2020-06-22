class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def empty(self):
        return self.head == None

    def print_nodes(self):
        if not self.head:
            print(self.head)
        node = self.head
        while node:
            end = " -> " if node.next else "\n"
            print(node.val, end=end)
            node = node.next

    def at(self, index):
        count = 0
        node = self.head
        while node:
            if count == index:
                return node.val
            count += 1
            node = node.next
        return ("Error: index > length ")

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(value)

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def push_front(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop_front(self):
        if self.head:
            first = self.head
            self.head = first.next
            return first.val

    def push_back(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node

    def pop_back(self):
        if not self.head:
            return
        node = self.head
        while node.next.next:
            node = node.next
        last = node.next.val
        node.next = None
        return last

    def front(self):
        if self.head:
            return self.head.val

    def back(self):
        if not self.head:
            return
        node = self.head
        while node.next:
            node = node.next
        return node.val
    
    def insert(self, index, value):
        new_node = ListNode(value)
        count = 0
        if not self.head:
            if index == 0:
                self.head = new_node
                return
            else:
                return "Error: insert error"
        node = self.head
        if index == 0:
            new_node.next = node
            self.head = new_node
            return
        while node:
            if index == count + 1:
                tmp = node.next
                new_node.next = tmp
                node.next = new_node
                return
            else:
                node = node.next
                count += 1

    def erase(self, index):
        count = 0
        if not self.head:
            return "Error: erase error"
        node = self.head
        if index == 0:
            node = node.next
            self.head = node
            return
        while node.next:
            if index == count + 1:             
                node.next = node.next.next
                return
            elif count + 1 > index:
                return "Error: erase index > length"
            else:
                node = node.next
                count += 1

    def value_n_from_end(self, n):
        if not self.head:
            return
        slow = self.head
        fast = self.head
        count = 1
        while n > count:
            fast = fast.next
            count += 1
        while fast.next:
            fast = fast.next 
            slow = slow.next
        return slow.val

    def reverse(self):
        if not self.head:
            return
        node = self.head
        prev = None
        while node:
            cur = node
            node = node.next
            cur.next = prev
            prev = cur
        self.head = prev

    def remove_value(self, value):
        if not self.head:
            return
        if self.head.val == value:
            self.head = self.head.next
            return
        node = self.head
        tmp = self.head
        while node.next:
            if node.next.val == value:
                node.next = node.next.next
                return
            node = node.next
        return "Error: value does not exist"




def main():
    list = LinkedList()
    # print(list.empty())
    list.append(1)
    # print(list.empty())
    list.append(2)
    list.append(3)
    list.append(2)
    # list.print_nodes()
    # print(list.at(0))
    # print(list.at(1))
    # print(list.at(2))
    # print(list.at(3))
    # print(list.size())
    list.push_front(5)
    # list.print_nodes()
    # print(list.pop_front())
    list.push_back(6)
    # list.pop_back()
    list.insert(3, 6)
    # list.erase(2)
    # list.print_nodes()
    list.reverse()
    list.remove_value(7)
    list.print_nodes()
    # print(list.value_n_from_end(5))
    # print(list.front())
    # print(list.back())


if __name__ == "__main__":
    main()