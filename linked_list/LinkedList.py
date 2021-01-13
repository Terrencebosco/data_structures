# linked list class

# class for "node" or in common terms "element"
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None # points to the head of the linked list

    def insert_at_begining(self, data):

        # node with value of "data" and next element will be the head
        # we add the element to the beginning and set the "Next" argument to the previous head
        # this puts the current data to the beginning of the list.
        node = Node(data, self.head)

        # we then set the current node as the head.
        self.head = node

    def insert_at_end(self, data):

        # if linked list is empty set the current data to the head.
        if self.head is None:
            self.head = Node(data, None)
            return

        # iterate through the entire linked list
            # once we hit an itr that is None we know we're at the end
            # we then set that node to the current data then set the next element to None
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    # insert a list of values as a linked list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        # if the index is less then 0 or greater than the count, its invalid
        if index < 0 or index >= self.get_length():
            raise Exception('not valid index')

        # if index is 0 then just point the head to the next element.
        # python handles garbage
        if index==0:
            self.head = self.head.next

        # keep count of where we are
        count = 0
        # start at the head
        itr = self.head
        # iter through linked list
        while itr:
            # if we reach the index BEFORE the index to drop move that index to the next.next
            # skipping the one we want to drop python garbage will clean.
            if count == index - 1:
                itr.next = itr.next.next
                break
            # if not n-1 count + 1 move to next.
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('invalid index')

        if index == 0:
            self.insert_at_begining(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
#         look for a value then insert after that value
#         use insert value?

        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data_to_remove):
        if self.head is None:
            return

        if self.head.data == data_to_remove:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data_to_remove:
                itr.next = itr.next.next
                break
            itr = itr.next

    # following links and print
    def print(self):

        # if the list is empty print nothing
        if self.head is None:
            print("list is empty")
            return

        # while itr is anything other than None, print it, else quit.
        itr = self.head
        linked_list = ''

        while itr:
            linked_list += str(itr.data) + ' --> '
            itr = itr.next

        print(linked_list)

if __name__ == '__main__':

    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
