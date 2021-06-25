import pytest
from hashtable import Hashtable

# add


def test_exists():
    assert Hashtable


def test_add():
    ht = Hashtable()
    actual = ht.add("apple", 42)
    expected = None
    assert actual == expected


def test_get_apple():
    ht = Hashtable()
    ht.add("apple", 42)
    actual = ht.get("apple")
    expected = 42
    assert actual == expected


def test_get_banana():
    ht = Hashtable()
    ht.add("banana", 9)
    actual = ht.get("banana")
    expected = 9
    assert actual == expected


def test_unknown_key():
    ht = Hashtable()
    ht.add("banana", 9)
    actual = ht.get("cucumber")
    expected = None

    assert actual == expected


def test_hash_apple():
    ht = Hashtable()
    actual = ht.hash("apple")  # in range index
    assert 0 <= actual <= 1024


def test_hash_banana():
    ht = Hashtable()
    actual = ht.hash("banana")  # in range index
    assert 0 <= actual <= 1024


# TODO: needs contains test
# TODO: how can we test that collisions are handled?
