num=input("enter the three digit num : ")
num=int(num)
num1=num
#get the last digit 
reverse=num1%10
sum=num1%10
reverse=reverse*10
num1=num1/10
num1=int(num1)
#get the 2nd last digit(now last) and adding it
reverse=reverse+(num1%10)
reverse=int(reverse)
reverse=reverse*10
sum=int(sum)
sum = sum+(num1%10)

num1=num1/10
num1=int(num1)
reverse=reverse+(num1%10)
reverse=int(reverse)
sum=int(sum)
sum = sum+(num1%10)


print("the reverse number is  : " , reverse)
print("the sum of digit is : " , sum)