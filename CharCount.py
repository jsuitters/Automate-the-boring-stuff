import pprint

message = input("Enter text to be counted")
count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

pprint.pprint(count)