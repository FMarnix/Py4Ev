def computepay(hours, rate):
    print("In compute pay", hours, rate)
    if hours > 40:
    #print('Overtime')
        reg = hours * rate
        otp = (hours - 40.0) * (rate * 0.5)
        #print(reg,otp)
        pay = reg + otp
    else:
        #print('Regular')
        pay = hours * rate
    return pay

hours = input('Enter the hours: ')
rate = input('Enter the rate:')
fh = float(hours)
fr = float(rate)

xp = computepay(fh,fr)

print('Payment: ', xp)