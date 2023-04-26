# Python program to find the SHA-1 message digest of a file

import hashlib


def hash_file(filename):
    h = hashlib.sha1()

    with open(filename, "rb") as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            h.update(chunk)

    return h.hexdigest()


message = hash_file("jijo.jpeg")
print(message)
