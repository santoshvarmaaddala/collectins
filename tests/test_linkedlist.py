from collectins.linkedlist import LinkedList
import pytest

def test_append_single_element():
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)

    assert l1.head.val == 1
    assert l1.head.next.val == 2
    assert l1.head.next.next is None

def test_append_multiple_elememt():
    l1 = LinkedList()
    l1.append(10)
    l1.append(20)
    l1.append(30)

    assert l1.head.val == 10
    assert l1.head.next.val == 20
    assert l1.head.next.next.val == 30


def test_length_linkedlist():
    l1 = LinkedList()
    l1.append(10)
    assert len(l1) == 1

    l1.append(20)
    assert len(l1) == 2

    l1.append(30)
    assert len(l1) == 3

def test_get_item():
    l1 = LinkedList()
    l1.append(10)
    node1 = l1[0]

    assert l1[0] == node1

    with pytest.raises(IndexError):
        _ = l1[10]
