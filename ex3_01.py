hours = input('Enter the hours: ')
rate = input('Enter the rate:')
fh = float(hours)
fr = float(rate)
if fh > 40:
    #print('Overtime')
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    #print(reg,otp)
    xp = reg + otp
else:
    #print('Regular')
    xp = fh * fr
print('Payment: ', xp)