# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not in line.startswith("X-DSPAM-Confidence:"):
        continue
    else: 
        count += 1
        total += float(line[19:])
print("Average spam confidence:", total/count)
