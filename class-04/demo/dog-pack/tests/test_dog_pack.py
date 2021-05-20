import pytest
from dog_pack.dogs import Boxer, Puggle, Dog


def test_boxer_import():
    assert Boxer


def test_boxer_create():
    assert Boxer()  # no "new" needed


def test_boxer_with_name():
    marv = Boxer("Marv")
    actual = marv.name
    expected = "Marv"
    actual == expected


def test_boxer_no_name():
    pooch = Boxer()
    actual = pooch.name
    expected = "unknown"
    assert actual == expected


def test_boxer_greet(marv):
    actual = marv.greet()
    expected = "The name's Marv. Pleasure."
    assert actual == expected


def test_boxer_sleep(marv):
    actual = marv.sleep()
    expected = "zzz"
    assert actual == expected


def test_puggle_create():
    assert Puggle()


def test_puggle_no_name():
    pooch = Puggle()
    actual = pooch.name
    expected = "unknown"
    assert actual == expected


def test_puggle_name(lela):
    actual = lela.name
    expected = "Lela"
    assert actual == expected


def test_puggle_greet(lela):
    actual = lela.greet()
    expected = "I am Lela. I am SO HAPPY to meet you!"
    assert actual == expected


def test_puggle_sleep(lela):
    actual = lela.sleep()
    expected = "zzz"
    assert actual == expected


def test_puggle_is_a_dog():
    lela = Puggle("Lela")
    actual = isinstance(lela, Dog)
    expected = True
    assert actual == expected


@pytest.fixture
def marv():
    return Boxer("Marv")


@pytest.fixture
def lela():
    return Puggle("Lela")
