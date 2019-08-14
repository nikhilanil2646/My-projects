<<<<<<< HEAD
import json
while True:
  choice=int(input("\n\nEnter 1 to to make new file \nEnter 2 to add students \nEnter 3 to take attendence \nEnter 4 to view attendence\nEnter 5 to exit\nInput your choice: "))
  if choice==1:
        newfilename=input("Enter file new name")         
        fp=open(f"{str(newfilename)}"+".txt",'w')
        print("File has been created. ")
        data={'name':{}}
        json.dump(data,fp)
        fp.close()
  if choice==2:
    filename=input("Enter file name")
    name=input("Enter student name: ")
    
    while name:             
        fp=open(f"{str(filename)}"+".txt",'r')
        data=json.load(fp)
        fp.close()
        fp=open(f"{str(filename)}"+".txt",'w')
        data['name'].update([(name , list())])
        json.dump(data,fp)
        fp.close()
        print("student added.")
        print(data)
        name=input("Enter student name: ")
        
        
  if choice==3:
        filename=input("Enter file name")         
        fp=open(f"{str(filename)}"+".txt",'r')
        data=json.load(fp)
        for item in data['name'].keys():
           
            data['name'][item].append(input(f"{item} is present or absent? "))
            if data['name'][item][-1]:
               data['name'][item][-1]='Absent'
            else:
                data['name'][item][-1]='Present'
        fp.close()
        fp=open(f"{str(filename)}"+".txt",'w')
        json.dump(data,fp)
        fp.close()
  if choice==4:
    filename=input("Enter file name")         
    fp=open(f"{str(filename)}"+".txt",'r')
    data=json.load(fp)
    print(json.dumps(data,indent=5))
        
  if choice==5:
      exit(1)
            
            
            
            
            
=======
import json
while True:
  choice=int(input("\n\nEnter 1 to to make new file \nEnter 2 to add students \nEnter 3 to take attendence \nEnter 4 to view attendence\nEnter 5 to exit\nInput your choice: "))
  if choice==1:
        newfilename=input("Enter file new name")         
        fp=open(f"{str(newfilename)}"+".txt",'w')
        print("File has been created. ")
        data={'name':{}}
        json.dump(data,fp)
        fp.close()
  if choice==2:
    filename=input("Enter file name")
    name=input("Enter student name: ")
    
    while name:             
        fp=open(f"{str(filename)}"+".txt",'r')
        data=json.load(fp)
        fp.close()
        fp=open(f"{str(filename)}"+".txt",'w')
        data['name'].update([(name , list())])
        json.dump(data,fp)
        fp.close()
        print("student added.")
        print(data)
        name=input("Enter student name: ")
        
        
  if choice==3:
        filename=input("Enter file name")         
        fp=open(f"{str(filename)}"+".txt",'r')
        data=json.load(fp)
        for item in data['name'].keys():
           
            data['name'][item].append(input(f"{item} is present or absent? "))
            if data['name'][item][-1]:
               data['name'][item][-1]='Absent'
            else:
                data['name'][item][-1]='Present'
        fp.close()
        fp=open(f"{str(filename)}"+".txt",'w')
        json.dump(data,fp)
        fp.close()
  if choice==4:
    filename=input("Enter file name")         
    fp=open(f"{str(filename)}"+".txt",'r')
    data=json.load(fp)
    print(json.dumps(data,indent=5))
        
  if choice==5:
      exit(1)
            
            
            
            
            
>>>>>>> ffa54a7009b3986a920100cbf48d0af75002874e
