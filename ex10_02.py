name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

d = dict()
lst = list()

for line in handle:
    line = line.strip()
    if not line.startswith('From '): 
        continue
    line = line.split()
    time = line[5]
    hours = time.split(':')
    hour = hours[0].split()

    for i in hour:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

for k,v in d.items():
    lst.append((k,v))
lst = sorted(lst)

for k,v in lst:
    print(k,v)
