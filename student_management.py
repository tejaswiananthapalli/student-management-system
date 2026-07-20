#students=[]
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
    student={
      "Name":name,
      "Roll No":roll,
      "Branch":branch
    }
    students.append(student)
    print("Students added successfully")
  elif choice==2:
    print("Students View")
    print("-"*20)
    if (len(students)==0):
      print("There are no student details here")
    else:
            print("\nStudent Records")
            for student in students:
                print("---------------------------")
                print("Name   :", student["Name"])
                print("Roll   :", student["Roll"])
                print("Branch :", student["Branch"])
  elif choice==3:
    print("Thank you")
    break
  else:
    print("Invalid choice")
    
