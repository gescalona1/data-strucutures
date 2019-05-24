from typing import List
import re


def method(obj: dict, key: str, value) -> dict:
    if "." in key:
        keys: List[str] = key.split(".")
        if obj and obj[keys[0]]:  # check if the object and if the key for it exists
            obj[keys[0]].update(method({}, keys[1], value))  # add a new key
        else:
            obj[keys[0]] = method({}, keys[1], value)  # if it doesn't exist, manually set the key-value
    else:
        obj[key] = value
    return obj


def encrypt_this(text: str) -> str:
    """Turn the message into a secret message"""
    words: List[str] = text.split()
    if len(words) == 1 and isinstance(words[0], str):
        word = words[0]
        first_char: int = ord(word[0])
        second = word[1]
        last = word[-1]
        # print(first_char, last, word[2:-2], second)
        return f"{first_char}{last}{word[2:-1]}{second}"
    elif len(words) > 1:
        return ' '.join([encrypt_this(word) for word in words])


def decrypt_this(text: str) -> str:
    """Turn the secret message into a regular message"""
    words: List[str] = text.split()
    if len(words) == 1 and isinstance(words[0], str):
        word: str = re.sub("\d*", "", words[0])
        first_letter: str = chr(int(re.sub("[a-z]", "", words[0])))
        last: str = word
        if len(last) == 1:
            last = ""
        else:
            last = word[0]
        return f"{first_letter}{word[-1]}{word[1:-1]}{last}"
    elif len(words) > 1:
        return ' '.join([decrypt_this(word) for word in words])

# test


print("-------Dictionary Editing-------")
print(method({}, "hamburger", 5))
print(method({}, "food.hamburger", 5))
print(method({"food": {"hamburger": 1}}, "food.hamburger", 5))
print(method({"food": {"pizza": "yummy", "hamburger": 1}}, "food.hamburger", 5))
print(method(method({"food": {"hamburger": 1}}, "food.hamburger", 5), "food.hamburger", 10))

print("-------Encrypt-------")
print(encrypt_this("Hello"), "Hello", "72olle")
print(encrypt_this("good"), "good", "103doo")
print(encrypt_this("hello world"), "hello world", "104olle 119drlo")

print("-------Decrypt-------")
print(decrypt_this("72olle 103doo 100ya"), "72olle 103doo 100ya", "Hello good day")
print(decrypt_this("82yade 115te 103o"), "82yade 115te 103o", "Ready set go")
