#Print number 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1

#Print number 100 to 1
# i=100
# while i>0:
#     print(i)
#     i-=1

#Print multiplication table
# i=1
# n=2
# while i<11:
#     print(i*n)
#     i+=1

#Print list element
# l=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<len(l):
#     print(l[i])
#     i+=1

#Search for number in tuple
# t=(1,4,9,16,25,36,49,64,81,100)
# i=0
# n=64
# while i<len(t):
#     if(t[i] == n):
#         print(n," index is ",i)
#     i+=1

#Print list element
# l=[1,4,9,16,25,36,49,64,81,100]
# for i in l:
#     print(i)
# else:
#     print("List print Completed")

#Search 
# t=(1,4,9,16,25,36,49,64,81,100)
# n=49
# idx=0
# for i in t:
#     if(i == n):
#         print("Found at idx ",idx)
#         break
#     idx+=1
# else:
#     print("Not Found")

#print 1 to 100
# for i in range(1,101):
#     print(i)

#print 100 to 1
# for i in range(100,0,-1):
#     print(i)

#Print multiplication
# n=int(input("Enter a Number : "))
# for i in range(1,11):
#     print(n*i)

#WAP to find sum of n numbers
# n=int(input("Enter a Number : "))
# i=1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1
# print(sum)

#WAP to find factorial
n=int(input("Enter a Number : "))
fact=1
for i in range(1,n+1):
    fact*=i
else:
    print(fact)