fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst =  list()
for line in fh:
    if (line.startswith('From ')):
        email = line.split()
        emailAdr = email[1]
        if emailAdr != None:
            print(emailAdr)
            count += 1
    

print("There were", count, "lines in the file with From as the first word")
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst =  list()
for line in fh:
    if (line.startswith('From ')):
        email = line.split()
        emailAdr = email[1]
        if emailAdr != None:
            print(emailAdr)
            count += 1
    

print("There were", count, "lines in the file with From as the first word")
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst =  list()
for line in fh:
    if (line.startswith('From ')):
        email = line.split()
        emailAdr = email[1]
        if emailAdr != None:
            print(emailAdr)
            count += 1
    

print("There were", count, "lines in the file with From as the first word")
