"""
Implementing a pseudo-encryption algorithm which given a string S and an integer N
concatenates all the odd-indexed characters of S with all the even-indexed characters of S,
this process should be repeated N times.
"""


def encrypt(text, n):
    new_text = ""
    if n <= 0:
        return text
    i = 0
    length = len(text)
    while i < length:
        if i % 2 != 0:
            new_text += text[i]
        i += 1
    i = 0
    while i < length:
        if i % 2 == 0:
            new_text += text[i]
        i += 1
    if n != 1:
        return encrypt(new_text, n - 1)
    else:
        return new_text


if __name__ == "__main__":
    print(encrypt("This is a test!", 2))
