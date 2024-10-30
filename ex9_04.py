fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

handle = open(fname)
di =  dict()
for line in handle:
    if (line.startswith('From ')):
        email = line.split()
        # Extracting only the emails and add it to a new dict
        emailAdr = email[1].split() 
        for adress in emailAdr:
            di[adress] = di.get(adress,0) + 1

# Find the most common email adress and the number of appearences
largest = -1
name = None
for k, v in di.items():
    if v > largest:
        largest = v
        name = adress         
        
print(name, largest)