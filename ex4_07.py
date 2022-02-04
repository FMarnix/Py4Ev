def computegrade(grade):
    fgrade = float(grade)
    if fgrade > 1.0:
        rate = 'Invalid Score'
    elif fgrade >= 0.9 and fgrade <= 1.0:
        rate = 'A'
    elif fgrade >= 0.8 and fgrade < 0.9:
        rate = 'B'
    elif fgrade >= 0.7 and fgrade < 0.8:
        rate = 'C'
    elif fgrade >= 0.6 and fgrade < 0.7:
        rate = 'D'
    elif fgrade < 0.6:
        rate = 'F'
    else:
        print("Invalid Score")
    return rate
grade = input("Enter the score of the grade: ")
try:
    fgrade = float(grade)
except:
    print("Invalid Score")
    quit()

fn = computegrade(grade)

print(fn)


