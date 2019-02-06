#for loops are traditionally used
#when you have a block of code which
#you want to repeat a fixed number of times

mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)

mylist = [100,200,300,400,500]
for num in mylist:
    print(num)

#adding if
for num in mylist:
    #check for even
    if num % 2 ==0:
        print(num)