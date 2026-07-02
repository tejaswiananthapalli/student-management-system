print("___Welcome to simple calculator____")
print("\n1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice=int(input("Enter your choice"))
if choice==1:
  n1=int(input("Enter first number: "))
  n2=int(input("Enter next number: "))
  print("Addition is: ",n1+n2)
elif choice==2:
  n1=int(input("Enter first number: "))
  n2=int(input("Enter number which is smaller than n1: "))
  print("Result: ",n1-n2)
elif choice==3:
   n1=int(input("Enter first number: "))
   n2=int(input("Enter next number: "))
   print("Result: ",n1*n2)
elif choice==4:
   n1=int(input("Enter first number: "))
   n2=int(input("Enter next number except zero: "))
   print("Result: ",n1//n2)
else:
  print("Invalid choice")
  

  
