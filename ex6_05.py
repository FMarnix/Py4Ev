text = 'X-DSPAM-Confidence:0.8475'
doub = text.find(':')
num = text[doub+1:]
print(float(num))