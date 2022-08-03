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


def decrypt(encrpyted_text, n):
    if n <= 0:
        return encrpyted_text
    li = list(range(len(encrpyted_text)))
    final_li = [
        *sorted(filter(lambda x: x % 2, li)),
        *sorted(filter(lambda x: x % 2 == 0, li)),
    ]
    thisdict = {}
    num, i = 0, 0
    while i < len(encrpyted_text):
        thisdict.update({encrpyted_text[i]: final_li[i]})
        i += 1

    return thisdict, final_li


if __name__ == "__main__":
    print(encrypt("Say God", 1))
    print(decrypt("LLkjklmekfwejfjke", 1))
