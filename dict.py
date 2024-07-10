
d = {} # d = dict()
print(type(d))
<class 'dict'>
d = { 1: "first", 2: "second", 3: "third" }
# { key: value, key: value, ... }

# key must be unique
# if key is duplicated, the last value will be used
d = { 1: "first", 2: "second", 1: "first again" }
print(d)
{1: 'first again', 2: 'second'}
d[4] = "fourth"
print(d)
{1: 'first again', 2: 'second', 4: 'fourth'}
# key must be hashable -> int, float, str, tuple (immutable)
d = { [1, 2]: "list" } # TypeError: unhashable type: 'list'
d = { "name": "T", "location": "LA" }
print(d["name"])
T
d = { "name": "T", "location": "LA" }
# del
del d["name"]
print(d)

del d
print(d) # NameError: name 'd' is not defined
{'location': 'LA'}
print(dir(dict))
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# dict.clear() -> remove all items (clears the dictionary)
d = { "name": "T", "location": "LA" }
d.clear()
print(d)
{}
# dict.copy() -> returns a shallow copy of the dictionary
d = { "name": "T", "location": "LA" }
d2 = d.copy()
print(d2)
{'name': 'T', 'location': 'LA'}
d = { "name": "T", "location": "LA" }

# dict.keys() -> returns a view object that displays a list of all the keys in the dictionary
print(list(d.keys()))

# dict.values() -> returns a view object that displays a list of all the values in the dictionary
print(list(d.values()))
['name', 'location']
['T', 'LA']
d = { "name": "T", "location": "LA" }
# dict.get(key, default) -> returns the value of the specified key
print(d.get("name"))

print(d.get("age")) # done not throw an error, instead returns None
print(d.get("age", 19)) # returns 19 as the key is not found but does not change the dictionary
# print(d["age"]) # KeyError: 'age'
T
None
19
{'name': 'T', 'location': 'LA'}
# dict.setdefault(key, default) -> returns the value of the specified key

d = { "name": "T", "location": "LA" }
print(d.setdefault("age", 19)) # since the key is not found, setdefault adds it to the dictionary
print(d)
19
{'name': 'T', 'location': 'LA', 'age': 19}
# dict.fromkeys(seq, value) -> returns a dictionary with the specified sequence of keys with the specified value
lst = ["name", "age", "location"]
d = dict.fromkeys(lst, "unknown")
print(d)

d["name"] = "T"
d["age"] = 19
print(d)
{'name': 'unknown', 'age': 'unknown', 'location': 'unknown'}
{'name': 'T', 'age': 19, 'location': 'unknown'}
# create a dictionary with keys from 1 to n with values as square of the key
n = int(input())
d = {i: i ** 2 for i in range(1, n + 1)}
print(d)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
