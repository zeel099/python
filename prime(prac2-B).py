num = int(input("Enter the number: "))

if num > 1:
     
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print("this number a prime number")
       
else:
   print("this number is not a prime number")