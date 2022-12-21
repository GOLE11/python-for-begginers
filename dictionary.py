#DICTIONARY
#un-ordered,changeable,indexed sympol{}
#key="name" value="yasin"
#making dict
#student = {"name" :"yasin","email" : "yasin@gmail.com","age" :25}
#student2 =dict(name="yasin",email="yasin@gmail.com",age=25)
#print(student1)
#print(student2)

#To define key in dict
#student = {"name" :"yasin","email" : "yasin@gmail.com","age" :25}
#x = student.get("email")
#x = student["email"]
#print(x)

#changing item in dict
#student = {"name" :"yasin","email" : "yasin@gmail.com","age" :25}
#student["name"]="ali"
#print(student)

#Looping over dict
#student = {"name" :"yasin","email" : "yasin@gmail.com","age" :25}

#to print only key

#for x in student:
    #print(x)

#to print only value

#for x in student:
    #print(student[x]) 
 
#to print both key and value  

#for x,y in student.items():
    #print(x,y)

#Check if item exists in dict  
#student = {"name" :"yasin","email" : "yasin@gmail.com","age" :25}
#if "email" in student:
    #print("yes")
#else:
    #print("nop")    

#To check length of dict items
#print(len(student))
 
#to add an item in dict
#student = {"name" :"yasin","email" : "yasin@gmail.com","age" :25}
#student["subject"]="english"
#print(student)

#To remove something from dict
#student = {"name" :"yasin","email" : "yasin@gmail.com","age" :25}
#student.pop("age")
#print(student)

#or
#student.popitem()
#print(student)
   
#To delete entire dict
#del student
#print(student)

#to clear the dict items
#sudent.clear()
#print(student)

#NESTED its important for data base making.
#students = {
#"student1":{    
           #"name": "yasin",
           #"email": "yasin@gmail.com",
           #"subject": "english",
           #"age": 25,
           #"Enrolled": True
           #},
#"student2":{
            #"name": "ali",
            #"email": "ali@gmail.com",
            #"subject": "math",
            #"age": 30,
            #"Enrolled": False
#}   

#}

#print(students)

#To make nested from two dict items

#student1 = {    
           #"name": "yasin",
           #"email": "yasin@gmail.com",
           #"subject": "english",
           #"age": 25,
           #"Enrolled": True
          # }
#student2 = {
         #   "name": "ali",
         #   "email": "ali@gmail.com",
         #   "subject": "math",
         #   "age": 30,
         #   "Enrolled": False
#}   

#students = {
   # "student1":student1,
    #"student2":student2
#}

#print(students)
