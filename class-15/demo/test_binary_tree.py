import pytest
from binary_tree.binary_tree import Node, BinaryTree, BinarySearchTree


@pytest.mark.skip("pending")
def test_node_has_value():
    node = Node("apple")
    assert node.value == "apple"


@pytest.mark.skip("pending")
def test_node_has_left_of_none():
    node = Node("apple")
    assert node.left is None


@pytest.mark.skip("pending")
def test_node_has_right_of_none():
    node = Node("apple")
    assert node.right is None


@pytest.mark.skip("pending")
def test_create_binary_tree():
    tree = BinaryTree()
    assert tree


@pytest.mark.skip("pending")
def test_binary_tree_has_root():
    tree = BinaryTree()
    assert tree.root is None


@pytest.mark.skip("pending")
def test_create_binary_search_tree():
    tree = BinarySearchTree()
    assert tree


@pytest.mark.skip("pending")
def test_binary_search_tree_has_root():
    tree = BinarySearchTree()
    assert tree.root is None


@pytest.mark.skip("pending")
def test_add_to_empty_bst():
    tree = BinarySearchTree()
    tree.add(5)
    actual = tree.root.value
    expected = 5
    assert actual == expected


@pytest.mark.skip("pending")
def test_add_to_empty_bst_again():
    tree = BinarySearchTree()
    tree.add(7)
    actual = tree.root.value
    expected = 7
    assert actual == expected


@pytest.mark.skip("pending")
def test_add_lesser_to_not_empty_bst():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(2)
    actual = tree.root.left.value
    expected = 2
    assert actual == expected


@pytest.mark.skip("pending")
def test_add_greater_to_not_empty_bst():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(7)
    actual = tree.root.right.value
    expected = 7
    assert actual == expected


@pytest.mark.skip("pending")
def test_add_lesser_then_in_between():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(2)
    tree.add(3)
    actual = tree.root.left.right.value
    expected = 3
    assert actual == expected


@pytest.mark.skip("pending")
def test_add_greater_then_in_between():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(10)
    tree.add(7)
    actual = tree.root.right.left.value
    expected = 7
    assert actual == expected


@pytest.mark.skip("pending")
def test_bst_contains():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(10)
    tree.add(6)
    tree.add(7)
    actual = tree.contains(7)
    expected = True
    assert actual == expected


@pytest.mark.skip("pending")
def test_pre_order():
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(25)
    tree.add(75)
    tree.add(20)
    tree.add(80)
    tree.add(40)

    """
                50
            25      75
        20    40          80
    """

    actual = tree.pre_order()
    expected = [50, 25, 20, 40, 75, 80]
    assert actual == expected


@pytest.mark.skip("pending")
def test_in_order():
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(25)
    tree.add(75)
    tree.add(20)
    tree.add(80)
    tree.add(40)

    """
                50
            25      75
        20    40          80
    """

    actual = tree.in_order()
    expected = [20, 25, 40, 50, 75, 80]
    assert actual == expected


@pytest.mark.skip("pending")
def test_post_order():
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(25)
    tree.add(75)
    tree.add(20)
    tree.add(80)
    tree.add(40)

    """
                50
            25      75
        20    40          80
    """

    actual = tree.post_order()
    expected = [20, 40, 25, 80, 75, 50]
    assert actual == expected
