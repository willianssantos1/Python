n1 n2 n3 = input().split()

num1 = int(n1)
num2 = int(n2)
num3 = int(n3)

if(num1 >= num2 and num1 >= num3):
    print("{} eh o maior".format(num1))
elif(num2 >= num1 and num2 >= num3):
    print("{} eh o maior".format(num2))
else:
    print("{} eh o maior".format(num3))
