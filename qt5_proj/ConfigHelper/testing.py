import json
# import os

# path = os.getcwd()
# print(path)
# test_dict = []
with open(r"..\example.json", "rb") as f:
    test_dict = json.load(f)
print(test_dict)
print(type(test_dict))
