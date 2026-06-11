print("FRIEND DIRECTORY")

d={}
import json
x="y"

while x=="y":
    name=input("Enter name of the person")
    num=int(input("Enter the persons number"))
    d[name]=num
    x=input("Do you want to enter any more records? (y/n)")

while True:
    
    print(json.dumps(d, indent=2))
    print("*****MENU*****")
    print("1. Search in records")
    print("2. Delete a record")
    print("3. Exit")
    
    x=int(input("Enter operation: "))
    
    if x==1:
        print(d.get(input("ENTER NAME TO SEARCH"),"NOT FOUND!!"))
        
    elif x==2:
        del d[input("ENTER NAME TO DELETE")]
        
    else:
        break
