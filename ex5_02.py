largest = None
smallest = None
num = 0
while True:
    try:
        num = input("Enter a number: ")
        if num == 'done':
            break
        inum = int(num)
        if smallest is None and largest is None:
            smallest = inum
            largest = inum
        elif smallest > inum:
            smallest = inum
        elif largest < inum:
            largest = inum
    except:
        print('Invalid input')
        continue
print("Maximum is",largest)
print("Minimum is",smallest)
