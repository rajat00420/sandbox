__author__ = 'jc441938'
vowels=['a','e','i','o','u']
vowels_count=0
name=input("enter your name:")
for c in name:
    if c.lower() in vowels:
     vowels_count +=1
     print(vowels_count)
     print('out of {} letter, {} has {} vowels'.format(len(name),name,vowels_count))

my_list=[1,2,3,4]
for e in my_list:
    print(e, end='')





choice = input("choose a,b,c or d: ")
while choice not in ["a,b, c or d:"]:
    print("invalid input")
    choice = input("a,b,c or d:" )







