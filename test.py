""" astr = 'Hello bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1

print(istr) """

""" def stuff():
    print('Hello')
    return
    print('World')

stuff() """

""" tot = 0
for i in [5,4,3,2,1]:
    tot = tot + i
print(tot) """

""" smallest_so_far = -1
for the_num in [9,41,12,3,74,15]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
print(smallest_so_far) """

""" n = 0
while n > 0:
    print('Lather')
    print('Rinse')
print('Dry off!') """

""" str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob) """

""" data = 'From stephen.marquar@uct.ac.za Sat Jan 5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3]) """

fhand = open('README.md')
print(fhand)