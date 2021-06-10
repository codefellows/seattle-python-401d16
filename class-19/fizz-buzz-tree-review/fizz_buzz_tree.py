from collections import deque


def fizz_buzz_tree(tree):
    return tree.clone(fizzify)


def fizz_buzz_tree_longer(tree):

    fizzy_root = fizzy_copy(tree.root)

    pairs = Queue()
    pairs.enqueue((tree.root, fizzy_root))

    while not pairs.is_empty():
        source_front, fizzy_front = pairs.dequeue()

        for source_child in source_front.children:
            fizzy_child = fizzy_copy(source_child)
            fizzy_front.children.append(fizzy_child)
            pair = (source_child, fizzy_child)
            pairs.enqueue(pair)

    return KaryTree(fizzy_root)


def fizzy_copy(node):
    fizzy_value = fizzify(node.value)
    return Node(fizzy_value)


def fizzify(value):
    fizzy_value = ""
    if value % 3 == 0:
        fizzy_value += "Fizz"

    if value % 5 == 0:
        fizzy_value += "Buzz"

    return fizzy_value or str(value)


def fizzify_seven(value):
    fizzy_value = ""
    if value % 3 == 0:
        fizzy_value += "Fizz"

    if value % 5 == 0:
        fizzy_value += "Buzz"

    if value % 7 == 0:
        fizzy_value += "hip hop hippity...."

    return fizzy_value or str(value)


class Queue:
    """Queue implementation using deque under the hood"""

    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.is_empty():
            raise EmptyError(self.dequeue)

        return self.storage.popleft()

    def peek(self):
        if self.is_empty():
            raise EmptyError(self.peek)

        return self.storage[0]

    def is_empty(self):
        return len(self.storage) == 0


class EmptyError(Exception):
    def __init__(self, method):
        super().__init__(
            f"Cannot call {method.__name__} method on empty Queue"
        )


class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def breadth_first(self):
        queue = Queue()

        collection = []

        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()
            collection.append(node.value)
            for child in node.children:
                queue.enqueue(child)

        return collection

    def clone(self, converter=None):
        """
        return clone of self
        """

        clone_root = self.root.clone(converter)
        clone_tree = KaryTree(clone_root)

        pairs = Queue()

        pairs.enqueue((self.root, clone_root))

        while not pairs.is_empty():
            source_node, clone_node = pairs.dequeue()
            for source_child_node in source_node.children:
                clone_child_node = source_child_node.clone(converter)
                pair = (source_child_node, clone_child_node)
                pairs.enqueue(pair)
                clone_node.children.append(clone_child_node)

        return clone_tree


class Node:
    """K-Ary Tree Node"""

    def __init__(self, value):
        self.value = value
        self.children = []

    def clone(self, converter=None):
        value = self.value

        if converter:
            value = converter(value)

        return Node(value)


if __name__ == "__main__":

    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)
    eleven = Node(11)
    twelve = Node(12)
    thirteen = Node(13)
    fourteen = Node(14)
    fifteen = Node(15)

    """
                            1
                2                       3
            4  5  6               7     8          9
           10  11 12              13            14   15
    """

    one.children = [two, three]
    two.children = [four, five, six]
    three.children = [seven, eight, nine]
    four.children = [ten]
    five.children = [eleven]
    six.children = [twelve]
    seven.children = [thirteen]
    nine.children = [fourteen, fifteen]

    kt = KaryTree()

    kt = KaryTree(one)

    # print(kt.breadth_first())

    def ellipsis(value):
        return f"... {value}"

    clone = kt.clone(fizzify_seven)

    print(clone.breadth_first())

    kt.root.value = 999

    print(clone.breadth_first())
