rate = input("Enter the score of the rate: ")
try:
    frate = float(rate)
except:
    print("Invalid Score")
    quit()
    
if frate > 1.0:
    print('Invalid Score')
elif frate >= 0.9 and frate <= 1.0:
    print('A')
elif frate >= 0.8 and frate < 0.9:
    print('B')
elif frate >= 0.7 and frate < 0.8:
    print('C')
elif frate >= 0.6 and frate < 0.7:
    print('D')
elif frate < 0.6:
    print('F')
else:
    print("Invalid Score")