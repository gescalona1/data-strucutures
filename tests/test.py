def method(obj: dict, key: str, value) -> dict:
    if "." in key:
        keys = key.split(".")
        a = {}
        a[keys[1]] = value
        obj[keys[0]] = a
    else:
        obj[key] = value
    return obj

# test
print(method({}, "hamburger", 5))
print(method({}, "food.hamburger", 5))
print(method({"food": {"hamburger": 1}}, "food.hamburger", 5))
print(method({"food": {"pizza": "yummy", "hamburger" : 1 }}, "food.hamburger", 5))



