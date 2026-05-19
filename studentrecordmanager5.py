"""  Project: Student Records Manager

File: students.txt
Features to implement:
	1.	Add student – name and marks
	2.	List all students
	3.	Search student by name
	4.	Update student marks
	5.	Delete student
	6.	Exit program. """
 
import os
import sys
def condition():
 if not os.path.exists("studentinfo.txt"):
   f=open("studentinfo.txt","x")
   f.close()
        
def list_info():
    condition()
    with open("studentinfo.txt", "r") as f:
        lines = f.readlines()  # Read all lines once
        if len(lines) == 0:
            print("file is empty!")
        else:
            details()  # Call your details() function
def details():
     with open("studentinfo.txt","r")as f:
         line=[k.strip().split(",")for k in f.readlines()]
         print("after modifing! : \n")
         for name,value in line:
            print(f"name :{name} marks: {value}")
    
        
def add():
    with open("studentinfo.txt","a") as f:
     userinput=input("enter the name if the student ").strip()
     while True:
      second=input("enter the marks of the student!").strip()
      if second.isdigit():
            second=int(second)
            break
      else:
           print("plese enter  marks in digits , Try Again! ")
           
     f.write(f"{userinput},{second}\n")
     details()

def search():
    list_info()
    userinput=input("enter the name of the student to search : ").strip()
    with open("studentinfo.txt","r")as f:
        found=False
        line=[l.strip().split(",")for l in f.readlines()]
        for name,marks in line:
            if name.lower()==userinput.lower():
                print(f"found {name}")
                print(f"details are name:  {name} , marks : {marks}")
                found=True
    if not found:
        print("not found!")
def update():
    with open("studentinfo.txt","r")as f:
       userinput=input("enter the name of the student to search! ").strip()
       change=[]
       found=False
       line=[k.strip().split(",")for k in f.readlines()]
       for name,marks in line:
           if name.lower()== userinput.lower():
               print(f"found {name}")
               found=True
               second=input(f"enter marks to update for {name}").strip()
               while True:
                try:
                   if second.isdigit():
                    second=int(second)
                    break
                except:
                   print("please enter a digit , Try Again!")
               change.append(f"{name},{second}\n")
           else:
                change.append(f"{name},{marks}\n")
    with open("studentinfo.txt","w")as f:
        f.writelines(change)
    
    if not found:
        print("not found , no update occours")
    
def delete():
    list_info()
    with open("studentinfo.txt","r")as f:
        update=[]
        updated=False
        found=False
        line=[k.strip().split(",")for k in f.readlines()]
        userinput=input("enter the name of the student to delete info!").strip()
        for name,marks in line:
         if name.lower()==userinput.lower():
             print(f"found {name} , marks: {marks}")
             found=True
             second=input("enter yes to del / no to skip").lower().strip()
             if second == "yes":
                 print("deleted successfully")
                 updated=True
             elif second=="no":
                 print("you enter no , skiped !")
         else :
             update.append(f"{name},{marks}")
    with open("studentinfo.txt","w")as f:
        f.writelines(update)
    if not updated:
        print("no deletion occours!")
    if not found:
        print("not found!")
    details()
while True:       
 userinput=input("enter list to check list \n enter add to add \n enter search to search \n enter del to delete \n enter update to update\n enter exit to exit\n").strip().lower()
 if userinput == "list":
   list_info()
 elif userinput=="add":
    add()
 elif userinput=="search":
    search()
 elif userinput=="update":
    update()
 elif userinput=="del":
    delete()
 elif userinput=="exit":
    sys.exit()
 else:
    print("enter an invalid!")
    
            
                 
            
    
    
          
        
         
 
    

