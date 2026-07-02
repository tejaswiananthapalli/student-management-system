students=[]
while True:
  print("....Student Management System....")
  print("\n1. Add Student")
  print("2.View Student")
  print("3.Exit")
  choice=int(input("enter your choice: "))
  if choice==1:
    name=input("Enter student's name: ")
    roll=input("Enter roll number: ")
    branch=input("Enter branch: ")
  elif choice==2:
    print("view Student feature will bw added soon")
  elif choice==3:
    print("Thank you")
  else:
    print("Invalid choice")
    
