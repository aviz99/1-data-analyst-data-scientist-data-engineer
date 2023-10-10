# 19 / 09 / 2023
# Day - 15
# Array & Linked List

# Array (list)
# ini_array = []

# ini_array.append("Brunch")
# print(f"Array: {ini_array}")
# ini_array.append("Bocce")
# print(f"Array: {ini_array}")
# ini_array.append("Tea")
# print(f"Array: {ini_array}")

# Linked List
# ini_array.insert(2, "Coffee")
# print(f"Array: {ini_array}")


# SIngly Linked List
class singlyLinkedList:
    class _Node:
        def __init__(self, element, nextNode=None):
            self.element = element
            self.nextNode = nextNode

    def __init__(self):
        self._head = None
        self._size = 0

    # View
    def __str__(self):
        result = ""
        pointer = self._head
        while pointer != None:
            result = result + str(pointer.element) + " "
            pointer = pointer.nextNode
        return result

    # AddFirst
    def add_first(self, element):
        newNode = self._Node(element)
        newNode.nextNode = self._head
        self._head = newNode
        self._size += 1

    def __len__(self):
        return self._size


def main():
    myList = singlyLinkedList()
    myList.add_first(10)
    myList.add_first(20)
    myList.add_first(30)
    print(str(myList))
    print(len(myList))


main()
