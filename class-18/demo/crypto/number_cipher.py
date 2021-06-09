def encrypt(plain, key):

    encrypted = ""

    for char in plain:
        num = (int(char) + key) % 10
        encrypted += str(num)

    return encrypted


def decrypt(plain, key):
    return encrypt(plain, -key)


if __name__ == "__main__":

    encrypted = encrypt("1234", 1)
    assert encrypted == "2345"
    assert decrypt(encrypted, 1) == "1234"

    encrypted = encrypt("9999", 1)
    assert encrypted == "0000", encrypted
    assert decrypt(encrypted, 1) == "9999"

    encrypted = encrypt("9999", 2)
    assert encrypted == "1111", encrypted
    assert decrypt(encrypted, 2) == "9999"

    encrypted = encrypt("9999", -2)
    assert encrypted == "7777", encrypted
    assert decrypt(encrypted, -2) == "9999"

    encrypted = encrypt("1111", -2)
    assert encrypted == "9999", encrypted
    assert decrypt(encrypted, -2) == "1111"

    print("TESTS PASSED")
