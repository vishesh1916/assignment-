words = ["eat", "tea", "tan", "ate", "nat", "bat"]
ag = {}

for word in words:
    key = ''.join(sorted(word))
    if key in ag:
        ag[key].append(word)
    else:
        ag[key] = [word]

result = list(ag.values())
print(result)                                   